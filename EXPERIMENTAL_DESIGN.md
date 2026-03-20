# Experimental Design Review — FP-19: Agent-Assisted Vulnerability Triage

> **Gate:** 0 (must pass before Phase 1 compute)
> **Date:** 2026-03-20
> **Target venue:** AISec Workshop (ACM CCS 2026)
> **lock_commit: `fb51534` (set after HYPOTHESIS_REGISTRY)
> **Profile:** contract-track
> **Budget:** ~$3-5 Claude API (Haiku)

---

## Novelty Claim

> First empirical comparison of LLM agent vulnerability triage against EPSS using CISA KEV as ground truth, with enrichment ablation and ensemble analysis.

---

## Comparison Baselines

| # | Method | Citation | How We Compare | Why This Baseline |
|---|--------|----------|---------------|-------------------|
| 1 | EPSS alone | Jacobs et al. 2021 | Agent vs EPSS on precision@k for KEV prediction | Industry standard. Reviewer expects this. |
| 2 | CVSS base score | FIRST.org | Simple severity ranking vs agent ranking | Naive baseline every practitioner uses. |
| 3 | Random ranking | Control | Lower bound on any ranking method | Ensures results exceed chance. |
| 4 | Agent + EPSS ensemble | This work | Combined ranking vs either alone | Tests complementarity. |

---

## Pre-Registered Reviewer Kill Shots

| # | Criticism | Planned Mitigation |
|---|----------|-------------------|
| 1 | "CISA KEV is biased toward high-profile vulnerabilities" | Acknowledged in Threats to Validity. We also report recall@k on the full NVD set. KEV is the best available proxy for "actually exploited." |
| 2 | "The agent just learned EPSS scores from training data" | We test with CVEs published AFTER the model's training cutoff. We also ablate: agent WITHOUT any EPSS data must still outperform random. |
| 3 | "N=100-200 CVEs is too small" | Each CVE tested with 5 seeds = 500-1000 ranking decisions. Unit of analysis is the ranking decision, not the CVE. |

---

## Ablation Plan

| Component | Hypothesis When Changed | Expected Effect | Priority |
|-----------|------------------------|-----------------|----------|
| Enrichment: CVE description only vs + exploit DB vs + vendor advisory | More enrichment = better ranking | Precision@10 improves with enrichment | HIGH |
| Agent model: Haiku vs no-agent (EPSS only) | Agent adds value beyond EPSS | Agent outperforms on KEV subset | HIGH |
| Prompt detail: minimal ("rank these CVEs") vs structured (role + criteria) | Structured prompt = better ranking | Structured improves precision@10 | MEDIUM |
| Temporal: CVEs from 2023 vs 2024 vs 2025 | Older CVEs may have more signal | Agent performance stable across years | MEDIUM |

---

## Ground Truth Audit

| Source | Type | Count | Known Lag | Positive Rate | Limitations |
|--------|------|-------|-----------|---------------|-------------|
| CISA KEV catalog | Authoritative (government) | ~1200 total, ~200 sample | 1-30 days from exploit to KEV listing | ~5% of all CVEs | Selection bias toward US-relevant, high-profile vulns |
| NVD CVE database | Reference | ~200 sample | Hours to days | N/A (all CVEs) | No exploitation signal |
| EPSS scores | Model output | API per CVE | Daily update | Continuous 0-1 | Circular if used as both feature and baseline |

### Alternative Sources Considered

| Source | Included? | Rationale |
|--------|-----------|-----------|
| ExploitDB | YES (enrichment) | Real exploit availability signal |
| Vendor advisories | YES (enrichment) | Patch urgency signal |
| VulnCheck KEV | NO | Proprietary, not reproducible |

---

## Statistical Plan

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Seeds | 5 (42, 123, 456, 789, 1024) | govML standard |
| CVEs per condition | 100-200 | Sampled from 2023-2025 KEV + non-KEV |
| Primary metric | Precision@10 (top 10 ranked CVEs, how many are KEV?) | Practitioner-meaningful: "are the top alerts real?" |
| Secondary metrics | NDCG@20, Recall@50, F1 | Completeness measures |
| Significance test | Paired t-test (same CVE set, different rankers) | Paired design |
| Multiple comparisons | Holm-Bonferroni correction for 4 baselines | Controls family-wise error rate |
| Effect size | ≥15pp precision@10 improvement over EPSS | Practitioner-meaningful |

---

## Related Work

| # | Paper | Year | Relevance |
|---|-------|------|-----------|
| 1 | Jacobs & Romanosky — "Exploit Prediction Scoring System (EPSS)" | 2021 | The baseline we test against |
| 2 | Spring et al. — "Prioritizing Vulnerability Response" | 2021 | SSVC framework, stakeholder-specific triage |
| 3 | Chen et al. — "ChatGPT for Vulnerability Detection" | 2023 | LLM applied to vulnerability analysis |
| 4 | Fang et al. — "LLM Agents Can Autonomously Exploit Vulnerabilities" | 2024 | LLM agents in offensive security |
| 5 | Yin et al. — "LLM for Software Vulnerability Detection: A Survey" | 2024 | Comprehensive survey of LLM+vuln landscape |
| 6 | Prior FP-05 (this portfolio) — "Vulnerability Prioritization ML" | 2026 | Our earlier work on this exact problem, without agents |

---

## Threats to Validity

| Threat | Type | Mitigation |
|--------|------|-----------|
| CISA KEV selection bias — overrepresents high-profile, US-relevant vulns | External validity | Acknowledged. Report results on KEV and full NVD separately. KEV is best available "actually exploited" proxy. |
| Data leakage — agent may have seen EPSS scores or KEV status during training | Internal validity | Test on CVEs published AFTER model training cutoff. Ablation: agent without EPSS input vs agent with EPSS. |
| EPSS circularity — using EPSS as both enrichment feature and baseline | Construct validity | Separate experiments: E1 uses EPSS as baseline only (agent gets no EPSS). E3 ensemble explicitly combines them. |
| Temporal bias — CVE exploitability changes over time | External validity | E4 tests across 3 year cohorts (2023, 2024, 2025). |
| Prompt engineering confound — results depend on prompt quality, not agent capability | Construct validity | Ablation E2 tests minimal vs structured prompts. Report prompt templates for reproducibility. |

---

## Audience Alignment

- **Audience:** Security practitioners running vulnerability management programs + AI builders evaluating agent capabilities
- **Portfolio position:** Bridges FP-05 (vuln prioritization ML, no agents) with agent-focused projects (FP-08/13/16). First project where an agent does REAL security work.
- **Distribution plan:** Blog post on rexcoleman.dev → LinkedIn (3K followers, security audience) → Reddit r/netsec → DEF CON AI Village CFP. The "can an AI triage your vulns?" angle is practitioner-clickable.

---

## Experiment Matrix

| ID | Question | IV | Levels | DV | Seeds |
|----|----------|-----|--------|-----|-------|
| E0 | Sanity: agent produces valid rankings | N/A | 5 known KEV CVEs | Valid score output | 1 |
| E1 | Agent vs baselines | Ranking method | Agent, EPSS, CVSS, Random | Precision@10, NDCG@20 | 5 |
| E2 | Enrichment ablation | Data sources | CVE-only, +ExploitDB, +Vendor, +All | Precision@10 | 5 |
| E3 | Ensemble analysis | Combination method | Agent+EPSS weighted, Agent+EPSS rank fusion | Precision@10 | 5 |
| E4 | Temporal analysis | CVE year | 2023, 2024, 2025 | Precision@10 per year | 5 |
