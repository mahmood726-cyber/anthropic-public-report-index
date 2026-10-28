# Controlled reproduction evidence

Two client behaviors associated with existing public reports were reproduced using a local fixture API and real released Claude Code binaries. Synthetic messages and canary data drive the tests; file bytes and client outputs are measurements. No production model calls are needed.

- #72957: Unicode escapes rewritten before Edit dispatch; measured on Windows 2.1.267 and 2.1.312.
- #105138: same-millisecond MCP persistence paths can substitute another call's result; observed in one of two burst trials on 2.1.312, with no collisions in the other burst or spaced control.
- #94314: inconclusive because the allowed Git Bash execution control failed.

See results.json for all trial summaries and version hashes. validation.json records 62 evidence checks. A human-readable HTML report is provided separately.

## Run

Windows and Python 3.13 are the tested environment. A local Claude Code binary is required; Git for Windows is required only for the permission probe. Port 8000 must be free. Test profiles and dummy files are created beneath this folder; no existing run folder is overwritten. Process trees are contained in a Windows Job Object and terminated when the test ends.

Download the isolated pinned official build, with package integrity verification:

    python download_current.py

Run Unicode controls:

    python unicode_controls.py --binary binaries/2.1.312/claude.exe --label your-unicode-run

Run a burst and a timing control:

    python mcp_controls.py --binary binaries/2.1.312/claude.exe --label your-burst --batch 10 --count 10
    python mcp_controls.py --binary binaries/2.1.312/claude.exe --label your-spaced --batch 1 --count 10 --spacing-ms 30

Timing collisions are not guaranteed on every burst. A collision-free run does not disprove the demonstrated shared-name mechanism. Capture all runs, including non-reproductions. Use a different label for each new run.

Optional harmless permission probe:

    python permission_controls.py --binary binaries/2.1.312/claude.exe --label your-permission-run

The test uses a dummy API key with a fixture API bound to 127.0.0.1:8000, isolated CLAUDE_CONFIG_DIR, bare mode, disabled nonessential traffic, and exact controlled tool messages. It does not call a real model or require account credentials. The Windows-path-shaped Unicode guard input is intentional synthetic text, not a filesystem target. Source files contain no global deletion commands or user-home paths.

No product fix, cross-platform prevalence, production incident impact, or remaining-catalogue validation is claimed. Anthropic binaries and copied proprietary implementation code are not distributed.

## Established client mechanisms

The Unicode case changes literal escape text such as x\u0041y into xAy after JSON parsing and before tool execution. The dispatched input already holds the changed value, and the resulting file equals that value. The inspected 2.1.312 binary has a recursive Unicode-repair pass called by its input normalizer, with escape and Windows-path guards matching the controls. This is client-side evidence; no real model supplied the input.

The MCP case uses filenames built from server name, tool name and millisecond time, without the tool-call ID. In the inspected release, an exclusive-create collision on a regular singly-linked file can return that existing path without checking result identity. In one burst, ten distinct canary results were mapped to three files and seven calls got another call's content. The second burst and the spaced control had ten files and no mismatches. This is timing-dependent substitution, not evidence that later writes overwrite earlier files.

Implementation anchors in results.json record binary offsets and window hashes so the inspected release can be checked without distributing proprietary implementation code. Observations include only fixture API messages and assistant/user tool events, with local root paths redacted. Full local logs are retained separately.

MCP test configuration: MAX_MCP_OUTPUT_TOKENS=100 forces the 2,010-character synthetic responses through the persistence path. The default size threshold was not tested. This qualifies the reproduction scope, not the demonstrated saved-file identity failure.
