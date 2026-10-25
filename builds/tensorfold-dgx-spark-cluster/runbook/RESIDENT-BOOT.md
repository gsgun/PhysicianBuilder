# Resident Boot & Recovery Runbook — c1 (Qwen3.8-27B TF)

## Normal Boot

```bash
# On spark1 (head, .139):
~/qwen38-tf-cluster/launch-tp2.sh

# Wait for health (~4-6 min for NCCL bootstrap):
for i in $(seq 1 90); do
  R=$(curl -fsS -m 15 http://127.0.0.1:8894/health 2>/dev/null || echo 000)
  [ "$R" = "200" ] && break
  sleep 2
done
echo "Health: $R"

# Verify:
curl -s http://192.168.8.139:8894/health | python3 -m json.tool
# Expected: {"status":"200","ready":true,"kv_usage":...,"active_streams":...}
```

## Health Check

- **Endpoint:** `GET /health` on :8894
- **Timeout:** 15s (set in `qwen38-tf-swap-up.sh`)
- **llama-swap:** `qwen3.8-27b-tp2` in `resident` group, `persistent: true`, `swap: false`
- **llama-swap healthCheckTimeout:** 4800s (80 min)

## Wedge Recovery

See skill `devops/qwen38-tp2-wedge-recovery` for the full runbook.

Quick recovery:
```bash
# Stop both containers
ssh spark1 'docker stop qwen38-tf-rank0'
ssh spark2 'docker stop qwen38-tf-rank1'

# Remove stale rank1 if present
ssh spark2 'docker rm -f qwen38-tf-rank1 2>/dev/null'

# Restart
ssh spark1 '~/qwen38-tf-cluster/launch-tp2.sh'
```

## Rollback to v9

```bash
ssh spark1 'cp ~/qwen38-tf-cluster/patches/backups/tp2draftgraph_v9_d0aa457a.py ~/qwen38-tf-cluster/patches/tp2draftgraph.py'
ssh spark2 'cp ~/qwen38-tf-cluster/patches/backups/tp2draftgraph_v9_d0aa457a.py ~/qwen38-tf-cluster/patches/tp2draftgraph.py'
# Reboot both containers (see above)
```

## Patch Deployment

```bash
# Deploy new patch to both nodes:
scp tp2draftgraph.py spark1:~/qwen38-tf-cluster/patches/tp2draftgraph.py
scp tp2draftgraph.py spark2:~/qwen38-tf-cluster/patches/tp2draftgraph.py

# Verify md5 match:
md5sum spark1:~/qwen38-tf-cluster/patches/tp2draftgraph.py spark2:~/qwen38-tf-cluster/patches/tp2draftgraph.py

# Reboot and verify:
ssh spark1 '~/qwen38-tf-cluster/launch-tp2.sh'
# Run bench + parity
```

## Known Issues

- **CUDA graph replay broken on boot78+** (4.6× slow, all versions). v10e avoids
  this by using eager static buffers. The parked `v10-graph` (`96fccac9`) is
  ready for clean-boot retesting.
- **Health-000 storms** (30-60 polls) on every boot are normal (~4-6 min NCCL
  bootstrap). Wait it out.
- **`fuser -k`** kills `nvidia-persistenced` — restart after.
- **Stale spark1 `rank1 Exited(1)`** — `docker rm` pre-launch.
