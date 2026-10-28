# Anthropic public-report index

A source-linked, AI-assisted triage compilation of **346 existing public issue reports**, with a separate appendix of **27 resolved vendor incidents**. Source snapshot: 28 October 2026. Independent community compilation; not affiliated with or endorsed by Anthropic.

**These are reporter allegations, not 346 independently verified errors or unique vulnerabilities. No runtime behavior was reproduced by this review.** Multiple cases may share a root cause. Open issue status at retrieval does not prove a failure persists in current releases. The requested target of 1,000 additional serious errors was not substantiated.

## Read the material

- [Categorized report index and correction notes](REPORT_INDEX.md)
- [CSV triage table](findings.csv)
- [Structured evidence and method](findings.json)
- [Downloadable HTML dossier and historical-incident appendix](review.html) — download and open locally; GitHub displays the source.

## Coverage

| Editorial category | Public reports |
|---|---:|
| Data integrity, deletion and recoverability | 73 |
| Access, privacy and permission controls | 78 |
| Resource exhaustion and process lifecycle | 38 |
| Billing, account attribution and cost visibility | 9 |
| Application and essential-workflow availability | 148 |

Counts are derived from findings.json. Every included issue links to its existing anthropics/claude-code report. Identified duplicate labels and several corrected, apparently fixed, or uncertain upstream-only cases encountered during screening were excluded. This does not establish complete deduplication by root cause. Follow-up comments were fetched and screened for 217 selected reports. No prevalence, comparative vendor-quality, financial-loss, or current-runtime conclusions follow from this convenience sample. The 27 resolved incidents are not added to the issue-report count.

## What this work is useful for

Its practical value is consolidation: finding related cases, retaining correction notes, and choosing candidates for careful investigation. Its novelty and evidential strength are limited: the underlying reports were already public, no runtime reproduction was performed, and root-cause independence remains unresolved. It should not be used to claim 346 confirmed defects, a vendor-wide failure rate, or 1,000 serious errors.

The most valuable next step is to reproduce a small set safely on the reported and current versions, group them by demonstrated root cause, and provide minimal reproductions or new evidence to the existing upstream issues.

## Method and validation

Public issue records supplied identifiers, dates, states and labels. Categories, selection and notes are editorial judgments rather than measured severity scores. Counts and overlap checks were calculated from records. Validation checked unique source URLs and numbering, source-identifier matches, prior-package exclusion, date ordering, duplicate/invalid labels, category totals, resolved-incident metadata, CSV row consistency and formula safety, and HTML source links and anchors. Those checks validate the compilation, not the alleged product behavior. Bulk collection was partial and stopped when later requests failed; this is not an exhaustive audit.

| Component | Origin | Limit |
|---|---|---|
| Issue state, labels and timestamps | Dynamic public-source snapshot | Can become stale |
| Category and review notes | Static editorial screening | Not a formal severity assessment |
| Counts and earlier-package overlap | Derived from records | Report counts are not unique defect counts |
| Incident status and impact | Vendor status archive | Historical and resolved |

## Corrections and reporting

The original source links retain attribution to their reporters. Please open an issue in this repository with a source-backed correction to this compilation. Product-specific follow-up belongs in the linked original issue; validated security vulnerabilities should follow [Anthropic's security policy](https://github.com/anthropics/claude-code/blob/main/SECURITY.md). Do not post credentials, private transcripts, personal account records or new undisclosed exploit details here. Third-party source material retains its original rights.
