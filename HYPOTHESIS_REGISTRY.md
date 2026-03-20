# HYPOTHESIS REGISTRY — FP-19 Agent-Assisted Vulnerability Triage

> **Project:** FP-19
> **Created:** 2026-03-20
> **Status:** PENDING (0/4 resolved)
> **Lock commit:** TBD
> **Lock date:** 2026-03-20

---

## H-1: LLM agent outperforms EPSS on precision@10 for KEV prediction

| Field | Value |
|-------|-------|
| **Statement** | A Claude Haiku agent ranking CVEs by exploitability achieves higher precision@10 than EPSS scores alone, using CISA KEV as ground truth. |
| **Prediction** | precision@10(agent) > precision@10(EPSS) by ≥15pp |
| **Falsification** | If agent precision@10 ≤ EPSS precision@10, the agent adds no triage value. |
| **Status** | PENDING |
| **Linked Experiment** | E1 |

---

## H-2: Enrichment data improves agent ranking quality

| Field | Value |
|-------|-------|
| **Statement** | Adding exploit database and vendor advisory data to CVE descriptions improves agent precision@10 by ≥10pp over CVE-description-only input. |
| **Prediction** | precision@10(CVE+ExploitDB+Vendor) > precision@10(CVE-only) by ≥10pp |
| **Falsification** | If enrichment does not improve precision, the agent extracts sufficient signal from CVE descriptions alone. |
| **Status** | PENDING |
| **Linked Experiment** | E2 |

---

## H-3: Agent + EPSS ensemble outperforms either alone

| Field | Value |
|-------|-------|
| **Statement** | A weighted ensemble of agent scores and EPSS scores achieves higher precision@10 than either method alone. |
| **Prediction** | precision@10(ensemble) > max(precision@10(agent), precision@10(EPSS)) |
| **Falsification** | If ensemble ≤ best individual method, the methods are redundant rather than complementary. |
| **Status** | PENDING |
| **Linked Experiment** | E3 |

---

## H-4: Agent performance degrades on older CVEs

| Field | Value |
|-------|-------|
| **Statement** | Agent precision@10 is lower for 2023 CVEs than 2025 CVEs, due to temporal distance from training data. |
| **Prediction** | precision@10(2025) > precision@10(2023) by ≥10pp |
| **Falsification** | If performance is stable across years, the agent generalizes well temporally. |
| **Status** | PENDING |
| **Linked Experiment** | E4 |

---

## Summary

| ID | Statement (short) | Prediction | Status |
|----|-------------------|-----------|--------|
| H-1 | Agent beats EPSS | ≥15pp precision@10 improvement | PENDING |
| H-2 | Enrichment helps | ≥10pp improvement with enrichment | PENDING |
| H-3 | Ensemble wins | Ensemble > best individual | PENDING |
| H-4 | Temporal degradation | 2025 > 2023 by ≥10pp | PENDING |
