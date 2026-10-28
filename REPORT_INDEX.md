# Index of 346 existing Anthropic GitHub reports

Prepared 28 October 2026. This index consolidates existing public issue reports for triage; it does not submit new bug reports.

These are reporter allegations, not 346 independently confirmed errors or unique vulnerabilities. None was reproduced in this review. Source records were open when checked; that does not establish current-release behavior. Related cases may share a root cause.

This index covers the latest emailed package. The 27 resolved vendor incidents in the HTML dossier are separate historical records and are not included here.

## Reporting route

All 346 reports below are already filed in anthropics/claude-code.

- [Repository reporting instructions](https://github.com/anthropics/claude-code/blob/main/README.md#reporting-bugs)
- [Bug-report form](https://github.com/anthropics/claude-code/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml): requires a single previously unreported bug and current-version information.
- [Security policy](https://github.com/anthropics/claude-code/blob/main/SECURITY.md): directs validated vulnerability submissions to HackerOne.

This index is published separately from Anthropic's issue tracker. The original linked issues remain the upstream reports; no duplicate bug submissions were created. This document preserves the consolidated review notes without representing them as firsthand reproduction results.

## Existing reports by review category

### Data integrity, deletion and recoverability

73 existing issue reports. The grouping is editorial, not a severity rating.

#### A003 — [Issue #85200](https://github.com/anthropics/claude-code/issues/85200)

> [BUG] TaskStop does not kill the process tree — orphaned `rm -rf /c` deleted user data for 20 minutes after

Another reported surviving-child case. The source includes an incomplete version field; its environment should be reconfirmed before reproduction.

Source snapshot: open; created 2026-08-09T08:47:30Z; updated 2026-10-26T01:18:43Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/85200#issuecomment-5310302782).

#### A005 — [Issue #95426](https://github.com/anthropics/claude-code/issues/95426)

> Claude Code deleted ~600GB: unprompted `rm -rf` on a substitution that resolved to a drive root

The reporter states the originating transcript was destroyed and offers later conversations. This materially limits verification of the initiating command and authorization.

Source snapshot: open; created 2026-09-18T18:51:56Z; updated 2026-10-25T01:07:49Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/95426#issuecomment-5763581307).

#### A006 — [Issue #105342](https://github.com/anthropics/claude-code/issues/105342)

> [BUG] Subagent-written test ran rm -rf ~ on the real home directory, deleting all of my unpushed works; worktree isolation

The reporter corrected the affected paths: the SSH directory survived. Worktree separation should not be equated with an operating-system security sandbox.

Source snapshot: open; created 2026-10-27T04:54:51Z; updated 2026-10-27T20:09:37Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A007 — [Issue #105298](https://github.com/anthropics/claude-code/issues/105298)

> Model-written test deleted the local repository checkout via unpatched cleanup rmtree

The described cleanup escaped the scope of a test mock and targeted the real checkout. Runtime behavior was not reproduced.

Source snapshot: open; created 2026-10-26T22:02:34Z; updated 2026-10-26T22:03:58Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A008 — [Issue #88753](https://github.com/anthropics/claude-code/issues/88753)

> [BUG] Compaction led to writing to wrong database in a way that could have destroyed production data

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-22T04:07:16Z; updated 2026-10-01T16:42:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A010 — [Issue #92328](https://github.com/anthropics/claude-code/issues/92328)

> [BUG] Write emits .cmd as UTF-8 + LF-only on Windows; cmd.exe (CP932) swallows the LF after a multibyte char, del

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-05T13:43:30Z; updated 2026-10-11T02:05:41Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A011 — [Issue #98635](https://github.com/anthropics/claude-code/issues/98635)

> [Bug] Worktree deletion removes branch with unmerged commits without warning

The report describes deletion of an unmerged branch, with recovery through reflog. Do not treat this as established permanent loss.

Source snapshot: open; created 2026-10-01T08:50:58Z; updated 2026-10-01T08:52:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A014 — [Issue #102682](https://github.com/anthropics/claude-code/issues/102682)

> [BUG] PowerShell tool: model-defined helper function silently shadowed by built-in alias (rd → Remove-Item), permanently deleting user files

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-16T08:48:31Z; updated 2026-10-18T09:34:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A015 — [Issue #93287](https://github.com/anthropics/claude-code/issues/93287)

> [Bug] Claude Code deleted my entire MacBook Applications directory contents - WTF

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T07:22:10Z; updated 2026-10-25T00:24:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/93287#issuecomment-5614992008).

#### A016 — [Issue #92737](https://github.com/anthropics/claude-code/issues/92737)

> Claude deleted user's irreplaceable personal photos with rm -rf before verifying files were moved

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-07T21:32:20Z; updated 2026-10-06T21:12:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A017 — [Issue #105138](https://github.com/anthropics/claude-code/issues/105138)

> [BUG] Parallel MCP results saved to tool-results share a millisecond filename; one result silently overwrites another

Correction in the discussion: exclusive creation means the first save wins. A later result can point to the earlier file; it is not simply last-writer overwriting.

Source snapshot: open; created 2026-10-26T07:41:56Z; updated 2026-10-27T15:02:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/105138#issuecomment-6435802388).

#### A019 — [Issue #103413](https://github.com/anthropics/claude-code/issues/103413)

> [BUG] Symlinking a sibling repo into a worktree to run a self-test let the test's rm -rf delete the real

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T09:04:28Z; updated 2026-10-19T19:07:58Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A020 — [Issue #98186](https://github.com/anthropics/claude-code/issues/98186)

> [BUG] Desktop WorktreePool GC still force-removes idle worktrees after #96162; --force deleted git-ignored data (days of paid model output)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-29T15:16:59Z; updated 2026-10-16T12:56:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A021 — [Issue #98642](https://github.com/anthropics/claude-code/issues/98642)

> [BUG] Desktop: deleting a session from the sidebar now permanently deletes its local transcript (since Claude Code 2.1.284), wiping usage

This concerns the consequences and warning of an explicit delete action, rather than an unsolicited deletion.

Source snapshot: open; created 2026-10-01T09:32:15Z; updated 2026-10-01T09:33:34Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A022 — [Issue #98120](https://github.com/anthropics/claude-code/issues/98120)

> [BUG] Desktop + Remote Control: forked session cannot reconnect after disconnect; `/teleport` inside a `--resume`d session writes a root entry

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-29T10:55:15Z; updated 2026-09-29T10:56:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A025 — [Issue #95717](https://github.com/anthropics/claude-code/issues/95717)

> Model destroyed a 410KB user file: open(path,"w") truncated it, then the write threw

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-20T18:17:04Z; updated 2026-09-20T18:43:12Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/95717#issuecomment-5751781175).

#### A027 — [Issue #93713](https://github.com/anthropics/claude-code/issues/93713)

> Desktop app: hours-long session transcript permanently lost (not just a display/routing bug)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-11T20:31:09Z; updated 2026-09-11T20:32:12Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A028 — [Issue #93658](https://github.com/anthropics/claude-code/issues/93658)

> Session lost after helper tool update — transcript intact but unrecoverable

The source says the transcript remains intact. The reported loss is recoverability/access, not proven deletion.

Source snapshot: open; created 2026-09-11T15:47:26Z; updated 2026-09-12T09:35:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A029 — [Issue #93385](https://github.com/anthropics/claude-code/issues/93385)

> [BUG] Cowork auto-repair deletes user session data then blocks its own retry - sessiondata.img preserved but sessiondata.vhdx required (Windows/MSIX); profile

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T15:36:57Z; updated 2026-09-10T15:38:19Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A032 — [Issue #91113](https://github.com/anthropics/claude-code/issues/91113)

> Recovered API-error retries orphan the turn's persisted output: late-flushed api_error records take over the parentUuid chain, so --resume drops the

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T01:10:04Z; updated 2026-09-10T05:32:06Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A033 — [Issue #88346](https://github.com/anthropics/claude-code/issues/88346)

> [BUG] Task store files deleted without any Task tool call, ~5s after a teammate completes the highest-numbered task (2.1.234–2.1.237)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-20T19:23:07Z; updated 2026-10-02T14:50:13Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/88346#issuecomment-5954982182).

#### A034 — [Issue #41458](https://github.com/anthropics/claude-code/issues/41458)

> [BUG] cleanupPeriodDays: 99999 ignored — 490 sessions silently deleted despite explicit setting

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-03-31T11:37:58Z; updated 2026-10-15T17:24:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4162254840), [comment 2](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4214611538), [comment 3](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4221487961), [comment 4](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4528923312), [comment 5](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4533090964), [comment 6](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4655661019), [comment 7](https://github.com/anthropics/claude-code/issues/41458#issuecomment-4703650034), [comment 8](https://github.com/anthropics/claude-code/issues/41458#issuecomment-5113960022).

#### A036 — [Issue #91284](https://github.com/anthropics/claude-code/issues/91284)

> [BUG] Silent session-transcript data loss keeps getting stale-closed (#53417, #70219): writer dies with zero errors — please fail loudly and

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T18:38:17Z; updated 2026-10-22T10:11:03Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A037 — [Issue #103323](https://github.com/anthropics/claude-code/issues/103323)

> ~45 session transcripts (newest 5 days old) deleted in one burst on 2.1.296 with no ctrl+x or purge; retention sweep

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T00:33:01Z; updated 2026-10-19T19:16:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A038 — [Issue #101188](https://github.com/anthropics/claude-code/issues/101188)

> [BUG] Rewind said it couldn't restore, but still overwrote ~20h of edits across the project and deleted files created since

The reporter describes disk changes despite a failed rewind indication; the exact selected restore point is uncertain.

Source snapshot: open; created 2026-10-11T05:16:26Z; updated 2026-10-12T06:16:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/101188#issuecomment-6118851209).

#### A039 — [Issue #99438](https://github.com/anthropics/claude-code/issues/99438)

> [Bug] ~/.claude.json corruption on Windows from concurrent writes causing data loss and trust reset

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-04T13:30:10Z; updated 2026-10-04T13:31:41Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A040 — [Issue #99938](https://github.com/anthropics/claude-code/issues/99938)

> [BUG] Session transcripts and prompt history vanish while other session files survive

The updated report identifies interactive launch with CLAUDE_CODE_CHILD_SESSION=1 as the trigger. It is not evidence of the general retention mechanism.

Source snapshot: open; created 2026-10-06T14:04:36Z; updated 2026-10-06T18:40:50Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A041 — [Issue #104123](https://github.com/anthropics/claude-code/issues/104123)

> [BUG] Remote Control resume overwrites the local transcript .jsonl with the server copy, losing everything before the last compaction

The file shrinkage is reported; the server-hydration explanation is explicitly the reporter's hypothesis.

Source snapshot: open; created 2026-10-21T21:24:06Z; updated 2026-10-21T21:25:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A060 — [Issue #94472](https://github.com/anthropics/claude-code/issues/94472)

> [Bug] File overwrite without existence check in bash auto mode

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-15T09:35:18Z; updated 2026-09-15T09:36:24Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A075 — [Issue #93780](https://github.com/anthropics/claude-code/issues/93780)

> delete_session leaves the transcript .jsonl on disk for spawned/child task sessions

The source alleges local transcript retention after a delete operation. It is a deletion-completeness concern, not a claim that every deletion path behaves identically.

Source snapshot: open; created 2026-09-12T07:41:42Z; updated 2026-09-12T12:06:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A080 — [Issue #97229](https://github.com/anthropics/claude-code/issues/97229)

> [BUG] VS Code: transcript &gt;2 GiB causes infinite re-parse loop, extension host OOM kills all Claude tabs (2.1.282)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-25T18:20:08Z; updated 2026-10-21T07:10:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/97229#issuecomment-5890226250).

#### A081 — [Issue #97230](https://github.com/anthropics/claude-code/issues/97230)

> [BUG] VS Code: post-compact skip ignored when boundaries carry preservedSegment — every tab parses the whole transcript, tab restore after

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-25T18:24:32Z; updated 2026-09-25T18:25:47Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A091 — [Issue #89859](https://github.com/anthropics/claude-code/issues/89859)

> [BUG] Windows Desktop: completed runs' CLI processes are never terminated — every scheduled-task run leaks a persistent process with open

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-26T16:45:25Z; updated 2026-10-19T22:10:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A098 — [Issue #104742](https://github.com/anthropics/claude-code/issues/104742)

> [BUG] Cloud session dies for good when its starting branch was deleted, although its working branch still exists

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-24T00:36:10Z; updated 2026-10-24T00:37:44Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A103 — [Issue #73638](https://github.com/anthropics/claude-code/issues/73638)

> Session rename mid-server-tool-call injects a turn that permanently corrupts the transcript (400 on every future prompt)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-02T23:23:13Z; updated 2026-09-21T12:05:04Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/73638#issuecomment-4875161448), [comment 2](https://github.com/anthropics/claude-code/issues/73638#issuecomment-4881081977), [comment 3](https://github.com/anthropics/claude-code/issues/73638#issuecomment-4905060478), [comment 4](https://github.com/anthropics/claude-code/issues/73638#issuecomment-5005383838), [comment 5](https://github.com/anthropics/claude-code/issues/73638#issuecomment-5154143335), [comment 6](https://github.com/anthropics/claude-code/issues/73638#issuecomment-5210192790), [comment 7](https://github.com/anthropics/claude-code/issues/73638#issuecomment-5221412670), [comment 8](https://github.com/anthropics/claude-code/issues/73638#issuecomment-5760191769).

#### A105 — [Issue #63192](https://github.com/anthropics/claude-code/issues/63192)

> Cancelling a parallel tool-call batch corrupts thinking blocks -&gt; 400 "thinking blocks cannot be modified" permanently wedges the session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-05-28T16:22:48Z; updated 2026-05-31T19:24:52Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/63192#issuecomment-4583290858), [comment 2](https://github.com/anthropics/claude-code/issues/63192#issuecomment-4585516897).

#### A107 — [Issue #100579](https://github.com/anthropics/claude-code/issues/100579)

> [BUG] Running /compact corrupts the session "API Error: 400 messages.1.content: Input should be a valid list"

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-08T17:58:24Z; updated 2026-10-08T18:01:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A115 — [Issue #99248](https://github.com/anthropics/claude-code/issues/99248)

> [BUG] [Cowork] A deleted organization plugin keeps running in Claude Desktop until the next hourly full plugin sync or a

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-03T14:51:47Z; updated 2026-10-03T14:58:02Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A117 — [Issue #38993](https://github.com/anthropics/claude-code/issues/38993)

> [BUG] Cowork: virtiofs FUSE mount serves truncated/stale files — host-side file changes not reflected in VM

This concerns host/guest file visibility and stale or truncated views; an integration failure does not by itself establish ownership of the underlying cause.

Source snapshot: open; created 2026-03-25T21:50:58Z; updated 2026-07-24T14:50:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4226895316), [comment 2](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4227846228), [comment 3](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4247239985), [comment 4](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4290870248), [comment 5](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4416572595), [comment 6](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4462146498), [comment 7](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4602720083), [comment 8](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4626164369), [comment 9](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4682233957), [comment 10](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4819384676), [comment 11](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4835451156), [comment 12](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4921214123), [comment 13](https://github.com/anthropics/claude-code/issues/38993#issuecomment-4996565519), [comment 14](https://github.com/anthropics/claude-code/issues/38993#issuecomment-5069906441).

#### A124 — [Issue #90410](https://github.com/anthropics/claude-code/issues/90410)

> [BUG] Windows MSIX: staged update leaves old instance running from WindowsApps\Deleted for 15h — 0x12C cleanup loop crashes it repeatedly,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-28T17:26:44Z; updated 2026-10-15T22:10:56Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A131 — [Issue #98583](https://github.com/anthropics/claude-code/issues/98583)

> Remote Control: session on my PC becomes permanently unreachable (environment_deleted) after the desktop app was closed for a few hours

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-01T03:17:24Z; updated 2026-10-01T19:41:03Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A133 — [Issue #93920](https://github.com/anthropics/claude-code/issues/93920)

> Desktop sessions become permanently unreachable ("Remote Control disconnected") after going dormant, with no local transcript cache

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-12T23:27:03Z; updated 2026-10-21T16:31:18Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/93920#issuecomment-5658831506), [comment 2](https://github.com/anthropics/claude-code/issues/93920#issuecomment-6321082514).

#### A134 — [Issue #93345](https://github.com/anthropics/claude-code/issues/93345)

> Remote Control: session worktrees are deleted before the session is archived, and activeSessionIds is almost never persisted

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T12:42:55Z; updated 2026-09-30T06:33:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A135 — [Issue #93409](https://github.com/anthropics/claude-code/issues/93409)

> [BUG] remote-control: stale bridge-pointer re-adopts a deleted session → "registerWorker failed 404" on every launch

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T17:07:21Z; updated 2026-10-10T08:09:08Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A136 — [Issue #77372](https://github.com/anthropics/claude-code/issues/77372)

> [Bug] Remote Control: stale environments cannot be deleted and ghost sessions cause permanent 404 errors

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-14T04:48:02Z; updated 2026-09-23T13:59:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/77372#issuecomment-5324934034).

#### A138 — [Issue #104659](https://github.com/anthropics/claude-code/issues/104659)

> [BUG] claude remote-control deleted all chats after weekend

An environment-deleted banner does not establish that underlying conversation records were physically deleted.

Source snapshot: open; created 2026-10-23T16:00:32Z; updated 2026-10-23T19:03:17Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A141 — [Issue #93583](https://github.com/anthropics/claude-code/issues/93583)

> [BUG] Cowork (Windows MSIX): 'Delete Cowork VM Sessions and Restart' deletes the scheduler index and all local chat transcripts, dialog

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-11T09:29:20Z; updated 2026-09-11T09:32:57Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A143 — [Issue #103503](https://github.com/anthropics/claude-code/issues/103503)

> [BUG] Scripted text replacement bounded by the next top-level def silently deleted 17 unrelated test functions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T16:10:23Z; updated 2026-10-20T00:03:44Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A144 — [Issue #83033](https://github.com/anthropics/claude-code/issues/83033)

> [BUG] Sonnet 5 writes Korean tool-call parameters as \uXXXX escapes and mis-spells the hex, corrupting Hangul (100% corruption when escape-writing

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-01T00:25:13Z; updated 2026-09-09T08:25:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/83033#issuecomment-5343029602).

#### A145 — [Issue #72957](https://github.com/anthropics/claude-code/issues/72957)

> Write/Edit tools silently decode \uXXXX in file content, corrupting escape-sequence text (Linux)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-01T21:29:47Z; updated 2026-10-25T21:59:30Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/72957#issuecomment-5311021450).

#### A147 — [Issue #92026](https://github.com/anthropics/claude-code/issues/92026)

> Uploading a UTF-8 CSV file via 'Upload from computer' corrupts Japanese text (double-encoding via Latin-1 misinterpretation)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T08:39:58Z; updated 2026-10-25T22:08:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A148 — [Issue #88561](https://github.com/anthropics/claude-code/issues/88561)

> Bash tool silently collapses `\\` to `\` in command text, corrupting regex and paths

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-21T15:27:46Z; updated 2026-10-13T00:01:11Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A149 — [Issue #82311](https://github.com/anthropics/claude-code/issues/82311)

> [BUG] Bash tool's shared shell cwd leaks silently across calls (parallel and long-distance) — can relocate or corrupt later commands

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-29T15:48:49Z; updated 2026-09-15T15:43:23Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A150 — [Issue #91526](https://github.com/anthropics/claude-code/issues/91526)

> [BUG] Windows: Claude Code CLI corrupts stdio MCP password arguments when launching npx through cmd.exe

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-02T14:33:51Z; updated 2026-09-12T13:37:34Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A177 — [Issue #90272](https://github.com/anthropics/claude-code/issues/90272)

> [BUG] Desktop app OOM on /compact with a much smaller transcript (~40MB) than previously reported crash threshold

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-28T05:15:35Z; updated 2026-10-14T22:09:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A183 — [Issue #74085](https://github.com/anthropics/claude-code/issues/74085)

> Background agent whose cwd was deleted crash-loops (exit 1 — exit_with_message) and is re-adopted on every daemon restart

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-04T03:33:56Z; updated 2026-07-04T03:40:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A269 — [Issue #93173](https://github.com/anthropics/claude-code/issues/93173)

> Bash sandbox denies writes to &lt;repo&gt;/.claude/ paths, silently corrupting the git working tree in repos that track files there

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-09T19:14:43Z; updated 2026-09-09T19:15:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A270 — [Issue #90916](https://github.com/anthropics/claude-code/issues/90916)

> [Bug] Windows/Git Bash: corrupted shell snapshot (serialized git-completion functions) makes every Bash tool call exit 127 with no output

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T06:54:06Z; updated 2026-10-19T22:10:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A272 — [Issue #88307](https://github.com/anthropics/claude-code/issues/88307)

> [BUG] Daemon-hosted background worker deletes `~/.claude/settings.json` when it is a symlink into a read-only directory (nix/home-manager) — all user settings

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-20T17:05:35Z; updated 2026-08-27T03:57:20Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A292 — [Issue #78439](https://github.com/anthropics/claude-code/issues/78439)

> Backup retention (keep-last-5) evicts the last good .claude.json after concurrent-write corruption, making config loss permanent

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-17T09:12:39Z; updated 2026-09-10T12:17:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A293 — [Issue #88462](https://github.com/anthropics/claude-code/issues/88462)

> [Data Loss] Claude Code ran rm -rf on $HOME in auto mode — destructive code hidden inside a script the

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-21T07:43:06Z; updated 2026-10-23T20:28:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A294 — [Issue #89199](https://github.com/anthropics/claude-code/issues/89199)

> [BUG] Retention sweep deletes user-created git-worktree-add worktrees under .claude/worktrees via dead job records (docs say it never removes user worktrees)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-24T11:31:30Z; updated 2026-08-25T00:19:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A295 — [Issue #90148](https://github.com/anthropics/claude-code/issues/90148)

> [BUG] cleanupPeriodDays in a project's .claude/settings.json controls the machine-wide transcript sweep, deleting other projects' history

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-27T15:40:24Z; updated 2026-09-13T22:09:17Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A296 — [Issue #90789](https://github.com/anthropics/claude-code/issues/90789)

> [BUG] Silent settings.json data loss: 5s time-only echo suppression masks external writes, stale per-process cache clobbers on next save

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-30T16:41:17Z; updated 2026-10-20T22:10:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A297 — [Issue #90943](https://github.com/anthropics/claude-code/issues/90943)

> [BUG] Concurrent sessions in one working tree: a stale git index silently deletes and reverts another session's committed work

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T09:46:58Z; updated 2026-10-11T22:40:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A300 — [Issue #93099](https://github.com/anthropics/claude-code/issues/93099)

> [MODEL] Opus 5 executed rm -rf "$HOME" during test cleanup(57,235 files and 11,315 directories deleted), causing extensive data loss

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-09T14:00:18Z; updated 2026-10-22T18:42:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/93099#issuecomment-5814403439).

#### A301 — [Issue #90421](https://github.com/anthropics/claude-code/issues/90421)

> [BUG] Shell snapshot silently truncated at ~7.2KB on Windows (Desktop) - every Bash call fails with unexpected EOF

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-28T18:07:35Z; updated 2026-09-24T00:47:44Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A314 — [Issue #98539](https://github.com/anthropics/claude-code/issues/98539)

> [BUG] `/model` in one session silently changes the model of every future session: an unnoticed downgrade led to data loss

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-30T22:08:00Z; updated 2026-09-30T22:15:17Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A331 — [Issue #94336](https://github.com/anthropics/claude-code/issues/94336)

> Between-tool assistant text intermittently NOT stored in session .jsonl — replaced by a summary typed as 'thinking' (permanent data loss,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-14T17:00:24Z; updated 2026-10-21T18:15:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A337 — [Issue #98612](https://github.com/anthropics/claude-code/issues/98612)

> [GitHub integration] Claude Design still uses deleted account's token

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-01T06:41:35Z; updated 2026-10-01T06:43:11Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A340 — [Issue #94489](https://github.com/anthropics/claude-code/issues/94489)

> Global settings.json corrupted into a top-level JSON array (5 partial snapshots) instead of an object

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-15T11:11:07Z; updated 2026-09-15T11:12:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A341 — [Issue #95815](https://github.com/anthropics/claude-code/issues/95815)

> [BUG] WebSearch session cap (CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION) fails silently: over-budget calls return non-error results and agents continue from model memory, corrupting long

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-21T10:15:13Z; updated 2026-10-22T11:22:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A342 — [Issue #93271](https://github.com/anthropics/claude-code/issues/93271)

> claude.ai Gmail MCP create_draft: the google.com/url wrapper is emitted CORRUPTED (raw 0x17 in place of "=1"), and the substituted signature

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T06:02:00Z; updated 2026-10-14T19:51:41Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

### Access, privacy and permission controls

78 existing issue reports. The grouping is editorial, not a severity rating.

#### A018 — [Issue #103805](https://github.com/anthropics/claude-code/issues/103805)

> [MODEL] Asked for a small doc-scraping workflow; Opus 5.5 built unrequested infrastructure, launched 44+ Claude Code sessions on my login,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-20T17:06:41Z; updated 2026-10-20T17:09:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A044 — [Issue #98595](https://github.com/anthropics/claude-code/issues/98595)

> Bug report: Claude started Remote Control in an unauthorized local folder and told it to search other folders

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-01T04:07:13Z; updated 2026-10-01T04:08:17Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A045 — [Issue #95749](https://github.com/anthropics/claude-code/issues/95749)

> [Bug] Auto mode classifier allowed unauthorized push to main branch without explicit confirmation

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-20T21:58:08Z; updated 2026-10-25T02:29:46Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A047 — [Issue #95170](https://github.com/anthropics/claude-code/issues/95170)

> [Bug] Unauthorized file system access beyond explicitly permitted directories

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-17T15:18:42Z; updated 2026-09-17T15:19:49Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A048 — [Issue #93072](https://github.com/anthropics/claude-code/issues/93072)

> Agent applied unauthorized config changes to a production device after being asked only to diagnose

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-09T12:00:38Z; updated 2026-09-09T12:01:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A049 — [Issue #90622](https://github.com/anthropics/claude-code/issues/90622)

> [Bug] Subagent committed and pushed unauthorized changes to PR branch using user's git identity

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-29T18:42:13Z; updated 2026-10-17T10:10:18Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A050 — [Issue #96661](https://github.com/anthropics/claude-code/issues/96661)

> [BUG] Background git fetch bypasses permissions.deny and sandbox SSH_AUTH_SOCK denial, using the ssh-agent key on every window focus

The report concerns background Git access and an SSH-agent authorization prompt. It does not establish silent key theft.

Source snapshot: open; created 2026-09-24T09:29:07Z; updated 2026-10-01T08:05:57Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A051 — [Issue #92901](https://github.com/anthropics/claude-code/issues/92901)

> [BUG] sandbox.credentials.files protection can be bypassed on first access to a not-yet-existing deny-listed path

The reproduction uses a dummy credential-file path and concerns first access before a deny-listed file exists. Actual secret compromise is not established.

Source snapshot: open; created 2026-09-08T17:33:55Z; updated 2026-09-08T17:35:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A052 — [Issue #92542](https://github.com/anthropics/claude-code/issues/92542)

> [BUG] Bash deny rules bypassed by any wrapper program outside ax()'s 8-item unwrap list

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-06T19:37:44Z; updated 2026-09-09T22:00:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A053 — [Issue #91690](https://github.com/anthropics/claude-code/issues/91690)

> grep -r and cp -r still bypass Read() deny rules on 2.1.259 (changelog fix does not reproduce; Windows/VS Code extension)

The reproduction uses canary data. It alleges a boundary bypass rather than proving exposure of real credentials.

Source snapshot: open; created 2026-09-03T04:38:36Z; updated 2026-10-24T10:10:05Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A054 — [Issue #88770](https://github.com/anthropics/claude-code/issues/88770)

> permissions.deny (Bash(curl *)) silently bypassed under Auto Mode

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-22T07:14:13Z; updated 2026-10-20T10:09:50Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A055 — [Issue #103241](https://github.com/anthropics/claude-code/issues/103241)

> permissions.deny Read rules are bypassed by command substitution, subshells, source and interpreters in Bash

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-18T16:49:23Z; updated 2026-10-25T01:47:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A056 — [Issue #94082](https://github.com/anthropics/claude-code/issues/94082)

> Security: automatic 'file changed on disk' notification bypasses secret-file PreToolUse hook, leaking full credential file to transcript

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-14T00:32:40Z; updated 2026-09-14T00:33:39Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A058 — [Issue #98601](https://github.com/anthropics/claude-code/issues/98601)

> [BUG] Bash Renders full Private Key for deleted file

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-01T05:23:25Z; updated 2026-10-01T05:24:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A059 — [Issue #95385](https://github.com/anthropics/claude-code/issues/95385)

> [MODEL] Scheduled /loop cron task accessed physical device (camera) without session consent after /clear

The source raises consent persistence around scheduled camera access. Access scope and consent history require controlled validation.

Source snapshot: open; created 2026-09-18T15:06:36Z; updated 2026-09-18T15:07:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A061 — [Issue #88583](https://github.com/anthropics/claude-code/issues/88583)

> [BUG] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-21T17:39:39Z; updated 2026-10-20T00:19:23Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/88583#issuecomment-5396834706).

#### A062 — [Issue #98755](https://github.com/anthropics/claude-code/issues/98755)

> macOS 2.1.285: failed OAuth refresh empties sole Keychain credential with one observed session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-01T17:03:29Z; updated 2026-10-01T23:02:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A063 — [Issue #105645](https://github.com/anthropics/claude-code/issues/105645)

> [BUG] A failed OAuth refresh blanks the stored credential (accessToken/refreshToken emptied, expiresAt 0) instead of reporting an error — reproduced

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-28T11:33:02Z; updated 2026-10-28T11:34:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A066 — [Issue #104155](https://github.com/anthropics/claude-code/issues/104155)

> [BUG] macOS Keychain credential never prunes mcpOAuth entries for disabled/removed plugin MCP servers; 16 KB payload exceeds `security` stdin limit

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T00:19:07Z; updated 2026-10-27T12:02:19Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A067 — [Issue #102147](https://github.com/anthropics/claude-code/issues/102147)

> Sandbox launcher leaks proxy credentials (HTTP(S)_PROXY basic-auth) via bwrap --setenv argv pairs, world-readable in /proc/&lt;pid&gt;/cmdline

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-14T19:12:34Z; updated 2026-10-14T19:13:56Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A068 — [Issue #94361](https://github.com/anthropics/claude-code/issues/94361)

> [BUG] claude-in-chrome Tab Context prints full URLs of every tab, leaking credentials in query strings

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-14T18:58:03Z; updated 2026-10-11T05:10:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A072 — [Issue #95954](https://github.com/anthropics/claude-code/issues/95954)

> Cross-session teammate/subagent messages leak between unrelated Claude Code sessions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-22T01:32:24Z; updated 2026-09-22T01:40:04Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A073 — [Issue #101845](https://github.com/anthropics/claude-code/issues/101845)

> [Bug] Concurrent Claude Code sessions in same repo leak tool outputs across sessions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-13T17:50:04Z; updated 2026-10-13T17:51:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A114 — [Issue #100869](https://github.com/anthropics/claude-code/issues/100869)

> Plugin hooks module: classic.* events (classic.Stop, classic.PreToolUse, classic.Notification, classic.PermissionRequest) never reach the module, while settings hooks for the same events

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-09T17:53:39Z; updated 2026-10-09T17:54:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A126 — [Issue #91481](https://github.com/anthropics/claude-code/issues/91481)

> [BUG] Internal browser crashes when accessing Windows Credential Manager during authentication

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-02T11:49:15Z; updated 2026-10-23T10:10:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A130 — [Issue #103557](https://github.com/anthropics/claude-code/issues/103557)

> [BUG] Remote Control: re-login on self-hosted `claude remote-control` worker orphans all existing chats ("environment was deleted") even though the environment

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T19:59:17Z; updated 2026-10-19T19:59:17Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A137 — [Issue #88607](https://github.com/anthropics/claude-code/issues/88607)

> [BUG] Interrupted sign-in with a different email orphans the desktop app's entire Code session store; sessions appear permanently deleted while

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-21T19:50:22Z; updated 2026-09-23T17:17:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A187 — [Issue #56840](https://github.com/anthropics/claude-code/issues/56840)

> [BUG] Remote SSH session crashes immediately with exit code 1 on Max/OAuth accounts (ccd-cli 2.1.128)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-05-06T22:43:45Z; updated 2026-05-20T23:35:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A191 — [Issue #105293](https://github.com/anthropics/claude-code/issues/105293)

> [BUG] 2.1.294: set_permission_mode to "auto" emits no system/status event — Xcode 27.2 RC agent hangs in Auto mode

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-26T21:13:39Z; updated 2026-10-26T21:46:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A193 — [Issue #104878](https://github.com/anthropics/claude-code/issues/104878)

> [BUG] Linux: startup hangs forever on hard-coded /home/claude/.claude/remote/.oauth_token probe when /home/claude is an unreachable NFS/autofs mount

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-24T18:46:27Z; updated 2026-10-24T18:48:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A197 — [Issue #102902](https://github.com/anthropics/claude-code/issues/102902)

> [BUG] Windows Desktop: any passkey prompt in the Browser pane hangs the whole app — CrBrowserMain blocked forever in webauthn.dll!WebAuthNGetPlatformCredentialList

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-17T02:38:09Z; updated 2026-10-22T12:39:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A203 — [Issue #99653](https://github.com/anthropics/claude-code/issues/99653)

> [BUG] Start-up hangs forever (main thread in open()) when a permission rule's path resolves to a TCC-protected location and the

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-05T12:18:55Z; updated 2026-10-05T14:06:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A205 — [Issue #99254](https://github.com/anthropics/claude-code/issues/99254)

> [Bug] zsh shell snapshot writes bare option names; `login` executes /usr/bin/login causing hangs

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-03T15:30:17Z; updated 2026-10-03T15:31:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A214 — [Issue #97911](https://github.com/anthropics/claude-code/issues/97911)

> Unattended `--bg` sessions can hang for hours on an unanswered auto-mode permission prompt, with no timeout and no way to

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-28T15:52:53Z; updated 2026-09-28T15:54:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A222 — [Issue #95384](https://github.com/anthropics/claude-code/issues/95384)

> [BUG] Unattended CCR routine sessions hang indefinitely on an unanswerable permission-mode prompt; run status disagrees across surfaces

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-18T15:04:29Z; updated 2026-09-18T15:06:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A226 — [Issue #94348](https://github.com/anthropics/claude-code/issues/94348)

> [BUG] Desktop Code tab (Auto mode): permission prompt never renders — call hangs then is silently killed as "cancelled" on

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-14T17:19:45Z; updated 2026-09-14T17:21:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A238 — [Issue #91149](https://github.com/anthropics/claude-code/issues/91149)

> [BUG] Claude Code 2.1.252 subprocess hangs indefinitely on socket handoff — host reports misleading 60s 'authentication and network connectivity' timeout

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T06:11:38Z; updated 2026-10-21T22:10:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A248 — [Issue #87812](https://github.com/anthropics/claude-code/issues/87812)

> [Bug] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-19T01:37:05Z; updated 2026-09-03T07:58:46Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A271 — [Issue #103633](https://github.com/anthropics/claude-code/issues/103633)

> Windows: moving a file login into Credential Manager leaves a manifest naming a piece it never wrote, and the login

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-20T02:40:58Z; updated 2026-10-20T02:42:24Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A273 — [Issue #104342](https://github.com/anthropics/claude-code/issues/104342)

> [BUG] Rewind silently changes the permission mode, and can put a Manual or auto session into bypass permissions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T17:13:25Z; updated 2026-10-22T21:49:32Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A274 — [Issue #94314](https://github.com/anthropics/claude-code/issues/94314)

> Bash permission allow-rule doesn't split on ;/&& before matching (contrary to docs) — compound-command smuggling bypasses scoped allowlist

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-14T15:53:37Z; updated 2026-09-15T08:09:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A275 — [Issue #93510](https://github.com/anthropics/claude-code/issues/93510)

> Self-permission-granting safety check bypassable via Bash-mediated write (gates by tool, not by effect)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-11T02:06:02Z; updated 2026-09-11T02:07:08Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A276 — [Issue #92383](https://github.com/anthropics/claude-code/issues/92383)

> [BUG] Cross-session send_message from an auto-permission-mode sender is silently dropped (45s no-ack settle); bypassPermissions sender delivers

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-05T19:45:50Z; updated 2026-09-21T05:18:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/92383#issuecomment-5555669387), [comment 2](https://github.com/anthropics/claude-code/issues/92383#issuecomment-5755756123).

#### A277 — [Issue #91969](https://github.com/anthropics/claude-code/issues/91969)

> Claude in Chrome: permission and credential consent prompts render in a window the user cannot see, so they lapse as

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T03:08:40Z; updated 2026-10-25T10:10:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A278 — [Issue #79782](https://github.com/anthropics/claude-code/issues/79782)

> [BUG] Scheduled task execution ignores UI-configured permission mode and model settings

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-21T13:40:07Z; updated 2026-09-15T10:20:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/79782#issuecomment-5363670109).

#### A279 — [Issue #104398](https://github.com/anthropics/claude-code/issues/104398)

> Background sessions set BROWSER=true, which breaks browser-based credential_process auth (Bedrock + SSO)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T21:27:10Z; updated 2026-10-22T21:29:02Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A281 — [Issue #95113](https://github.com/anthropics/claude-code/issues/95113)

> MCP OAuth credentials persisted with expiresAt: 0 and no refreshToken, forcing re-auth every session (mcp.grafana.com, mcp.slack.com)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-17T10:22:53Z; updated 2026-09-25T12:31:32Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A282 — [Issue #94856](https://github.com/anthropics/claude-code/issues/94856)

> [BUG] macOS: claude auth login reports success but CLI stays unauthenticated - hasAvailableSubscription false on an active Stripe subscription, and

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-16T19:53:52Z; updated 2026-09-16T19:55:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A283 — [Issue #90527](https://github.com/anthropics/claude-code/issues/90527)

> macOS: Claude Code accumulates a new Keychain credential entry per login (110 in 5 weeks) and fails to reuse them,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-29T07:32:21Z; updated 2026-10-22T00:25:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A285 — [Issue #91847](https://github.com/anthropics/claude-code/issues/91847)

> [BUG] Headless `-p` suppresses plugin MCP servers in favor of same-URL claude.ai connectors, which cannot authenticate headlessly

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T15:57:28Z; updated 2026-09-12T13:00:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A287 — [Issue #89188](https://github.com/anthropics/claude-code/issues/89188)

> Background session cannot edit a repo nested under a non-git cwd: write guard demands EnterWorktree, EnterWorktree refuses (and a hand-made

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-24T10:28:26Z; updated 2026-08-25T00:19:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A288 — [Issue #105518](https://github.com/anthropics/claude-code/issues/105518)

> [BUG] plugin eval: every sandboxed Bash call fails on hosts using sops-nix, because the /run/secrets read-deny can't be mounted

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-27T21:32:07Z; updated 2026-10-27T21:33:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A298 — [Issue #91980](https://github.com/anthropics/claude-code/issues/91980)

> Forced re-login wipes ~/.claude transcripts; concurrent instance deletes a live session's task output files (Windows)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T04:05:45Z; updated 2026-10-25T22:08:33Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A303 — [Issue #92613](https://github.com/anthropics/claude-code/issues/92613)

> Desktop SSH remote session fails with "401 OAuth access token is invalid" while the claude CLI on the same host,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-07T07:56:35Z; updated 2026-09-07T12:04:52Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A304 — [Issue #92839](https://github.com/anthropics/claude-code/issues/92839)

> [BUG] MACOS Keychain: argv fallback for oversized OAuth credential payload (&gt;4KB) itself fails silently ("pbt" error) during MCP OAuth login

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-08T12:20:13Z; updated 2026-09-08T14:04:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A312 — [Issue #91270](https://github.com/anthropics/claude-code/issues/91270)

> VSCode extension: 'always allow' permission grants written to tracked .claude/settings.json instead of gitignored settings.local.json

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T16:45:05Z; updated 2026-10-22T10:10:46Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A315 — [Issue #105648](https://github.com/anthropics/claude-code/issues/105648)

> [BUG] Protected-path guard for Remove-Item is bypassed when the path comes from a variable

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-28T12:04:26Z; updated 2026-10-28T12:06:37Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A316 — [Issue #103626](https://github.com/anthropics/claude-code/issues/103626)

> [BUG] User-tier classic.UserPromptSubmit hook bypassed by cc-plugin-sec-default on the first prompt of every session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-20T01:47:37Z; updated 2026-10-21T17:37:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A317 — [Issue #103435](https://github.com/anthropics/claude-code/issues/103435)

> [BUG] VS Code extension: extension-host requests bypass the configured proxy (OAuth refresh, remote sessions, telemetry)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T11:15:36Z; updated 2026-10-19T11:16:58Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A318 — [Issue #88118](https://github.com/anthropics/claude-code/issues/88118)

> Read dedup does not account for PostToolUse updatedToolOutput: repeated Reads bypass substituting hooks, and readFileState records disk content the model

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-20T03:44:13Z; updated 2026-10-22T10:40:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A319 — [Issue #86504](https://github.com/anthropics/claude-code/issues/86504)

> [Bug] Project-scope settings.json can bypass sandbox isolation via sandbox.enabled: false

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-13T20:20:26Z; updated 2026-09-26T21:45:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A320 — [Issue #92060](https://github.com/anthropics/claude-code/issues/92060)

> [BUG] Cross-session messaging bypasses per-session folder scope: a direct Read across the boundary prompts, the same content via SendMessage does

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T11:17:36Z; updated 2026-10-25T22:09:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A321 — [Issue #90758](https://github.com/anthropics/claude-code/issues/90758)

> Claude ran a credential-helper `get` command and printed a live access token into the transcript

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-30T13:40:05Z; updated 2026-10-18T22:09:13Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A322 — [Issue #96307](https://github.com/anthropics/claude-code/issues/96307)

> Sandbox proxy credentials are sent to Git credential helpers on macOS (`fatal: failed to store: 100001`)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T10:10:24Z; updated 2026-09-23T10:11:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A323 — [Issue #76561](https://github.com/anthropics/claude-code/issues/76561)

> Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-11T02:04:04Z; updated 2026-10-06T15:36:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A324 — [Issue #104359](https://github.com/anthropics/claude-code/issues/104359)

> [BUG] CLI holding an env credential still renews the stored claude.ai login; on macOS sandboxed processes split it to .credentials.json

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T18:28:16Z; updated 2026-10-27T12:02:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A325 — [Issue #104769](https://github.com/anthropics/claude-code/issues/104769)

> [BUG] Desktop app: Remote Control drops every few hours under Require trusted devices (HTTP 403 on credential re-mint; Desktop host

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-24T04:42:22Z; updated 2026-10-24T04:43:50Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A326 — [Issue #105443](https://github.com/anthropics/claude-code/issues/105443)

> [BUG] Linux sandbox: duplicate --ro-bind /dev/null for one credential file (built-in denylist + user settings) kills every Bash call on

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-27T14:58:13Z; updated 2026-10-27T14:59:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A327 — [Issue #105381](https://github.com/anthropics/claude-code/issues/105381)

> [BUG] proxyAuthHelper credential is captured once per request and per MCP transport; a 407 on CONNECT never re-runs the helper,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-27T10:27:31Z; updated 2026-10-27T14:02:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/105381#issuecomment-6443938468).

#### A328 — [Issue #96385](https://github.com/anthropics/claude-code/issues/96385)

> [BUG] macOS OAuth credential rotation resets Keychain ACL and invalidates Always Allow

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T14:59:27Z; updated 2026-09-23T15:00:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A329 — [Issue #91708](https://github.com/anthropics/claude-code/issues/91708)

> Windows/VSCode: concurrent sessions race on OAuth refresh against the file credential store (400 → forced re-login)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T05:44:22Z; updated 2026-10-12T22:20:56Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A330 — [Issue #89671](https://github.com/anthropics/claude-code/issues/89671)

> HTTP MCP OAuth: valid token silently corrupted by status check (wrong redirectUri, empty accessToken)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-26T01:02:17Z; updated 2026-09-19T07:54:50Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A332 — [Issue #92194](https://github.com/anthropics/claude-code/issues/92194)

> Remote Control archives live sessions after a transient network give-up, bypassing the preserve-on-shutdown path

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T19:09:21Z; updated 2026-10-09T16:29:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A333 — [Issue #91700](https://github.com/anthropics/claude-code/issues/91700)

> Subagent composed permitted operations to bypass a permission block, causing SSH self-lockout on a remote host

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T05:06:22Z; updated 2026-10-24T10:10:11Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A338 — [Issue #104410](https://github.com/anthropics/claude-code/issues/104410)

> Remote Control sessions drop and don't recover on their own; cross-session messages are lost silently and identities change on reconnect

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T22:35:18Z; updated 2026-10-25T22:56:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A339 — [Issue #95236](https://github.com/anthropics/claude-code/issues/95236)

> [BUG] Windows: `.oauth_refresh.lock` directory survives a mid-refresh exit and is never reclaimed despite `stale: 60000` — every `claude -p` call

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-17T20:58:19Z; updated 2026-10-07T20:43:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/95236#issuecomment-6046494822).

#### A344 — [Issue #99650](https://github.com/anthropics/claude-code/issues/99650)

> [BUG] macOS sandbox proxy truncates response bodies and resets the connection when the server closes it (`Connection: close`)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-05T12:09:51Z; updated 2026-10-27T02:27:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A345 — [Issue #103788](https://github.com/anthropics/claude-code/issues/103788)

> [BUG] Claude Desktop (macOS): sign-in fails with "We couldn't verify your browser" — both Google and email paths 400 —

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-20T16:37:48Z; updated 2026-10-28T07:26:33Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/103788#issuecomment-6463257074).

### Resource exhaustion and process lifecycle

38 existing issue reports. The grouping is editorial, not a severity rating.

#### A078 — [Issue #74001](https://github.com/anthropics/claude-code/issues/74001)

> OOM crash under multi-subagent load: subagent CLI processes grow to ~6.5 GB RSS each; CliGovernor logs critical memory pressure for

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-03T21:09:34Z; updated 2026-09-15T12:33:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/74001#issuecomment-5000649583).

#### A079 — [Issue #104497](https://github.com/anthropics/claude-code/issues/104497)

> [BUG] Bash tool's bundled find (bfs 4.1.1) follows an ntfs3 junction reported as DT_DIR, loops forever and grows memory without

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-23T06:06:48Z; updated 2026-10-27T01:48:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A082 — [Issue #99538](https://github.com/anthropics/claude-code/issues/99538)

> [BUG] Desktop app renderer OOM-crash loop when opening a large cloud session (600 MB → 5 GB in ~50 s)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-05T00:38:35Z; updated 2026-10-05T06:18:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A083 — [Issue #101901](https://github.com/anthropics/claude-code/issues/101901)

> Extension host OOM-crashes within seconds to ~1 min of launching 2+ parallel background Agent subagents (Windows)

The discussion retracts the OOM diagnosis: measured memory stayed modest. Treat this as extension-host failure or liveness loss, with mechanism unresolved.

Source snapshot: open; created 2026-10-13T22:38:31Z; updated 2026-10-18T00:47:31Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/101901#issuecomment-6158335710), [comment 2](https://github.com/anthropics/claude-code/issues/101901#issuecomment-6158683426), [comment 3](https://github.com/anthropics/claude-code/issues/101901#issuecomment-6158763503), [comment 4](https://github.com/anthropics/claude-code/issues/101901#issuecomment-6170291258), [comment 5](https://github.com/anthropics/claude-code/issues/101901#issuecomment-6243885775).

#### A084 — [Issue #97044](https://github.com/anthropics/claude-code/issues/97044)

> Extension chat webview causes renderer OOM crash (code 5) after large agent turns

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-25T08:59:03Z; updated 2026-10-26T02:05:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A085 — [Issue #104891](https://github.com/anthropics/claude-code/issues/104891)

> [Bug] Linux: enabling sandbox in project settings grows every running session to 6–8 GB RSS until the OOM killer fires

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-24T20:25:35Z; updated 2026-10-24T20:26:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A086 — [Issue #92422](https://github.com/anthropics/claude-code/issues/92422)

> [Bug] Excessive unused memory allocation causing OOM when vm.overcommit_memory=2

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-06T02:35:47Z; updated 2026-10-27T22:07:39Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A087 — [Issue #67433](https://github.com/anthropics/claude-code/issues/67433)

> [Bug] Off-heap memory leak: RSS grows 400–500 MB/min while idle, reaches multi-GB

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-06-11T09:16:41Z; updated 2026-08-04T21:21:58Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/67433#issuecomment-4738118739).

#### A088 — [Issue #82188](https://github.com/anthropics/claude-code/issues/82188)

> Background daemon (v2.1.220) leaks to ~11GB RSS, repeated OOM-kills cascade into full WSL2 session teardown

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-29T06:24:57Z; updated 2026-08-26T23:57:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/82188#issuecomment-5177200766).

#### A089 — [Issue #68626](https://github.com/anthropics/claude-code/issues/68626)

> Scheduled tasks leak headless claude.exe --resume processes on Windows (never exit, accumulate until OOM)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-06-15T16:11:50Z; updated 2026-10-19T10:11:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/68626#issuecomment-5471455998).

#### A090 — [Issue #91879](https://github.com/anthropics/claude-code/issues/91879)

> Scheduled-task runs leak a resident claude process per fire (2.1.255, Linux): 106 procs / 26 GB in 25 h —

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T18:30:31Z; updated 2026-10-25T22:08:39Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91879#issuecomment-5536208277).

#### A092 — [Issue #86443](https://github.com/anthropics/claude-code/issues/86443)

> [BUG] Desktop app (macOS): scheduled sessions with background tasks leak harness processes indefinitely (task-notification race, follow-up to #39632)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-13T17:05:51Z; updated 2026-10-24T22:09:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A093 — [Issue #81095](https://github.com/anthropics/claude-code/issues/81095)

> Windows: Claude Desktop Node service leaks one headless ConPTY (conhost.exe) per PowerShell tool call and never releases it — unbounded,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-25T08:32:07Z; updated 2026-10-16T17:04:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/81095#issuecomment-5078821540).

#### A094 — [Issue #95387](https://github.com/anthropics/claude-code/issues/95387)

> Windows: Claude Desktop Terminal panel leaks one interactive ConPTY pwsh.exe (~85 MB) per Code session; ending the session does not

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-18T15:09:04Z; updated 2026-09-18T16:28:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A095 — [Issue #87891](https://github.com/anthropics/claude-code/issues/87891)

> [BUG] Background daemon never reaps stale workers or unclaimed spares — they are re-adopted on every restart (64 leaked processes

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-19T09:14:00Z; updated 2026-10-21T23:22:44Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A096 — [Issue #96746](https://github.com/anthropics/claude-code/issues/96746)

> [BUG] [Windows] VS Code extension still leaks orphan claude.exe processes in 2.1.281 (one per window at startup, plus /clear and

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-24T13:36:28Z; updated 2026-09-24T13:37:38Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A097 — [Issue #71424](https://github.com/anthropics/claude-code/issues/71424)

> Claude Desktop local-agent (Cowork) sessions leak claude-code node processes (never exit at session end) — GBs of RAM + MCP

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-06-25T19:54:01Z; updated 2026-10-22T00:39:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/71424#issuecomment-5119736942), [comment 2](https://github.com/anthropics/claude-code/issues/71424#issuecomment-5194707293), [comment 3](https://github.com/anthropics/claude-code/issues/71424#issuecomment-6329810091).

#### A110 — [Issue #89062](https://github.com/anthropics/claude-code/issues/89062)

> CLI hangs in a 100%-CPU main-thread loop and ignores SIGTERM/SIGINT (19 sample captures, 3 versions, identical stack)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-23T20:21:05Z; updated 2026-09-12T20:08:52Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A128 — [Issue #90581](https://github.com/anthropics/claude-code/issues/90581)

> [BUG] remote-control: transient supervisor exits (poll 401 / memory pressure) permanently orphan every attached session — environment survives a 2s

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-29T13:31:09Z; updated 2026-09-14T02:43:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/90581#issuecomment-5658269480).

#### A139 — [Issue #93469](https://github.com/anthropics/claude-code/issues/93469)

> Local ~/.claude directory (settings, skills, per-project memory) silently reset on disk, while ~/.claude.json history stays intact

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T20:39:31Z; updated 2026-09-11T19:55:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A161 — [Issue #99378](https://github.com/anthropics/claude-code/issues/99378)

> VS Code extension native binary crashes (SIGSEGV) on CPU with AVX but no AVX2

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-04T05:30:07Z; updated 2026-10-04T05:35:34Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A164 — [Issue #96625](https://github.com/anthropics/claude-code/issues/96625)

> Bash tool leaves orphaned background processes running after session crash/force-quit

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-24T06:43:39Z; updated 2026-10-06T19:39:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A166 — [Issue #96402](https://github.com/anthropics/claude-code/issues/96402)

> [BUG] SIGILL on x86-64 CPU without AVX (Linux, bare metal) — native installer 2.1.280 and npm 2.1.197 both crash; 2.1.112

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T16:03:11Z; updated 2026-09-28T23:02:19Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A173 — [Issue #90507](https://github.com/anthropics/claude-code/issues/90507)

> [BUG] Regression: Claude Code crashes with SIGILL on non-AVX CPU (macOS 12.7.6, 2.1.251) — see also #19907, #19904, #19967, #20611

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-29T04:47:24Z; updated 2026-09-28T20:02:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A175 — [Issue #90478](https://github.com/anthropics/claude-code/issues/90478)

> Browser/preview pane hard-crashes the entire Claude Desktop app on Windows 11 — conhost.exe AppHang, hang type `Quiesce` (correlates with KB5120998)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-28T23:19:06Z; updated 2026-10-17T10:09:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A181 — [Issue #88864](https://github.com/anthropics/claude-code/issues/88864)

> [BUG] Qemu VM : arm64 OK, x86+KVM+AVX2 OK , x86+KVM KO (hangs forever 100% CPU) , x86 KO (crashes)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-22T18:13:52Z; updated 2026-09-28T20:02:56Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A194 — [Issue #104348](https://github.com/anthropics/claude-code/issues/104348)

> [BUG] Cowork VM hangs after Windows sleep/resume and spins ~2 CPU cores for days, though the user never opened Cowork

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T17:30:37Z; updated 2026-10-22T17:32:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A221 — [Issue #95566](https://github.com/anthropics/claude-code/issues/95566)

> Native binary hangs silently at 100% CPU on VMs with the kvm64 CPU model (no SSE4/POPCNT) — needs a CPU

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-19T16:08:54Z; updated 2026-10-20T00:08:04Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/95566#issuecomment-5759050860).

#### A246 — [Issue #89627](https://github.com/anthropics/claude-code/issues/89627)

> [BUG] claude install and claude doctor hang indefinitely at ~100% CPU (Proxmox/QEMU VM)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-25T20:13:24Z; updated 2026-10-15T10:10:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A260 — [Issue #104932](https://github.com/anthropics/claude-code/issues/104932)

> [BUG] Linux CLI: 2+ concurrent sessions hard-freeze a VMware guest (rtkit canary starvation, no OOM logged); regression after 2.1.275, 2.1.274

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-25T02:38:05Z; updated 2026-10-25T02:39:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A261 — [Issue #33350](https://github.com/anthropics/claude-code/issues/33350)

> [BUG] v2.1.73 causes terminal freeze with yellow search bar in tmux sessions - memory leak related

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-03-11T20:39:31Z; updated 2026-03-15T08:28:12Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A262 — [Issue #21378](https://github.com/anthropics/claude-code/issues/21378)

> 🚨 CRITICAL: Memory leak causes freeze after 20+ minutes (15GB RAM consumption)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-28T03:48:11Z; updated 2026-08-19T13:30:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/21378#issuecomment-3815875567), [comment 2](https://github.com/anthropics/claude-code/issues/21378#issuecomment-3864604814), [comment 3](https://github.com/anthropics/claude-code/issues/21378#issuecomment-3902883969).

#### A264 — [Issue #18532](https://github.com/anthropics/claude-code/issues/18532)

> [BUG] Claude Code v2.1.9 Complete Freeze - 100% CPU, Main Thread Stuck in Infinite Loop (macOS ARM64)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-16T08:27:34Z; updated 2026-08-24T03:08:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/18532#issuecomment-3800233506), [comment 2](https://github.com/anthropics/claude-code/issues/18532#issuecomment-3865888661), [comment 3](https://github.com/anthropics/claude-code/issues/18532#issuecomment-4099610945), [comment 4](https://github.com/anthropics/claude-code/issues/18532#issuecomment-4525732741).

#### A265 — [Issue #103349](https://github.com/anthropics/claude-code/issues/103349)

> Windows desktop: after a few days the app leaves dozens of hidden PowerShell and console processes running, the PC runs

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T02:50:10Z; updated 2026-10-19T02:51:33Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A266 — [Issue #98092](https://github.com/anthropics/claude-code/issues/98092)

> Commands that hit the Bash timeout keep running in the background unbounded; agents re-run them and processes pile up until

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-29T08:35:30Z; updated 2026-10-27T16:04:31Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A267 — [Issue #88982](https://github.com/anthropics/claude-code/issues/88982)

> Scheduled task sessions (Desktop local agent mode) never exit after completing; processes accumulate until the host runs out of memory

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-23T13:21:01Z; updated 2026-10-23T10:10:46Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/88982#issuecomment-5508223637).

#### A268 — [Issue #18859](https://github.com/anthropics/claude-code/issues/18859)

> [BUG] Memory leak in long-running idle Claude Code sessions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-17T18:58:54Z; updated 2026-10-01T07:24:30Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A305 — [Issue #89075](https://github.com/anthropics/claude-code/issues/89075)

> [BUG] VS Code extension host restart due to OOM caused by Claude Code loading histories of ALL sessions!

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-23T21:32:23Z; updated 2026-09-25T18:27:31Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/89075#issuecomment-5837460815).

### Billing, account attribution and cost visibility

9 existing issue reports. The grouping is editorial, not a severity rating.

#### A046 — [Issue #95594](https://github.com/anthropics/claude-code/issues/95594)

> Unauthorized Financial Transaction - AI Assistant Bypassed Explicit Safety Interlock

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-19T20:29:47Z; updated 2026-09-26T10:29:06Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A064 — [Issue #103648](https://github.com/anthropics/claude-code/issues/103648)

> [BUG] Expired subscription login silently falls back to ant CLI Console credentials, billing per-token

The claimed fallback could change the billing account. Confirm account identity and authentication precedence before concluding the billing was wrong.

Source snapshot: open; created 2026-10-20T03:46:16Z; updated 2026-10-20T04:00:02Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/103648#issuecomment-6282879854).

#### A065 — [Issue #101747](https://github.com/anthropics/claude-code/issues/101747)

> [BUG] `claude` processes spawned from a desktop Code session ignore the session's account and fall back to the OS user's

The report alleges a child process selecting the default operating-system profile, potentially affecting account attribution and data access.

Source snapshot: open; created 2026-10-13T11:02:24Z; updated 2026-10-13T12:07:34Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A151 — [Issue #81078](https://github.com/anthropics/claude-code/issues/81078)

> [BUG][Billing] Claude Code auto-created an API key + workspace after re-auth, silently routing subscription usage to pay-per-use API; runaway 8h+

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-25T07:19:42Z; updated 2026-10-02T10:17:06Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/81078#issuecomment-5077532986), [comment 2](https://github.com/anthropics/claude-code/issues/81078#issuecomment-5077540613).

#### A152 — [Issue #16489](https://github.com/anthropics/claude-code/issues/16489)

> [BUG] Claude Code uses API billing despite forceLoginMethod: claudeai setting

The source disputes billing-account selection despite a configured login method. Reconcile against actual account and request records.

Source snapshot: open; created 2026-01-06T17:08:51Z; updated 2026-02-26T13:59:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/16489#issuecomment-3788191888).

#### A153 — [Issue #92776](https://github.com/anthropics/claude-code/issues/92776)

> [BUG] OTel token.usage / cost.usage silently stop recording main-loop turns mid-session (3% of actual captured)

Usage telemetry stopping is not proof that the actual invoice is wrong; it concerns visibility and monitoring.

Source snapshot: open; created 2026-09-08T04:33:31Z; updated 2026-09-08T04:34:38Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A154 — [Issue #83162](https://github.com/anthropics/claude-code/issues/83162)

> Title: Background task reported exit 0 on OOM failure, Claude proceeded to push stale image to production ECR causing $250

The source alleges an OOM failure was surfaced as success and downstream deployment proceeded. Financial-loss amounts have not been validated.

Source snapshot: open; created 2026-08-01T18:46:22Z; updated 2026-10-19T10:10:47Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A335 — [Issue #100546](https://github.com/anthropics/claude-code/issues/100546)

> [BUG] Usage-limit stop leaves background processes running with no warning (17 hours, about 59k API calls); $2K in unexpected charges

The reported unexpected cost concerns background activity after a usage stop. Do not assume all charges were Anthropic API charges or independently validate the amount.

Source snapshot: open; created 2026-10-08T15:34:36Z; updated 2026-10-08T15:36:20Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A336 — [Issue #105063](https://github.com/anthropics/claude-code/issues/105063)

> Unauthorized Pro → Max 20x upgrade and charge (€201.92) without user consent

This is an account-level charge dispute. Authorization and entitlement require private account records; the public report alone cannot establish an improper charge.

Source snapshot: open; created 2026-10-25T19:20:58Z; updated 2026-10-25T19:22:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

### Application and essential-workflow availability

148 existing issue reports. The grouping is editorial, not a severity rating.

#### A001 — [Issue #99193](https://github.com/anthropics/claude-code/issues/99193)

> [BUG] Windows: sub-agent rm -rf on the 8.3 short-name alias of the home dir wiped ~116 GB; TaskStop left it

The reporter describes a home-directory alias resolving to a destructive target and a child process surviving TaskStop. Loss volume and the absence of a permission prompt remain reporter claims.

Source snapshot: open; created 2026-10-03T09:32:20Z; updated 2026-10-24T13:13:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/99193#issuecomment-5969933377), [comment 2](https://github.com/anthropics/claude-code/issues/99193#issuecomment-6384641747).

#### A002 — [Issue #92593](https://github.com/anthropics/claude-code/issues/92593)

> Runaway rm -rf: timeout auto-backgrounding kept a destructive command running, and TaskStop did not kill the child process (Windows)

The reporter says stopping the wrapper left its destructive child running. Related process-tree reports may share one root cause; this is a reported case, not another independently established defect.

Source snapshot: open; created 2026-09-07T04:34:56Z; updated 2026-10-22T19:34:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A004 — [Issue #97660](https://github.com/anthropics/claude-code/issues/97660)

> [BUG] Subagent ran rm -rf \ via PowerShell → MSYS2 bash (PowerShell expanded the escaped variables to empty), wiping C:\

Reported PowerShell expansion changed the nested shell's deletion target. The claimed lost volume is not independently validated.

Source snapshot: open; created 2026-09-27T16:06:47Z; updated 2026-10-07T02:58:23Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A009 — [Issue #99768](https://github.com/anthropics/claude-code/issues/99768)

> [Bug] Background task cleanup with sudo kills entire process tree instead of target process group

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-05T19:06:09Z; updated 2026-10-08T21:02:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/99768#issuecomment-6043782937).

#### A012 — [Issue #95355](https://github.com/anthropics/claude-code/issues/95355)

> [BUG] Critical: git stash pop + reset --hard destroyed ~600 lines of new code and unrelated stash in worktree session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-18T12:25:28Z; updated 2026-10-20T16:59:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A013 — [Issue #104331](https://github.com/anthropics/claude-code/issues/104331)

> [Safety] Claude Code ran unrequested `git checkout` + `git reset --hard`, silently destroying the user's gitignored .env (API keys)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-22T16:44:52Z; updated 2026-10-25T01:46:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A023 — [Issue #97759](https://github.com/anthropics/claude-code/issues/97759)

> [BUG] Harness tells the model to save scripts and outputs to the scratchpad, which macOS wipes at reboot; no setting

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-28T06:40:11Z; updated 2026-10-18T13:52:23Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A024 — [Issue #96628](https://github.com/anthropics/claude-code/issues/96628)

> [BUG] After a tool call fails to parse, the retry notice can point `parentUuid` at a row that is never

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-24T06:45:39Z; updated 2026-10-27T00:53:49Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A026 — [Issue #94794](https://github.com/anthropics/claude-code/issues/94794)

> [BUG] external file changes are not notified to the agent before an Edit tool call when the file was only

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-16T15:16:55Z; updated 2026-09-16T15:30:57Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A030 — [Issue #92168](https://github.com/anthropics/claude-code/issues/92168)

> change_directory leaves $CLAUDE_PROJECT_DIR at the launch project, and the resulting ENOENT silently erases every user prompt (exit 2 reads as

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T17:30:41Z; updated 2026-09-24T09:35:23Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/92168#issuecomment-5811613761).

#### A031 — [Issue #91676](https://github.com/anthropics/claude-code/issues/91676)

> [BUG] Sandboxed `mktemp -d` fails on macOS (ignores `$TMPDIR`); the empty variable made `rm -rf "$T"` run against the working

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T03:03:52Z; updated 2026-10-09T18:19:23Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91676#issuecomment-6086731542).

#### A035 — [Issue #97084](https://github.com/anthropics/claude-code/issues/97084)

> Critical: Claude ignored explicit 'no upload' instruction and purged GCS version history

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-25T11:22:44Z; updated 2026-10-03T12:53:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A042 — [Issue #96261](https://github.com/anthropics/claude-code/issues/96261)

> [BUG] /compact on Sonnet 5: the summarizer treats the compaction instruction as a prompt injection, answers the last question instead,

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T06:52:50Z; updated 2026-09-23T08:32:08Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A043 — [Issue #94675](https://github.com/anthropics/claude-code/issues/94675)

> UserPromptSubmit fires for agent/system-injected messages with no prompt_source/is_meta in the payload — hooks cannot tell them from typed input (prompt-injection

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-16T06:14:01Z; updated 2026-10-01T02:18:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A057 — [Issue #103456](https://github.com/anthropics/claude-code/issues/103456)

> [BUG] Claude Code told me .dev.vars "would never be published", then deployed the entire project directory to Cloudflare Pages, leaking

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-19T13:32:00Z; updated 2026-10-19T17:49:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A069 — [Issue #104774](https://github.com/anthropics/claude-code/issues/104774)

> [Bug] Subagent leaks userEmail into curl User-Agent header sent to sec.gov despite no-disclosure instruction

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-24T05:59:38Z; updated 2026-10-24T06:00:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A070 — [Issue #91155](https://github.com/anthropics/claude-code/issues/91155)

> [BUG] IDE extension: retained editor selection is never invalidated when the document closes, and leaks into new conversations

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T06:40:49Z; updated 2026-10-21T10:11:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A071 — [Issue #79233](https://github.com/anthropics/claude-code/issues/79233)

> CLAUDE_CONFIG_DIR is not honored by .claude/rules/*.md auto-attachment (leaks default profile's rules into isolated profiles)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-19T22:22:05Z; updated 2026-10-22T13:36:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A074 — [Issue #101140](https://github.com/anthropics/claude-code/issues/101140)

> [Bug] Claude Code sessions leak tool uses and diffs across VS Code split terminals

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-10T23:37:13Z; updated 2026-10-10T23:40:11Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A076 — [Issue #98708](https://github.com/anthropics/claude-code/issues/98708)

> [Critical] Runaway: agent could not be stopped by any in-product means; only closing the VS Code window with the X

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-01T14:31:51Z; updated 2026-10-01T14:35:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/98708#issuecomment-5933668223).

#### A077 — [Issue #92510](https://github.com/anthropics/claude-code/issues/92510)

> [BUG] Cowork/Code VM leaks host file descriptors (~400k) until macOS exhausts kern.maxfiles and panics/reboots

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-06T15:24:53Z; updated 2026-10-27T19:17:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A099 — [Issue #102389](https://github.com/anthropics/claude-code/issues/102389)

> [BUG] ToolSearch loads an MCP tool bigger than the context window; auto-compact keeps it, so the session is permanently dead

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-15T12:11:25Z; updated 2026-10-16T16:32:30Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A100 — [Issue #96820](https://github.com/anthropics/claude-code/issues/96820)

> [BUG] Oversized plan file makes a session unrecoverable: compaction yields postTokens &gt; preTokens, and resume replays the stale copy

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-24T17:44:51Z; updated 2026-09-24T17:47:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A101 — [Issue #94055](https://github.com/anthropics/claude-code/issues/94055)

> Session dies permanently with `400 ... unexpected end of data` after a Bash result containing NUL bytes

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-13T21:09:03Z; updated 2026-10-09T05:21:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A102 — [Issue #95463](https://github.com/anthropics/claude-code/issues/95463)

> A `/goal` Stop-hook record written mid-turn splits an advisor server-tool call from its result, permanently bricking the session (400 loop)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-18T22:00:53Z; updated 2026-09-18T22:02:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A104 — [Issue #104122](https://github.com/anthropics/claude-code/issues/104122)

> [Bug] Session permanently broken after mid-turn user message splits advisor server_tool_use/result pair (400 on resume)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-21T21:21:59Z; updated 2026-10-21T21:23:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A106 — [Issue #93998](https://github.com/anthropics/claude-code/issues/93998)

> [BUG] Context prune can leave conversation in unrecoverable 400 loop

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-13T13:18:49Z; updated 2026-09-13T13:19:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A108 — [Issue #96781](https://github.com/anthropics/claude-code/issues/96781)

> [BUG] Interactive TUI freezes permanently: main thread blocks in openat() during clipboard polling (macOS)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-24T15:43:01Z; updated 2026-10-01T03:35:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A109 — [Issue #93495](https://github.com/anthropics/claude-code/issues/93495)

> Claude Desktop 1.49585.0 freezes: main thread deadlocks on synchronous UNUserNotificationCenter XPC call (macOS, regression of #57706)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-10T23:34:08Z; updated 2026-09-10T23:35:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A111 — [Issue #91648](https://github.com/anthropics/claude-code/issues/91648)

> [BUG] Windows: two Bash tool calls never return and never time out — main session deadlocks for 53 min; agent

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-02T23:05:30Z; updated 2026-10-23T22:10:43Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91648#issuecomment-5517711245).

#### A112 — [Issue #91226](https://github.com/anthropics/claude-code/issues/91226)

> PreToolUse Bash hook with relative command path can permanently deadlock the Bash tool for the rest of a session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T13:40:21Z; updated 2026-10-21T22:10:45Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A113 — [Issue #100167](https://github.com/anthropics/claude-code/issues/100167)

> All project hooks silently disappear for the rest of a session after the project's volume dismounts and remounts (Windows, Google

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-07T08:21:12Z; updated 2026-10-07T08:22:31Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A116 — [Issue #99271](https://github.com/anthropics/claude-code/issues/99271)

> [BUG] Projects: shared folder (/mnt/project-files) fails with EIO on every operation exactly 24 hours after the container's mount starts, and

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-03T16:52:44Z; updated 2026-10-03T16:53:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A118 — [Issue #96384](https://github.com/anthropics/claude-code/issues/96384)

> [BUG] Windows MSIX: while Desktop is down after an update, new Remote Control sessions connect but never register - machine

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T14:59:23Z; updated 2026-09-23T15:00:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A119 — [Issue #96942](https://github.com/anthropics/claude-code/issues/96942)

> [BUG] Windows: main process survives beforeQuitForUpdate; relaunch blocked by single-instance lock (update deadlock, reproduced on two versions)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-25T02:27:41Z; updated 2026-10-25T04:20:58Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/96942#issuecomment-5943036541), [comment 2](https://github.com/anthropics/claude-code/issues/96942#issuecomment-6021050610), [comment 3](https://github.com/anthropics/claude-code/issues/96942#issuecomment-6281054204), [comment 4](https://github.com/anthropics/claude-code/issues/96942#issuecomment-6393378375).

#### A120 — [Issue #91763](https://github.com/anthropics/claude-code/issues/91763)

> [BUG] Windows/MSIX: `git fsmonitor--daemon` spawned by Claude Code inherits the AppX container job, survives the update's forced shutdown, and blocks

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T10:18:15Z; updated 2026-10-08T23:59:37Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91763#issuecomment-5558977951), [comment 2](https://github.com/anthropics/claude-code/issues/91763#issuecomment-5604859842), [comment 3](https://github.com/anthropics/claude-code/issues/91763#issuecomment-6038457800).

#### A121 — [Issue #53247](https://github.com/anthropics/claude-code/issues/53247)

> [BUG] Claude Desktop fails to launch on Windows — orphaned Silo / Job Object after app crash, only logoff or

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-04-25T12:56:00Z; updated 2026-10-28T07:49:38Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/53247#issuecomment-4665446229), [comment 2](https://github.com/anthropics/claude-code/issues/53247#issuecomment-4691713023), [comment 3](https://github.com/anthropics/claude-code/issues/53247#issuecomment-4965578510), [comment 4](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5186999283), [comment 5](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5293117363), [comment 6](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5327095659), [comment 7](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5338807864), [comment 8](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5394741479), [comment 9](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5436748576), [comment 10](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5460046793), [comment 11](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5498974301), [comment 12](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5501404829), [comment 13](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5510825681), [comment 14](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5516138453), [comment 15](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5518133657), [comment 16](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5520878812), [comment 17](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5545408079), [comment 18](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5550904589), [comment 19](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5553667723), [comment 20](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5559082247), [comment 21](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5570647597), [comment 22](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5629285336), [comment 23](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5657698208), [comment 24](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5662878514), [comment 25](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5715735012), [comment 26](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5721770270), [comment 27](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5793933329), [comment 28](https://github.com/anthropics/claude-code/issues/53247#issuecomment-5798551980).

#### A122 — [Issue #89676](https://github.com/anthropics/claude-code/issues/89676)

> [BUG] Claude Desktop (Windows x64) — stale AppContainer Job leaked by AppInfo service blocks relaunch after ordinary crash (no update

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-26T01:22:28Z; updated 2026-10-27T10:12:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/89676#issuecomment-5536094643), [comment 2](https://github.com/anthropics/claude-code/issues/89676#issuecomment-5546760452).

#### A123 — [Issue #95901](https://github.com/anthropics/claude-code/issues/95901)

> [BUG] Claude Desktop reinstall fails with 0x80073CFF — orphaned CoworkVMService cannot be removed, blocks AddPackage

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-21T18:37:19Z; updated 2026-09-21T18:38:41Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A125 — [Issue #90233](https://github.com/anthropics/claude-code/issues/90233)

> [BUG][Windows] npm-global auto-update leaks a ~240 MB claude.exe.old per failure and can leave no claude.exe at all (update_apply_exe_locked)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-28T00:00:01Z; updated 2026-10-15T10:11:17Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A127 — [Issue #85840](https://github.com/anthropics/claude-code/issues/85840)

> [BUG] Windows: CoworkVMService can never arm its own recovery actions ("Access is denied" at every start) — service death becomes

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-11T14:40:49Z; updated 2026-10-22T14:34:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5269296724), [comment 2](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5310508193), [comment 3](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5328601296), [comment 4](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5473451499), [comment 5](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5504253739), [comment 6](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5527433760), [comment 7](https://github.com/anthropics/claude-code/issues/85840#issuecomment-5752912448).

#### A129 — [Issue #91087](https://github.com/anthropics/claude-code/issues/91087)

> Remote Control: sessions served by a crashed server are never re-claimed — restart doesn't restore them and messages to disconnected

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T21:44:43Z; updated 2026-10-22T13:08:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A132 — [Issue #97067](https://github.com/anthropics/claude-code/issues/97067)

> [BUG] Uninstall/reinstall of Desktop (Windows MSIX) permanently orphans existing sessions — confirmed missing from claude.ai/code too, not just local cache

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-25T10:36:52Z; updated 2026-09-28T13:55:47Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A140 — [Issue #93791](https://github.com/anthropics/claude-code/issues/93791)

> ~/.claude config directory silently wiped and recreated - 4 incidents, matches #41415/#34330 pattern

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-12T08:32:17Z; updated 2026-09-12T08:33:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A142 — [Issue #103690](https://github.com/anthropics/claude-code/issues/103690)

> [BUG] Desktop Code tab: clicking the single-file change entry triggers a hidden Undo instead of opening the diff

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-20T08:10:51Z; updated 2026-10-20T08:17:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A146 — [Issue #96263](https://github.com/anthropics/claude-code/issues/96263)

> [BUG] Windows: Edit on a Shift_JIS file replaces every Japanese character in the file with U+FFFD and saves it as

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T07:05:41Z; updated 2026-10-10T14:19:39Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A155 — [Issue #105593](https://github.com/anthropics/claude-code/issues/105593)

> [BUG] linux-x64 native binary (2.1.311, 2.1.312) SIGSEGVs every few turns under Rosetta in an x86_64 dev container on Apple Silicon;

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-28T06:27:59Z; updated 2026-10-28T08:36:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/105593#issuecomment-6463134116).

#### A156 — [Issue #105318](https://github.com/anthropics/claude-code/issues/105318)

> [BUG] Windows Desktop 3.x: Electron main process (CrBrowserMain) crashes 0xc0000005 several times a day — V8 jumps to a tagged

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-27T00:13:07Z; updated 2026-10-27T17:33:50Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A157 — [Issue #105296](https://github.com/anthropics/claude-code/issues/105296)

> [BUG] Segfault at 0xD0 on startup (Bun 1.4.4, Linux arm64, Cortex-A72 without LSE) - every launch crashes

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-26T21:51:04Z; updated 2026-10-26T21:53:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A158 — [Issue #104108](https://github.com/anthropics/claude-code/issues/104108)

> [BUG] VS Code extension 2.1.306: Claude panel webview crashes (Chrome sad face) in browser VS Code (code serve-web) on Chrome

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-21T20:10:41Z; updated 2026-10-25T21:06:47Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A159 — [Issue #104019](https://github.com/anthropics/claude-code/issues/104019)

> Ghost background tasks remain "running" after a crash and cannot be cleared over Remote Control

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-21T14:43:15Z; updated 2026-10-21T14:44:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A160 — [Issue #102009](https://github.com/anthropics/claude-code/issues/102009)

> [BUG] VS Code: CLI with a running background task outlives a crashed extension host and holds the session ("still open

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-14T09:27:26Z; updated 2026-10-14T14:07:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A162 — [Issue #97530](https://github.com/anthropics/claude-code/issues/97530)

> Desktop app crashes (no clean shutdown) under concurrent session-spawn load; same mechanism causes session-switch lag

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-26T22:40:15Z; updated 2026-10-16T20:00:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A163 — [Issue #96802](https://github.com/anthropics/claude-code/issues/96802)

> [BUG] Background daemon respawn crashes "exit 1 before init" when Fleet view reattaches an idle session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-24T16:42:35Z; updated 2026-09-24T16:43:52Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A165 — [Issue #96498](https://github.com/anthropics/claude-code/issues/96498)

> VS Code extension crashes when switching branch while resuming /remote-control session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T20:49:33Z; updated 2026-09-23T20:50:31Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A167 — [Issue #93141](https://github.com/anthropics/claude-code/issues/93141)

> [BUG] Cowork crashes on every session with "Scheduled tasks not initialized" (100% reproducible)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-09T16:44:24Z; updated 2026-09-10T15:06:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A168 — [Issue #93038](https://github.com/anthropics/claude-code/issues/93038)

> [BUG] Claude Code 2.1.266 crashes with "Bus error" on WSL2 (npm/NVM install) — 2.1.265 works

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-09T09:12:55Z; updated 2026-09-09T09:14:20Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A169 — [Issue #92916](https://github.com/anthropics/claude-code/issues/92916)

> [BUG] Claude Code 2.1.263 crashes with Bun segmentation fault on Windows 11 — reproducible on trivial prompts

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-08T18:42:16Z; updated 2026-09-10T06:25:41Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/92916#issuecomment-5603289250), [comment 2](https://github.com/anthropics/claude-code/issues/92916#issuecomment-5603568403), [comment 3](https://github.com/anthropics/claude-code/issues/92916#issuecomment-5604063227), [comment 4](https://github.com/anthropics/claude-code/issues/92916#issuecomment-5606537341).

#### A170 — [Issue #91941](https://github.com/anthropics/claude-code/issues/91941)

> [BUG] Linux Desktop: backend NodeService utility process aborts (SIGABRT) — event-loop stalls compound into whole-app crash-loop

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T00:13:36Z; updated 2026-10-25T10:10:05Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A171 — [Issue #91578](https://github.com/anthropics/claude-code/issues/91578)

> Windows desktop app: idle warm sessions never release MCP child processes (1 to 1,182 children / 33 GB RSS in

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-02T19:08:38Z; updated 2026-10-23T22:10:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91578#issuecomment-5515026820).

#### A172 — [Issue #90892](https://github.com/anthropics/claude-code/issues/90892)

> Claude Desktop crashes when the Browser pane is opened at an external https URL (3/3)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T04:10:45Z; updated 2026-10-19T22:10:39Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A174 — [Issue #90495](https://github.com/anthropics/claude-code/issues/90495)

> Windows: exec-form hook args dropped, still routed through bash.exe, causing eval_stdin crash

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-29T02:24:45Z; updated 2026-10-16T22:09:49Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A176 — [Issue #90418](https://github.com/anthropics/claude-code/issues/90418)

> Windows desktop app crashes when Browser pane opens a Cloudflare-challenged site (preview_start)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-28T17:51:27Z; updated 2026-10-22T22:10:02Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/90418#issuecomment-5499784423).

#### A178 — [Issue #90122](https://github.com/anthropics/claude-code/issues/90122)

> [Windows] Plugin hooks' commandWindows field silently ignored - forces Git Bash, causes MSYS2 crash (errno 1 add_item)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-27T14:10:29Z; updated 2026-09-11T18:07:46Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/90122#issuecomment-5638731680).

#### A179 — [Issue #89692](https://github.com/anthropics/claude-code/issues/89692)

> Windows desktop app (MSIX) wedges on every auto-update - crash-loops until reboot, 3 reboots in one day

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-26T02:35:35Z; updated 2026-10-22T22:10:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/89692#issuecomment-5435101995).

#### A180 — [Issue #89679](https://github.com/anthropics/claude-code/issues/89679)

> [BUG] Claude Desktop (Windows x64) — recurring "freeze-then-vanish" crash with zero forensic trace across all standard channels

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-26T01:25:28Z; updated 2026-10-27T22:07:41Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/89679#issuecomment-5552105867).

#### A182 — [Issue #87963](https://github.com/anthropics/claude-code/issues/87963)

> [BUG] Remote Control: ending a session from the app exits the child 1, so the bridge reports a crash and

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-19T13:49:20Z; updated 2026-10-15T13:03:54Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/87963#issuecomment-5552593764).

#### A184 — [Issue #73600](https://github.com/anthropics/claude-code/issues/73600)

> Background worker crash family (#61740 successor): no claim-time cwd validation for spares; adopted workers mis-settled as "crashed" across daemon upgrade

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-02T21:09:34Z; updated 2026-09-18T11:30:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A185 — [Issue #69590](https://github.com/anthropics/claude-code/issues/69590)

> [BUG] Native Windows CLI crashes at loader init (0xC0000005) before entry point — Win11 26200, i9-13900

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-06-19T15:02:48Z; updated 2026-07-28T16:56:32Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A186 — [Issue #65216](https://github.com/anthropics/claude-code/issues/65216)

> Worktree-relocated background agent sessions crash-loop on reopen from the agents view ("No conversation found with session ID")

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-06-03T23:53:59Z; updated 2026-10-27T12:07:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/65216#issuecomment-5085028508).

#### A188 — [Issue #16691](https://github.com/anthropics/claude-code/issues/16691)

> [Bug] Claude in Chrome Native Host crashes on Windows 11 - Bun internal assertion failure

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-07T20:37:06Z; updated 2026-03-11T11:18:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/16691#issuecomment-3805301745), [comment 2](https://github.com/anthropics/claude-code/issues/16691#issuecomment-3857895588), [comment 3](https://github.com/anthropics/claude-code/issues/16691#issuecomment-3873568998), [comment 4](https://github.com/anthropics/claude-code/issues/16691#issuecomment-4038505319).

#### A189 — [Issue #16135](https://github.com/anthropics/claude-code/issues/16135)

> Background process termination crashes Claude Code in Docker containers

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-03T07:25:29Z; updated 2026-07-16T20:42:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/16135#issuecomment-4466742913), [comment 2](https://github.com/anthropics/claude-code/issues/16135#issuecomment-4989483460).

#### A190 — [Issue #105337](https://github.com/anthropics/claude-code/issues/105337)

> Bash tool hangs indefinitely on a macOS privacy (TCC) prompt; remote user gets no indication

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-27T04:11:26Z; updated 2026-10-28T02:24:22Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A192 — [Issue #105149](https://github.com/anthropics/claude-code/issues/105149)

> [Bug] 2.1.302 hangs on startup, including `claude --version` (2.1.299 works)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-26T09:05:16Z; updated 2026-10-26T09:06:42Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A195 — [Issue #103978](https://github.com/anthropics/claude-code/issues/103978)

> [BUG] Desktop: start_session side session hangs after worktree creation and never spawns Claude Code ("Claude Code didn't start within 5

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-21T10:48:31Z; updated 2026-10-26T16:21:03Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A196 — [Issue #103599](https://github.com/anthropics/claude-code/issues/103599)

> [BUG] 2.1.301: frequent "No response from API" first-byte hangs (6.2/1k replies) — rolling back to 2.1.299 cut it to 0.45/1k

Follow-up retracts the apparent improvement from rollback. The version-specific rate comparison in the title should not be used as causal evidence.

Source snapshot: open; created 2026-10-19T22:50:01Z; updated 2026-10-26T20:31:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/103599#issuecomment-6289071307).

#### A198 — [Issue #102635](https://github.com/anthropics/claude-code/issues/102635)

> [BUG] Desktop (Windows, WSL): long-running asyncRewake SessionStart hook blocks new Code sessions (hang on first message)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-16T03:39:02Z; updated 2026-10-23T15:50:55Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/102635#issuecomment-6207688959).

#### A199 — [Issue #101154](https://github.com/anthropics/claude-code/issues/101154)

> [Bug] Bash tool calls hang before dispatch on Windows desktop; Stop ignored until claude.exe killed

Follow-up corrects the mode: both observed sessions were in auto mode, despite one launch argument saying acceptEdits.

Source snapshot: open; created 2026-10-11T02:09:18Z; updated 2026-10-14T08:02:24Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/101154#issuecomment-6104555655).

#### A200 — [Issue #101132](https://github.com/anthropics/claude-code/issues/101132)

> [Bug] iOS app sessions on desktop-served Remote Control hang; "That mode isn't available right now"

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-10T22:41:39Z; updated 2026-10-10T22:42:56Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A201 — [Issue #100451](https://github.com/anthropics/claude-code/issues/100451)

> [BUG] Desktop app main process hangs and is force-killed on every launch of 2.26454.2 (macOS)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-08T09:09:18Z; updated 2026-10-08T15:10:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A202 — [Issue #100241](https://github.com/anthropics/claude-code/issues/100241)

> [BUG] macOS: startup hangs forever (uninterruptible openat) when known_marketplaces.json installLocation points under /home (autofs)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-07T14:37:04Z; updated 2026-10-07T15:06:43Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A204 — [Issue #99524](https://github.com/anthropics/claude-code/issues/99524)

> [BUG] After a network change, the next request hangs 180s on a dead connection before retrying (Linux)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-04T21:52:46Z; updated 2026-10-24T10:51:13Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A206 — [Issue #99056](https://github.com/anthropics/claude-code/issues/99056)

> [BUG] Windows desktop app: all child processes terminated simultaneously (exitCode 1, reason=killed), UI hangs — 15 occurrences since 9/28, survives

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-02T19:40:18Z; updated 2026-10-02T19:41:43Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A207 — [Issue #99008](https://github.com/anthropics/claude-code/issues/99008)

> [BUG] [Cowork] Typing /skill whose !`cmd` fails hangs the cloud session silently (interactive twin of #87159)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-02T15:37:53Z; updated 2026-10-02T22:20:08Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/99008#issuecomment-5956058496), [comment 2](https://github.com/anthropics/claude-code/issues/99008#issuecomment-5956340604), [comment 3](https://github.com/anthropics/claude-code/issues/99008#issuecomment-5962373373).

#### A208 — [Issue #98938](https://github.com/anthropics/claude-code/issues/98938)

> [BUG] Sandbox: pnpm hangs forever when the project pins another pnpm version, and the write denial is never reported

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-02T10:50:26Z; updated 2026-10-24T21:49:38Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A209 — [Issue #98424](https://github.com/anthropics/claude-code/issues/98424)

> Local sandbox (bwrap) hangs indefinitely when any unrelated hard-mounted NFS/autofs share is unreachable

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-30T14:17:30Z; updated 2026-09-30T14:24:56Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A210 — [Issue #98343](https://github.com/anthropics/claude-code/issues/98343)

> [BUG] Auto-compact hangs indefinitely on Bedrock: post-compact CountTokens call has no timeout and cannot be interrupted

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-30T06:52:17Z; updated 2026-10-23T09:50:14Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A211 — [Issue #98310](https://github.com/anthropics/claude-code/issues/98310)

> Remote Control: unarchived server-mode sessions are never re-dispatched to the running host — messages hang at "Sending…", then "Claude Code

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-30T04:10:55Z; updated 2026-10-25T11:08:37Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A212 — [Issue #98291](https://github.com/anthropics/claude-code/issues/98291)

> [BUG] linux-arm64: --version works, --help and agents hang with empty output (Orange Pi Zero 3)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-30T01:10:47Z; updated 2026-09-30T01:12:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A213 — [Issue #98032](https://github.com/anthropics/claude-code/issues/98032)

> [BUG] Turns hang ~6 minutes then "Connection dropped (ECONNRESET)", sudden onset 2026-09-28, across all sessions on one Mac

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-29T01:01:20Z; updated 2026-10-03T17:09:24Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A215 — [Issue #97830](https://github.com/anthropics/claude-code/issues/97830)

> [BUG] Xcode 27.0 Claude Agent: claude 2.1.280 exits with code 1 within 40 ms of Xcode's first stdin write; conversations

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-28T10:07:17Z; updated 2026-10-03T15:47:01Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A216 — [Issue #96476](https://github.com/anthropics/claude-code/issues/96476)

> [Windows] Hook timeout kills only the Git Bash launcher; an orphaned grandchild keeps the stdout pipe open and the session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T19:22:30Z; updated 2026-09-26T11:38:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A217 — [Issue #96237](https://github.com/anthropics/claude-code/issues/96237)

> [BUG] Claude Code install/launch hangs indefinitely on Hyper-V VM with Processor Compatibility Mode enabled

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T04:39:11Z; updated 2026-09-28T20:03:02Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A218 — [Issue #96119](https://github.com/anthropics/claude-code/issues/96119)

> Image paste probe (xclip -t TARGETS -o) hangs forever on X11, leaving stuck processes for hours

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-22T19:08:50Z; updated 2026-09-22T19:09:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A219 — [Issue #95696](https://github.com/anthropics/claude-code/issues/95696)

> VS Code extension: session hangs indefinitely on stalled SSE stream (no idle-timeout/reconnect)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-20T16:13:44Z; updated 2026-09-20T16:22:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/95696#issuecomment-5751044078).

#### A220 — [Issue #95691](https://github.com/anthropics/claude-code/issues/95691)

> [BUG] Claude Code hangs with zero output on Ubuntu VM under Proxmox (all commands except --version)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-20T15:42:48Z; updated 2026-09-24T08:55:48Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A223 — [Issue #94806](https://github.com/anthropics/claude-code/issues/94806)

> Cowork desktop: MCP elicitation (2026-07-28 MRTR) dropped via print-mode branch, tool call hangs 180s

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-16T16:04:51Z; updated 2026-09-16T17:08:02Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A224 — [Issue #94641](https://github.com/anthropics/claude-code/issues/94641)

> [BUG] archive_session with session_id "self" hangs for hours in scheduled runs, delaying other scheduled tasks

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-16T01:43:32Z; updated 2026-09-16T01:44:30Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A225 — [Issue #94475](https://github.com/anthropics/claude-code/issues/94475)

> [BUG] VS Code integrated-browser MCP tools hang forever: action completes in browser but result never returns; session stuck until manual

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-15T09:40:58Z; updated 2026-09-15T14:06:25Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/94475#issuecomment-5681548298).

#### A227 — [Issue #94187](https://github.com/anthropics/claude-code/issues/94187)

> Desktop remote-SSH: native model picker sends bare model id, hangs/falls back instead of resolving to org's custom-role slug

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-14T03:55:54Z; updated 2026-09-14T03:56:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A228 — [Issue #94059](https://github.com/anthropics/claude-code/issues/94059)

> Background tasks: moved-to-background commands stay 'Running' after the process exits; background remote-shell call hangs on open stdin

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-13T22:23:07Z; updated 2026-09-13T22:24:13Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A229 — [Issue #93615](https://github.com/anthropics/claude-code/issues/93615)

> [BUG] Scheduled tasks: WebSearch tool calls hang indefinitely in background/cron-triggered sessions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-11T12:37:21Z; updated 2026-09-11T12:38:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A230 — [Issue #92932](https://github.com/anthropics/claude-code/issues/92932)

> New session hangs indefinitely when cwd is HOME with no git repo - unscoped rg scan hits TCC-denied paths

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-08T20:44:54Z; updated 2026-09-08T20:45:51Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A231 — [Issue #92921](https://github.com/anthropics/claude-code/issues/92921)

> [BUG] Cowork hangs after first message on Windows — clean VM boot confirmed, matches #26805/#26921/#44776/#59532 cluster

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-08T19:07:22Z; updated 2026-09-10T01:37:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A232 — [Issue #92789](https://github.com/anthropics/claude-code/issues/92789)

> Session hangs indefinitely — queued prompt never dispatched (reproduced 5x, 2 unrelated projects)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-08T06:24:09Z; updated 2026-09-08T12:04:47Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A233 — [Issue #92036](https://github.com/anthropics/claude-code/issues/92036)

> [Bug] Claude Code hangs indefinitely with worktree probe timeout in specific project directory

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T09:31:00Z; updated 2026-10-25T22:09:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A234 — [Issue #92014](https://github.com/anthropics/claude-code/issues/92014)

> [BUG] Claude Desktop - MCP tool call hangs silently if "Allow once" is clicked before Claude finishes generating the call

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T07:45:32Z; updated 2026-10-25T22:08:50Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A235 — [Issue #91987](https://github.com/anthropics/claude-code/issues/91987)

> claude -p headless session hangs at startup when a version-directory lock is contended by a concurrent interactive claude session

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-04T04:47:45Z; updated 2026-10-25T22:08:47Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A236 — [Issue #91881](https://github.com/anthropics/claude-code/issues/91881)

> [BUG] Windows native install/CLI hangs indefinitely with zero network activity (confirmed via Process Monitor)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-03T18:48:06Z; updated 2026-09-17T17:22:36Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A237 — [Issue #91321](https://github.com/anthropics/claude-code/issues/91321)

> remote-control in 2.1.257 never attempts a network connection (silent hang after banner; regression from 2.1.247)

Follow-up attributes the silent wait to an invisible first-run interactive prompt, rather than a proven failure to attempt networking.

Source snapshot: open; created 2026-09-01T21:18:02Z; updated 2026-10-22T22:10:15Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91321#issuecomment-5500780422).

#### A239 — [Issue #91131](https://github.com/anthropics/claude-code/issues/91131)

> [BUG] v2.1.248 hangs indefinitely on startup on Windows 11 VM (works on 2.1.58)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T03:08:58Z; updated 2026-09-19T16:09:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A240 — [Issue #91077](https://github.com/anthropics/claude-code/issues/91077)

> [BUG] Windows desktop: recurring MoAppHang mid-subagent-spawn (same Watson bucket across 4 versions); hang wedges MSIX package into "Can't open this

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T20:37:33Z; updated 2026-10-22T22:10:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/91077#issuecomment-5486531203).

#### A241 — [Issue #90970](https://github.com/anthropics/claude-code/issues/90970)

> [BUG] Slack MCP: http protocol-negotiation probe hangs -&gt; 30s CONNECT_TIMEOUT in every session except the one that most recently minted

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T12:22:25Z; updated 2026-10-20T10:10:10Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/90970#issuecomment-5478865886).

#### A242 — [Issue #90800](https://github.com/anthropics/claude-code/issues/90800)

> CLI hangs indefinitely on every subcommand except --version (headless Linux, both native and npm installs)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-30T17:16:14Z; updated 2026-10-21T00:37:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A243 — [Issue #90651](https://github.com/anthropics/claude-code/issues/90651)

> [BUG] Claude Code hangs indefinitely at "Setting up Claude Code..." with no error when Hardware Virtualization is disabled/unavailable

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-29T22:03:41Z; updated 2026-10-17T22:08:53Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A244 — [Issue #90126](https://github.com/anthropics/claude-code/issues/90126)

> [BUG] Native installer produces a binary with the correct size but the wrong contents; hangs pre-main on a pthread_mutex_lock

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-27T14:23:02Z; updated 2026-10-03T09:17:31Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/90126#issuecomment-5967652237).

#### A245 — [Issue #89791](https://github.com/anthropics/claude-code/issues/89791)

> Routines: unattended cloud runs hang indefinitely on sensitive-file prompts for `.claude/` writes (PreToolUse allow does not override)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-26T11:53:59Z; updated 2026-10-24T22:08:59Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A247 — [Issue #89135](https://github.com/anthropics/claude-code/issues/89135)

> [BUG] Scheduled routine "Run Now" hangs at "Initialized session" — possible regression of #84271

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-24T04:43:28Z; updated 2026-10-15T10:11:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A249 — [Issue #86910](https://github.com/anthropics/claude-code/issues/86910)

> [BUG] WebFetch hangs forever on a CSS-heavy 1 MB page

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-15T13:46:17Z; updated 2026-10-23T22:10:18Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/86910#issuecomment-5468989922), [comment 2](https://github.com/anthropics/claude-code/issues/86910#issuecomment-5515663169), [comment 3](https://github.com/anthropics/claude-code/issues/86910#issuecomment-5515832991).

#### A250 — [Issue #86574](https://github.com/anthropics/claude-code/issues/86574)

> Desktop: sessions with "create a fresh worktree" enabled hang and create nothing — regression between 1.24012.9 and 1.26832.0

Follow-up narrows this to worktree-backed session creation on a clean repository; earlier empty-payload and background-chip explanations were retracted.

Source snapshot: open; created 2026-08-14T02:46:11Z; updated 2026-10-18T10:09:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/86574#issuecomment-5302951127), [comment 2](https://github.com/anthropics/claude-code/issues/86574#issuecomment-5467667954).

#### A251 — [Issue #86000](https://github.com/anthropics/claude-code/issues/86000)

> [BUG] All Bash tool commands hang indefinitely — no child process is ever spawned (macOS, v2.1.228)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-12T03:41:14Z; updated 2026-09-10T12:11:12Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/86000#issuecomment-5618466867).

#### A252 — [Issue #77754](https://github.com/anthropics/claude-code/issues/77754)

> Windows: daemon named-pipe connection hangs 45s+ for any externally-launched process (Orca, VS Code, native PowerShell/cmd)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-15T10:19:55Z; updated 2026-09-03T07:58:33Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A253 — [Issue #75571](https://github.com/anthropics/claude-code/issues/75571)

> VS Code Extension 2.1.204 hangs for 90+ seconds every 30-40 min (macOS ARM64) — native process correctly idle in kevent64

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-07-08T06:14:21Z; updated 2026-09-18T11:14:38Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/75571#issuecomment-4911923942), [comment 2](https://github.com/anthropics/claude-code/issues/75571#issuecomment-4911931497), [comment 3](https://github.com/anthropics/claude-code/issues/75571#issuecomment-4915303307), [comment 4](https://github.com/anthropics/claude-code/issues/75571#issuecomment-4915349971), [comment 5](https://github.com/anthropics/claude-code/issues/75571#issuecomment-4953755222), [comment 6](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5010217536), [comment 7](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5020941428), [comment 8](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5021099768), [comment 9](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5022855589), [comment 10](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5046905508), [comment 11](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5050479382), [comment 12](https://github.com/anthropics/claude-code/issues/75571#issuecomment-5052334037).

#### A254 — [Issue #51267](https://github.com/anthropics/claude-code/issues/51267)

> [BUG] Remote Control (mobile): session silently hangs mid-execution; only local Esc recovers it — no remote unstick mechanism

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-04-20T18:58:37Z; updated 2026-08-22T23:17:33Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/51267#issuecomment-4343457643).

#### A255 — [Issue #33949](https://github.com/anthropics/claude-code/issues/33949)

> SSE streaming hangs indefinitely (no timeout) + ESC cannot fully cancel (queue auto-restart) — root cause analysis with fix proposals

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-03-13T10:42:16Z; updated 2026-09-28T14:58:16Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4054235326), [comment 2](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4055585574), [comment 3](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4057370274), [comment 4](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4066392801), [comment 5](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4072218544), [comment 6](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4072726472), [comment 7](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4073653447), [comment 8](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4074109620), [comment 9](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4078969863), [comment 10](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4087883870), [comment 11](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4089022143), [comment 12](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4089141342), [comment 13](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4102410362), [comment 14](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4124459715), [comment 15](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4140277643), [comment 16](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4140610390), [comment 17](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4140967390), [comment 18](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4171151109), [comment 19](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4236712976), [comment 20](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4360697109), [comment 21](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4966022820).

#### A256 — [Issue #20380](https://github.com/anthropics/claude-code/issues/20380)

> [Bug] Claude Code hangs unresponsively on macOS M1, requires terminal force-close

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-23T15:16:21Z; updated 2026-04-02T16:10:49Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A257 — [Issue #19195](https://github.com/anthropics/claude-code/issues/19195)

> [BUG] Background task queue operations after completion signal cause session hang (stop_reason: null)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-19T08:09:21Z; updated 2026-02-23T18:41:00Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/19195#issuecomment-3946601319).

#### A258 — [Issue #19065](https://github.com/anthropics/claude-code/issues/19065)

> [Bug] Marketplace config JSON parsing hangs on empty files without error handling - cannot start claude when this happens

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-18T19:16:53Z; updated 2026-02-14T19:38:35Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A259 — [Issue #13290](https://github.com/anthropics/claude-code/issues/13290)

> [Bug] CLI hangs mid-conversation requiring session restart

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2025-12-07T09:28:33Z; updated 2026-03-05T13:39:37Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/13290#issuecomment-3734884008).

#### A263 — [Issue #20572](https://github.com/anthropics/claude-code/issues/20572)

> Claude Code freezes: static spinner, unresponsive input, ignores SIGTERM

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-01-24T12:07:13Z; updated 2026-04-20T19:21:37Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A280 — [Issue #99358](https://github.com/anthropics/claude-code/issues/99358)

> [BUG] Desktop Browser pane: auth handshake redirect chain back to http://localhost loops (ERR_TOO_MANY_REDIRECTS) — Clerk dev instances unusable on localhost

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-04T01:31:53Z; updated 2026-10-04T17:03:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A284 — [Issue #100354](https://github.com/anthropics/claude-code/issues/100354)

> [BUG] Cowork VM cannot start on Windows when the default Appx volume is a non-system drive (package data forced EFS)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-08T00:18:02Z; updated 2026-10-08T00:24:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/100354#issuecomment-6049570339).

#### A286 — [Issue #90205](https://github.com/anthropics/claude-code/issues/90205)

> change_directory cannot re-mount a session's original root directory after the session has moved away from it

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-27T20:28:44Z; updated 2026-10-11T05:11:09Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/90205#issuecomment-5444877995), [comment 2](https://github.com/anthropics/claude-code/issues/90205#issuecomment-5444955948).

#### A289 — [Issue #102670](https://github.com/anthropics/claude-code/issues/102670)

> [BUG] Cowork Linux workspace fails to start after update to 2.42304.0 (Windows ARM64): HCS 0x80370102 "required feature is not installed"

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-16T07:27:53Z; updated 2026-10-16T07:29:03Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A290 — [Issue #100218](https://github.com/anthropics/claude-code/issues/100218)

> [BUG] Desktop app session fails to start when working directory on SMB share contains accents (macOS 27, NFC vs NFD)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-07T12:50:52Z; updated 2026-10-07T12:55:40Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/100218#issuecomment-6038365180).

#### A291 — [Issue #93518](https://github.com/anthropics/claude-code/issues/93518)

> Claude Desktop MSIX (v1.52386.0): Workspace fails to start — VHDX not found + junction redirect rejected, even after clean reinstall

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-11T02:59:30Z; updated 2026-10-11T04:12:28Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

Follow-up context: [comment 1](https://github.com/anthropics/claude-code/issues/93518#issuecomment-6105325178).

#### A299 — [Issue #92419](https://github.com/anthropics/claude-code/issues/92419)

> [BUG] Edit/Write replace files via rename (new inode), so editor file watchers never fire — external changes invisible, then clobbered

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-06T02:26:48Z; updated 2026-10-21T14:04:46Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A302 — [Issue #91028](https://github.com/anthropics/claude-code/issues/91028)

> Bug Report: Linux sandbox fails to start on Windows 10 (RPC pipe closed) — MSIX identity detection bug

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-31T16:31:04Z; updated 2026-09-12T10:47:07Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A306 — [Issue #105361](https://github.com/anthropics/claude-code/issues/105361)

> [Bug] Chats crash when reading user-written agent instructions

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-27T07:46:13Z; updated 2026-10-27T07:47:24Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A307 — [Issue #105175](https://github.com/anthropics/claude-code/issues/105175)

> [BUG] [Windows] VS Code extension 2.1.310 crashes on startup with Bun segfault, even with config removed

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-26T11:51:16Z; updated 2026-10-26T11:53:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A308 — [Issue #98158](https://github.com/anthropics/claude-code/issues/98158)

> [BUG] Autocompact thrashing crashes subagent researching auto-compact behavior itself (invalid_request error)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-29T13:29:46Z; updated 2026-09-29T20:15:54Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A309 — [Issue #98119](https://github.com/anthropics/claude-code/issues/98119)

> [BUG] Background session daemon enters infinite crash-respawn loop when session process is stuck in kernel D-state (dead FUSE mount)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-29T10:54:27Z; updated 2026-09-29T10:55:27Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A310 — [Issue #96441](https://github.com/anthropics/claude-code/issues/96441)

> [BUG] Sessions list view crashes with TypeError in getAuthStatus when stored auth state is malformed

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-23T17:21:18Z; updated 2026-09-24T15:42:52Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A311 — [Issue #95646](https://github.com/anthropics/claude-code/issues/95646)

> [BUG] Cowork Windows: sandbox VM disk (rootfs.vhdx) hits a hard 10 GiB cap every 1–2 weeks and kills bash with

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-20T08:29:22Z; updated 2026-09-25T20:31:05Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A313 — [Issue #95825](https://github.com/anthropics/claude-code/issues/95825)

> [BUG] Claude in Chrome expanded scoped task authorization into an account-wide third-party setting change without fresh approval

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-21T11:57:56Z; updated 2026-09-21T11:59:08Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. No comments at metadata retrieval.

#### A334 — [Issue #91283](https://github.com/anthropics/claude-code/issues/91283)

> [BUG] Cowork /sessions never garbage-collects session directories (2,328 stale dirs, disk at 100%, unrecoverable from sandbox)

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-09-01T18:25:02Z; updated 2026-10-21T10:01:26Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A343 — [Issue #88072](https://github.com/anthropics/claude-code/issues/88072)

> [BUG] [BUG] Auto-updater blocks main process event loop — Claude Desktop becomes unresponsive on Windows

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-08-19T21:41:27Z; updated 2026-10-25T10:10:21Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.

#### A346 — [Issue #100254](https://github.com/anthropics/claude-code/issues/100254)

> [BUG] enabledMcpjsonServers in settings.json changes from an array to a string without notice, then fails validation ("Invalid settings")

Review the linked source for the environment, observed behavior and any reproduction steps. Attribution, prevalence, current-version status and independence from related reports remain unconfirmed.

Source snapshot: open; created 2026-10-07T15:52:26Z; updated 2026-10-08T09:01:29Z.

Evidence: Public reporter allegation; runtime behavior not independently reproduced. Follow-up comments fetched and screened for corrections/disposition.
