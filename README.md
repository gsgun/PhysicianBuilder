---
description: Documentation for Projects In Progress and Deployed
---

# Physician Builder Projects

MIT License. Open Source.&#x20;

Completed:

* [ASCVD CVD 2024 Risk Calculators](https://app.gitbook.com/s/6Caf1JA5ufQharGpTSxg/predicting-cvd-risk-events)
* [Gupta NSQIP Risk Calculators](https://app.gitbook.com/s/6Caf1JA5ufQharGpTSxg/gupta-surgery-risk-scores)
* GRACE InHospital 6 month Risk Calculators
* [Admission Med Rec Tip Text](https://app.gitbook.com/s/6Caf1JA5ufQharGpTSxg/admission-med-rec-tip-text)
* [CathPCI Risk Calculators](https://app.gitbook.com/s/6Caf1JA5ufQharGpTSxg/cath-pci-gdmt)
* Sepsis QI Hospitalist
* [Standand Notes](https://app.gitbook.com/s/6Caf1JA5ufQharGpTSxg/standardnotes)



In Progress:

* Cardiac PCI Quality Metric
* Hospitalist Quality Metric Update
* [Secure Chat Templates Pharmacy](https://app.gitbook.com/s/6Caf1JA5ufQharGpTSxg/data-analytics)
* ED Scoring Tools Rule Updates



---

## Repository Architecture

Canonical layout maintained by the Physician Builder workbench:

```
PhysicianBuilder/
├── README.md · INDEX.md · SUMMARY.md (GitBook TOC)
├── ideas/
│   ├── triage-and-backlog.md     # Low-friction idea incubator + quick capture
│   └── rfc/                      # Formal specs: RFC-[XXX]-<slug>.md
├── builds/                       # Curated, cross-build component libraries
│   ├── cer-rules/                # CER patterns, criteria tables, property trees
│   ├── smarttools/               # SmartLinks, SmartLists, SmartPhrases, macros
│   ├── order-sets-navigators/    # Inpatient pathways, navigators, order set guides
│   ├── reporting-workbench/      # Criteria records, metric definitions, audit queries
│   └── protocols-uris/           # Hyperdrive/Hyperspace protocol URI routing & handlers
├── operational-sops/
│   ├── clinician-tip-sheets/     # Frontline physician education
│   └── automation-pipelines/     # Data transformation, Power Automate, SharePoint wiki
├── projects/                     # Ephemeral active build spaces (see template)
│   └── _template/                # PROJECT.md · ROADMAP.md · SESSION_LOG.md · SCRATCHPAD.md
└── <project-slug>/               # Per-build GitBook content (source of truth for deployed builds)
```

**Conventions**

- `INDEX.md` is the master machine-generated manifest of every doc in the repo.
- Per-project GitBook folders (e.g. `predicting-cvd-risk-events/`) remain the source of truth for *deployed* builds; `builds/*` holds reusable patterns extracted across builds.
- Zero-PHI mandate: no real MRNs, patient names, DOBs, exact admit/discharge timestamps, or identifying room numbers anywhere in this repo. Synthetic data only (e.g. `MRN 999000123`, `TEST-DOE, JOHN`, `Encounter Day 2`, `T-6h`). Internal IPs, intranet domains, and credentials are stripped before commit.
- New ideas → `ideas/triage-and-backlog.md`; promoted ideas get an RFC in `ideas/rfc/`; active builds get a project folder under `projects/`.
