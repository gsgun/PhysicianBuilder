# TensorFold DGX Spark Cluster — Qwen3.8-27B 8-bit TP=2

Production-resident LLM cluster on dual NVIDIA DGX Spark (GB10 Grace-Blackwell),
serving `z-lab/Qwen3.8-27B` (8-bit affine, group_size=64) + `DFlash2` draft model
with tensor-parallelism across two nodes over 200GbE ConnectX-7 RoCEv2.

## Hardware & Topology

| Node   | IP            | Role  | GPU         | RAM      |
|--------|---------------|-------|-------------|----------|
| spark1 | 192.168.8.139 | rank0 | GB10 (88GiB)| 128 GiB  |
| spark2 | 192.168.8.150 | rank1 | GB10 (88GiB)| 128 GiB  |

- **Interconnect:** 200GbE ConnectX-7 RoCEv2 (`enp1s0f1np1`, MTU 9000)
- **NCCL:** 2.30.7, `NCCL_NVLS_ENABLE=0 NCCL_CUMEM_ENABLE=0 NCCL_MULTI_RANK_GPU_ENABLE=1`
- **Allreduce 8KB:** 37 µs (measured)
- **Management:** 192.168.8.0/24, head API on spark1 :8894

## Model & Memory Layout

- **Model:** `z-lab/Qwen3.8-27B` 8-bit affine (group_size=64) + `z-lab/Qwen3.8-27B-DFlash2`
- **Parallelism:** TP=2 (rank0 on spark1, rank1 on spark2)
- **Context:** 4 streams × 262,144 tokens = 1,048,576 pooled FP8 KV tokens
- **Precision:** `PREFILL_FP8=0` (bf16 prompt activations), FP8 KV cache
- **Memory:** 32 GiB used / 88 GiB available on spark1 (GB10 unified memory)
- **Prompt cache:** 16 GiB, 32 checkpoint slots

## Patch Stack (Production: v10e `3ccfeb2b`)

| Patch | Description |
|-------|-------------|
| `0006-fused-w8a16-affine` | W8A16 Triton fused affine kernel |
| `0007-tp2-multistream-batch` | Batch verify + auto-unhook (0 draft colls) |
| `0008a-replicated-dflash2` | Replicated rank-local DFlash2 (no NCCL for draft) |
| `0008b-v10e-fused-multistream-draft` | Per-stream BL fused `_dg_block_attention` S=1..4, eager static buffers |
| `0008-D2` (in launch) | 32 checkpoint slots |

### v10e Design

v10e = v9 base + eager static-buffer staging for ALL S ∈ {1,2,3,4} (no CUDA graph).
The fused `_dg_block_attention` kernel handles S>1 with per-stream `BL` strides
(`keys[s].shape[1]`), eliminating the cross-stream stride corruption that
plagued the original `BL = keys[0].shape[1]` assumption.

**CUDA graph replay is broken on boot78+** (4.6× slow, all versions) — a
boot-state issue, not a code issue. The parked `v10-graph` (`96fccac9`) in
`patches/experimental/` is ready for clean-boot retesting.

## Performance Progression

| Milestone | p1d (prose C=1) | c1d (code C=1) | p4d (prose C=4) | c4d (code C=4) | Notes |
|-----------|-----------------|----------------|-----------------|----------------|-------|
| 8-bit TP2 baseline | 10.5 | 21.5 | — | — | Exited 133 (crash) |
| Patch 0006 (W8A16) | 32.2 | 136.6 | — | — | Triton fused affine |
| Boot 7/10 CDMC+262k | 48.5 | 220.0 | — | — | TTFT 102–340 ms |
| **v10e (3ccfeb2b)** | **45.4** | **94.1** | **121.5** | **208.0** | 0 draft colls, 14/14 parity |

v10e is +15.5% over v9 on c4d (180.1 → 208.0 tok/s). The c4d target was
210–225 tok/s; v10e reaches 99% of the lower bound.

## Verification

- **0007 gate:** `target-colls/round=128.0`, `draft-colls/round=0.0` ✓
- **Parity:** C=1+C=4, prose+code = 14/14 byte-exact ✓
  - C=1 prose: `d5589b366369`
  - C=1 code: `39191bf72982`
- **Health:** `{"status":"200","ready":true,"kv_usage":0.0346,"active_streams":2}` ✓

## Files

```
patches/
  0006-fused-w8a16-affine.patch
  0007-tp2-multistream-batch.patch
  0008a-replicated-dflash2.patch
  0008b-v10e-fused-multistream-draft.py    # v10e (3ccfeb2b) — production
  experimental/
    tp2draftgraph_v10_graph_96fccac9.py    # v10-graph — parked for clean-boot test
launch-tp2.sh        # Sanitized boot script (no secrets)
tp2.env              # Runtime environment variables
bench/
  w8a16_c4.sh        # Benchmark harness
  parity_c4.sh       # 14/14 byte-exact parity harness
  phase1_scorecard.txt
  v10e_scorecard.txt
runbook/
  RESIDENT-BOOT.md   # Resident boot & recovery runbook
```

## Boot

```bash
# On spark1 (head):
~/qwen38-tf-cluster/launch-tp2.sh

# Health check:
curl -s http://192.168.8.139:8894/health
# Expected: {"status":"200","ready":true,...}

# Bench:
ssh spark1 '~/qwen38-tf-cluster/bench/w8a16_c4.sh'
```

## Rollback

```bash
# Revert to v9 (d0aa457a):
ssh spark1 'cp ~/qwen38-tf-cluster/patches/backups/tp2draftgraph_v9_d0aa457a.py ~/qwen38-tf-cluster/patches/tp2draftgraph.py'
ssh spark2 'cp ~/qwen38-tf-cluster/patches/backups/tp2draftgraph_v9_d0aa457a.py ~/qwen38-tf-cluster/patches/tp2draftgraph.py'
# Reboot both containers
```

## See Also

- Skill: `devops/w8a16-tp2-patch-ops` (patch manifest + perf history)
- Skill: `devops/qwen38-tp2-wedge-recovery` (wedge recovery runbook)
- Skill: `qwen38-cluster-recipe-dgx-sparks` (initial provisioning)
