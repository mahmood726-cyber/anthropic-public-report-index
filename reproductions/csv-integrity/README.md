# Edit changes an unrelated CSV field during a one-word replacement

Controlled follow-up to https://github.com/anthropics/claude-code/issues/100983, not a claim of original discovery.

Claude Code 2.1.312 on Windows 11, official package integrity verified. Executable SHA-256: 6099672ebe5dcb518b67d1d32dde1e3360bc6bee1dae7f8d28a69c49acc7c865.

An authorized Edit replaces APPLE with ORANGE in one CSV row. An unrelated quoted note field also changes its embedded newline bytes. Python csv.reader using StringIO(newline='') confirms this changes the parsed field value, beyond a diff-formatting effect.

| Case | Unrelated note before | After | Result in each of two sessions |
|---|---|---|---|
| UTF-8 LF-majority mixed | alpha\r\nbeta | alpha\nbeta | changed |
| UTF-8 CRLF-majority mixed | alpha\nbeta | alpha\r\nbeta | changed |
| UTF-16LE BOM mixed | alpha\r\nbeta | alpha\nbeta | changed |
| UTF-8 BOM mixed | alpha\r\nbeta | alpha\nbeta | changed |
| Uniform UTF-8 LF | alpha\nbeta | unchanged | byte-exact requested replacement |
| Uniform UTF-8 CRLF | alpha\r\nbeta | unchanged | byte-exact requested replacement |

Each session completed all six cases, three API requests and twelve tool calls. Every Edit reported success without a newline-conversion warning. Across both sessions: eight mixed-format cases changed unrelated field contents; four uniform controls preserved all bytes except the requested word.

Minimal fixture bytes: b'key,value\nnote,"alpha\r\nbeta"\nfruit,APPLE\n'. Read it, then call Edit with old_string='APPLE', new_string='ORANGE'. Compare raw bytes and parse the untouched note value with newline translation disabled.

Reproduce with Python 3.13 on Windows:
1. Obtain the pinned official binary using ../download_current.py from the parent reproductions folder (or supply your verified 2.1.312 executable).
2. Run: python mixed_newline_controls.py --binary PATH_TO_VERIFIED_CLAUDE --label fresh-local-label
3. Inspect runs/fresh-local-label/csv_edits/mixed_results.json. Labels cannot overwrite existing evidence.

The real client receives predetermined synthetic API messages from 127.0.0.1:8000. No production model calls, credentials, private documents or generated code execution. Dummy CSV files only. The fixture authorizes only Read and Edit, with an isolated profile. Network permission must permit loopback.

Mechanism assessment: the release's Edit persistence path reads file contents plus a single line-ending classification, applies a replacement and writes the whole updated file through a helper that reconstructs CRLF globally for CRLF-classified content. This is consistent with both observed conversion directions; exact source-level remediation is for the vendor to validate. Byte normalization should preserve unedited spans or refuse mixed-format edits with a warning. No vendor patch or security severity is claimed.

| Item | Static input or measured result |
|---|---|
| CSV text, APPLE/ORANGE, encoding choices, API replies | Explicit synthetic test inputs |
| Actual disk bytes, parsed note values, tool success replies | Measured real-client outputs |
| Eight changed cases, four controls | Calculated from two completed sessions in results.json |
| Production frequency, exploitability | Not measured |

Other encoding checks safely refused CP1252/CP932 edits. Write was unavailable in the tested configuration, so failed Write attempts are excluded and do not establish the overwrite report. Research and report preparation were AI-assisted.
