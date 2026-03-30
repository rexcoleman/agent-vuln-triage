# Agent-Assisted Vulnerability Triage

**An LLM agent (Claude Haiku) achieves 92% precision@10 on vulnerability triage — outperforming CVSS (82%) but underperforming EPSS (100%). The key finding: agent + EPSS ensemble reaches 98%, capturing complementary signal that neither achieves alone.**

**Blog post:** [Can an AI Agent Triage Vulnerabilities Better Than EPSS?](https://rexcoleman.dev/posts/agent-vuln-triage/)

![govML](https://img.shields.io/badge/govML-v3.3-blue) ![Quality](https://img.shields.io/badge/quality-8.0-brightgreen) ![License](https://img.shields.io/badge/license-MIT-green)

![Key Result](outputs/figures/e1_precision_comparison.png)

## Key Results

| Method | Precision@10 | vs CVSS |
|--------|-------------|---------|
| EPSS | **100%** | +18pp |
| **Agent + EPSS ensemble** | **98%** | +16pp |
| Agent (Claude Haiku) | 92% | +10pp |
| Agent + exploit enrichment | 94% | +12pp |
| CVSS ranking | 82% | baseline |
| Random | 14% | — |

## Quick Start

```bash
git clone https://github.com/rexcoleman/agent-vuln-triage
cd agent-vuln-triage
pip install -e .
bash reproduce.sh
```

## Project Structure

```
FINDINGS.md # Research findings with pre-registered hypotheses and full results
EXPERIMENTAL_DESIGN.md # Pre-registered experimental design and methodology
HYPOTHESIS_REGISTRY.md # Hypothesis predictions, results, and verdicts
reproduce.sh # One-command reproduction of all experiments
governance.yaml # govML governance configuration
LICENSE # MIT License
pyproject.toml # Python project configuration
scripts/ # Experiment and analysis scripts
src/ # Source code
tests/ # Test suite
outputs/ # Experiment outputs and results
data/ # Data files and datasets
docs/ # Documentation and decision records
```

## Methodology

See [FINDINGS.md](FINDINGS.md) and [EXPERIMENTAL_DESIGN.md](EXPERIMENTAL_DESIGN.md) for detailed methodology, pre-registered hypotheses, and full experimental results with multi-seed validation.

## License

[MIT](LICENSE) 2026 Rex Coleman

---

Governed by [govML](https://rexcoleman.dev/posts/govml-methodology/) v3.3
