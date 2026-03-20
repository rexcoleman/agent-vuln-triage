# FP-19: Agent-Assisted Vulnerability Triage

An LLM agent achieves 92% precision@10 on vulnerability triage but underperforms EPSS (100%). The ensemble of both reaches 98% precision with lower variance — the value is in complementarity, not replacement.

**Blog post:** [Your AI Can't Beat EPSS at Vulnerability Triage](https://rexcoleman.dev/posts/agent-vuln-triage/)

## Key Results

| Metric | Agent | EPSS | Ensemble |
|--------|-------|------|----------|
| Precision@10 | 92% | 100% | 98% |
| Variance | Higher | Lower | Lowest |
| Context reasoning | Yes | No | Yes |

## Quick Start

```bash
pip install -r requirements.txt
bash reproduce.sh
```

5 experiments (E0-E4). Claude 3 Haiku agent. 5 seeds. Pre-registered hypotheses with honest negative results. Built with [govML](https://rexcoleman.dev/posts/govml-methodology/) governance.
