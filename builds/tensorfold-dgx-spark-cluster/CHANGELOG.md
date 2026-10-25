# CHANGELOG — TensorFold DGX Spark Cluster

## 2026-10-25 — v10e Production Closeout

**Production state: v10e (`3ccfeb2b`)**

### Performance
- p1d: 45.37 tok/s (C=1 prose)
- c1d: 94.07 tok/s (C=1 code)
- p4d: 121.45 tok/s (C=4 prose)
- c4d: **208.00 tok/s** (C=4 code) — +15.5% over v9 (180.09)
- m4d: 125.30 tok/s
- c4off: 38.63 tok/s

### Verification
- 0007 gate: target-colls/round=128.0, draft-colls/round=0.0 ✓
- Parity: 14/14 byte-exact (C=1+C=4, prose+code) ✓
- C=1 prose: `d5589b366369`
- C=1 code: `39191bf72982`

### Changes
- `patches/tp2draftgraph.py` = v10e (eager static buffers for ALL S=1..4)
- `patches/backups/` consolidated (v9, v10-graph, 0007, 0006, 32slot)
- `launch-tp2.sh` md5 `0bed2901` (both nodes match)
- `tp2.env` md5 `3f86d5c1` (both nodes match)
- Health check timeout increased to 15s in `qwen38-tf-swap-up.sh`
- llama-swap config: `qwen3.8-27b-tp2` in `resident` group, `persistent: true`, `swap: false`

### Parked
- `v10-graph` (`96fccac9`) in `patches/backups/` — CUDA graph replay broken on
  boot78+ (4.6× slow, all versions). Ready for clean-boot retesting.
- `v9` (`d0aa457a`) in `patches/backups/` — rollback checkpoint.

---

## 2026-10-24 — v10 Graph A/B Test

- Built v10 (`96fccac9`): v9 base + CUDA graph capture for S=1 and S=4
- Boot77: p1d 9.67 tok/s (graph replay broken)
- Boot78: v10m 9.85, v9check 9.97/155 (c4d), v9-nograph 45.65
- **Conclusion:** CUDA graph replay is a boot-state issue, not a code issue.
  All graph versions are 4.6× slow on boot78+; eager versions are unaffected.
- v10-graph parked for clean-boot retesting.

---

## 2026-10-23 — v9 Production (Phase 2 Final)

- v9 (`d0aa457a`): Graph D for S=1, fused `_dg_block_attention` for S>1
- Boot74/76 stable: p1d 45.92, c1d 92.80, p4d 120.77, c4d 180.09, m4d 120.17
- 0007 gate: 128.0/0.0 ✓
- 14/14 parity ✓

---

## 2026-10-23 — Phase 2 Final (launch-tp2.sh locked)

- `launch-tp2.sh` md5 `0bed2901` (both nodes)
- `--parallel 4 --context 262144 --prompt-cache-gib 16 --checkpoint-slots 32 --no-prefill-fp8`
- `CDMC=1 TP2_W8A16=1 TP2_BATCH_VERIFY=1 TP2_DRAFT_REPL=1 TF_SLOT_KV_CAP=16384`
- cpuset 5-9,15-19 (10x Cortex-X925)

---

## 2026-10-23 — 8-bit 4-stream Staged Variant

- 8-bit TP=2 staged variant: p1d 10.5, c4d 21.5 (Exited 133)
- Patch 0006 (W8A16 Triton): 32.2 / 136.6
- Boot 7/10 CDMC+262k: 48.5 / 220.0, TTFT 102–340 ms

---

## 2026-10-02 — c1 Resident Promotion

- c1 (spark1 .139 + spark2 .150) promoted to resident Qwen3.8-27B TF
- GLM failover kit stopped
- llama-swap: `qwen3.8-27b-tp2` in `resident` group
