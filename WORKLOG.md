# Worklog — Practical Agent Skills

Plan and next action are owned by PROJECT_FOCUS.md. Mirror target: GitHub commits.

## 2026-09-10 · DOD-3 publication verified · Codex · mirror: synced
**Done:** Published the updated skill and two guides through GitHub's text editor. Public snapshot 06128d28575610f162b5fbc8039111387ddba77f matches all three reviewed files byte for byte. Both installed skill copies match SHA256 b76b9c05ded99fc1124d2f02e92b00fc5c2f2a706ffb6007addd3136a84f24b9. Structural validation, relative links, and ten-case author scenario review passed; no application E2E run is claimed.
**Learned:** Browser sign-in permits normal text editing even when extension-mediated file upload is unavailable. Readback establishes successful publication after transient UI waits. Seen before: yes.
**Went wrong:** Git CLI had no authentication or configured author identity, and the browser upload lacked extension file access. Used signed-in GitHub text editing without changing permissions or Git identity. One stale browser node and navigation timeout required fresh page inspection; no duplicate mutation was submitted.
**Next:** DONE: Share the updated skill and its verified GitHub publication.

## 2026-09-10 · DOD-1/DOD-2 and pre-publication · Codex · mirror: synced
**Done:** Reconciled newer installed E2E guidance, added an intended-flow contract and rule-derived adversarial checks, and updated both guides. Skill validator, relative links, ten-case author scenario review, and both local installation byte checks pass. Browser confirms repository ownership and editing access.
**Learned:** Green cases covered a preferred setup and a different input method while missing ordinary user paths. Requirements, exact entry points, and input methods must define coverage. Seen before: yes.
**Went wrong:** CLI publication lacked unattended authentication; user restored browser sign-in. Both Python runtimes lacked PyYAML; the validator dependency was installed in a temporary validation folder only. An initial patch context mismatch applied no edits; the corrected patch succeeded. Focus-state and whitespace checks caught drafting errors that were corrected. Browser upload was then blocked by extension file-URL access; no files were attached.
**Next:** BLOCKER: Enable browser extension file-URL access to publish the validated update for DOD-3.

## 2026-09-08 · DOD-3 publication verified · Codex · mirror: synced
**Done:** Published all four skill packages, five guides, and four original illustrations. At content snapshot cb2961a6e2c1e505ed29281a495ba63d746afd8d, all 29 public blobs match the prepared files. All four guides and PNGs return HTTP 200 without authentication; browser checks confirm the guide links and loaded images. Public URL: https://github.com/varut/practical-agent-skills.
**Learned:** GitHub supports nested upload targets even before the target folder exists. Its upload progress can outlast browser-tool waits, so an expired wait does not establish a failed upload. Seen before: yes.
**Went wrong:** Several browser waits expired while GitHub was still processing successful operations. Each operation was inspected before continuing; no duplicate publication was needed. System Python lacked a trusted certificate chain for the read check; curl completed it with normal TLS verification.
**Next:** DONE: Share the verified public collection URL; all three acceptance criteria are complete.

## 2026-09-08 · Publication resumes · Codex · mirror: pending
**Done:** User enabled browser-extension file access. The signed-in session confirms the empty public collection repository; the upload chooser is available.
**Learned:** A user-controlled extension permission is a prerequisite for this browser upload route. Seen before: yes.
**Went wrong:** No new failure; transport and publication still need verification.
**Next:** DOD-3: Publish the prepared collection and verify its public files and rendered guides.

## 2026-09-08 · DOD-1 and DOD-2 complete · Codex · mirror: pending
**Done:** Prepared four complete skill packages, five guides, artwork notes, and four reviewed original illustrations. All four skill validators pass; the guard passes 10 tests; relative links resolve; the privacy scan is clear. Final text review found an installer/manual-path mismatch, which is now explained in the guide.
**Learned:** The browser upload requires explicit extension file access. The connector's repository permissions did not guarantee its integration could write. Seen before: no.
**Went wrong:** Browser attachment returned Not allowed, connector writing returned 403, and the first multi-file document patch was rejected before applying; the corrected write completed successfully. One generated cartoon needed an anatomy correction.
**Next:** BLOCKER: Enable the browser extension's Allow access to file URLs setting so the prepared collection can be uploaded for DOD-3.

## 2026-09-08 · User expands collection scope · Codex · mirror: pending
**Done:** User authorized selecting other original skills and requested proper anonymous write-ups plus a funny image for each. The existing skill draft passed review but no files are published yet.
**Learned:** GitHub repository permission metadata did not establish connector write access; the actual contents write returned 403. Seen before: no.
**Went wrong:** Connector publication was rejected, so browser publication remains necessary.
**Next:** DOD-1: Audit skill provenance and select the original collection.

## 2026-09-08 · Publication transport recovery · Codex · mirror: pending
**Done:** The public repository now exists; the existing GitHub connector confirms the same owner and push access on main.
**Learned:** Browser file attachment was unavailable, while the existing repository connector supported the authorized write. Seen before: no.
**Went wrong:** The extension upload returned Not allowed, and native picker selection did not attach files. Switched to the existing connector after stopping those attempts.
**Next:** DOD-2: Publish the reviewed release files to GitHub.

## 2026-09-08 · DOD-1 and pre-publication · Codex · mirror: pending
**Done:** DOD-1 passed: source parity verified and independent review found no portability or instruction blockers. Prepared six Markdown files: skill, README, and required delivery records.
**Learned:** A standalone instruction skill needs no package dependencies, but recipients still need UI tools and suitable authorized test access. Seen before: no.
**Went wrong:** Nothing in the artifact review.
**Next:** DOD-2: Publish the reviewed release files to GitHub.

## 2026-09-08 · Release preparation · Codex · mirror: pending
**Done:** Located a single instruction-only skill file and verified a ZIP copy against its bytes. GitHub creation form confirms owner varut and Public visibility.
**Learned:** The installed discovery folder is a symlink; the release must contain the actual file. Seen before: no.
**Went wrong:** Nothing in release preparation; publication has not happened yet.
**Next:** DOD-1: Prepare and verify the unchanged skill and installation README.
