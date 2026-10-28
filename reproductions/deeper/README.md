# Deeper controlled investigation: existing reports #72957 and #105138

Snapshot: 28 October 2026. Real released Windows Claude Code 2.1.312; local synthetic API/MCP inputs. Existing public reports retain attribution to their original reporters. This is follow-up evidence, not a claim of original discovery or a production exploit.

## Unicode rewriting: cross-tool and semantic impact

The corrected UTF-8 dummy MCP server received four of ten test arguments changed by the client. Six controls were preserved, including an actual non-ASCII character. The received codepoints matched the earlier Edit dispatch results, supporting a shared client input-normalization mechanism rather than an Edit-only file-writing error.

An Edit supplied this valid Python source:

    sample = r"x\u0041y"

The written source was:

    sample = r"xAy"

AST parsing and literal evaluation showed the intended eight-character value became a three-character value. Generated code was not executed. Adding an unrelated comment containing the synthetic Windows-path-shaped text Q:\fixture\dummy preserved the original escape text and eight-character value. An ordinary-string control was unchanged. Thus valid source can retain valid syntax while its test data changes, and unrelated surrounding text can affect the rewrite.

## MCP saved-result identity: defaults, branch selection and timing

MAX_MCP_OUTPUT_TOKENS was unset in all deeper MCP storage trials. The fixture's token-count API response is explicitly synthetic:

| Condition | Calls | Saved files | Wrong associations |
|---|---:|---:|---:|
| 60,000 filler characters, fixture token count 10 | 20 | 20 | 0 |
| 120,000 filler characters, fixture token count 10 | 20 | 20 | 0 |
| 600,000 filler characters, no token-count API invoked | 10 | 10 | 0 |
| 60,000 filler characters, controlled token count 30,000, burst | 20 | 16 | 4 |
| Same 30,000 count and payload, configured 30 ms reply spacing | 20 | 20 | 0 |

The first two trials used call-ID filenames. Their fixture count of 10 is not a valid estimate of production token counts, so those runs do not establish default production safety.

The larger fastpath run reached timestamp filenames with the default configured limit and no token-count API call, independently showing that default configuration can enter this path. It did not collide in that run.

The controlled over-limit token-count intervention selected the same timestamp path for shorter responses. Four of twenty calls then received another call's file; the matched spaced run preserved all twenty. This isolates path selection and timing without claiming a production failure rate. It does not turn the synthetic 30,000 count into a real token measurement.

Inspected release implementation: timestamp filenames omit tool-call identity, while an existing regular singly-linked file is accepted after exclusive-create failure without validating result identity. The winning file survives; losing calls may receive its path. This is not a demonstrated later-write overwrite.

## Reproduce

Use Windows and Python 3.13, with port 8000 free. Download the pinned official build using the parent folder's download_current.py, then run from this folder with the binary path adjusted as necessary. The local fixture uses a dummy API key; no account credentials or production model requests are needed.

    python unicode_extension.py --binary ../binaries/2.1.312/claude.exe --case mcp
    python unicode_extension.py --binary ../binaries/2.1.312/claude.exe --case semantics
    python mcp_controls.py --binary ../binaries/2.1.312/claude.exe --label example-burst --batch 20 --count 20 --payload-chars 60000 --default-threshold --burst-write --fixture-count-tokens 30000
    python mcp_controls.py --binary ../binaries/2.1.312/claude.exe --label example-spaced --batch 1 --count 20 --payload-chars 60000 --default-threshold --spacing-ms 30 --fixture-count-tokens 30000

Timing outcomes can vary. Record all runs, including those without collisions. The Unicode runner refuses to overwrite its existing run folders. Fixture messages and token-count signals are test inputs; received arguments, stored bytes and result-file associations are real-client measurements.

## Scope and disclosure

| Item | Origin |
|---|---|
| Tool inputs, canary tags, filler and token-count API responses | Static synthetic fixtures |
| Server-received values, source bytes and result associations | Dynamic measurements of the real released client |
| Version and integrity | Verified official package and executable hash |
| Root-cause mechanism | Runtime controls plus inspected embedded implementation |
| Security severity and production prevalence | Not established |

Two network-blocked attempts and an additional blocked comparison are excluded because they produced no usable product observations. An early MCP Unicode attempt used a legacy Python stdin encoding and is excluded because its non-ASCII control failed; explicit UTF-8 decoding corrected the fixture. Neither fixture errors nor missing responses are reported as product defects.

No new independent issue count is claimed. No cross-user disclosure, attacker capability, privilege escalation, permission bypass, financial loss or production prevalence was demonstrated. Please triage demonstrated client integrity failures separately from security impact.

Sources: https://github.com/anthropics/claude-code/issues/72957 and https://github.com/anthropics/claude-code/issues/105138. Official MCP limit documentation: https://code.claude.com/docs/en/mcp.

Evidence consistency checks: 46 passed. See results.json and validation.json.
