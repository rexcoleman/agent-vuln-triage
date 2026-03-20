#!/bin/bash
# Reproduce all experiments from scratch.
# Usage: bash reproduce.sh
set -euo pipefail
echo "TODO: Add experiment reproduction commands"
echo "Use nohup for long-running jobs (R35):"
echo "  nohup python -u scripts/run_experiments.py > ~/compute_logs/PROJECT_experiments.log 2>&1 &"

# --- Gate Validation (R50) ---
if [ -f "$HOME/ml-governance-templates/scripts/check_all_gates.sh" ]; then
    echo "--- Gate Validation (R50) ---"
    bash "$HOME/ml-governance-templates/scripts/check_all_gates.sh" .
else
    echo "WARN: govML not found — skipping gate validation (R50)"
fi
