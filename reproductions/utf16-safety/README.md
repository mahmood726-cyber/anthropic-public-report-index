# Edit silently drops an odd trailing UTF-16LE byte

Confirmed on Claude Code 2.1.312, Windows 11, using the official integrity-checked binary:
SHA-256 6099672ebe5dcb518b67d1d32dde1e3360bc6bee1dae7f8d28a69c49acc7c865.

Scope: a malformed UTF-16LE BOM file with an incomplete final code unit. This is a narrow file-safety defect, not evidence that ordinary well-formed UTF-16 files are corrupted, and not a demonstrated security exploit.

Create a dummy UTF-16LE BOM file containing note = "dummy" and fruit = "APPLE", then append one byte 0x41 or 0xFF. Read it and Edit only APPLE to ORANGE. The edit reports success but drops the unrelated trailing byte without a malformed-file warning.

Two isolated completed sessions each exercised six cases:
- Two malformed UTF-16LE files: requested word changed, odd trailing byte silently deleted.
- Valid UTF-16LE and UTF-8: exact expected bytes.
- UTF-8 with an invalid trailing byte and UTF-16BE: refused, original bytes unchanged.
Across both sessions: four affected malformed-file edits, four exact valid controls, four safe refusal controls. Each session had three loopback API requests and twelve tool calls. All before/after bytes and tool results are in results.json.

Root cause was localized in the exact binary: Hxt detects the UTF-16LE BOM and immediately returns the encoding, bypassing the validity checks used for UTF-8. COe then decodes the whole buffer with that encoding. The incomplete final byte disappears from the decoded string. Edit writes that decoded content after replacement and reports success; the output-size check verifies the newly encoded string, which no longer contains the lost byte. This is consistent with both trailing-byte probes and the refusal controls. Function byte offsets and SHA-256 hashes are included in results.json; no proprietary source is reproduced here.

Suggested correction: validate UTF-16LE structure before permitting edits, at least reject odd byte lengths, and leave malformed input untouched with a clear warning. A valid text encoding BOM is insufficient to establish that the entire file is valid.

Reproduce on Windows with Python 3.13:
1. Obtain the pinned official binary using ../download_current.py in the parent reproductions folder, or supply a separately verified executable.
2. Run: python utf16_controls.py --binary PATH_TO_VERIFIED_CLAUDE --label fresh-label
3. Inspect runs/fresh-label/malformed/utf16_results.json. Existing labels cannot be overwritten.

The real client consumes predetermined synthetic API replies from 127.0.0.1:8000, uses an isolated profile and only authorized Read/Edit tools. No production model calls, real API credentials, private files or generated source execution were involved.

| Item | Static input or measured output |
|---|---|
| Dummy text, trailing bytes, APPLE/ORANGE, API messages | Explicit synthetic test inputs |
| Disk bytes, tool success/refusal replies | Measured client outputs |
| Four affected cases and eight controls | Calculated from two completed sessions |
| Root-cause anchors | Measured offsets and hashes from verified release binary |
| Production frequency, exploitability, severity score | Not established |

Related broader encoding reports: #7134 and #96263. This report concerns malformed UTF-16LE, whose branch bypasses the current refusal guard; it does not claim that those older UTF-8 corruption scenarios remain reproducible.

Rejected candidates: current MCP error tests preserved all text diagnostics. Success-response preference for structuredContent is documented intentional behavior (maintainer explanation in anthropics/claude-code#9962), so it was not submitted as a new bug. Research and report preparation were AI-assisted.
