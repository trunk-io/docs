# Docs Backlog Processing Report
Generated: 2026-02-17

## Summary
14 PRs created across P1-P2 documentation backlog tickets. All Linear tickets moved to "In Review". Each PR requires manual review for accuracy before merging.

---

## P1: Quick Fixes

### PR #430 — Multi-branch merge queue docs
| | |
|---|---|
| **Branch** | `sam/document-multi-branch-merge-queues` |
| **PR** | https://github.com/trunk-io/docs/pull/430 |
| **Linear** | [TRUNK-17546](https://linear.app/trunk/issue/TRUNK-17546) — In Review |
| **Type** | new-feature |
| **Changes** | New `multi-branch-queues.md` page, FAQ correction in `common-problems.md`, cross-link in `advanced-settings.md` |
| **Review focus** | Verify multi-branch queue behavior matches product; confirm FAQ answer about multiple queues per repo |

### PR #431 — Fix codeowners link
| | |
|---|---|
| **Branch** | `sam/fix-codeowners-link` |
| **PR** | https://github.com/trunk-io/docs/pull/431 |
| **Linear** | [TRUNK-17095](https://linear.app/trunk/issue/TRUNK-17095) — In Review |
| **Type** | fix |
| **Changes** | Fixed broken CODEOWNERS link in `flaky-tests/dashboard.md`, added manual override note to `detection.md` |
| **Review focus** | Quick check — link fix and minor prose addition |

### PR #432 — Fix deprecated flakytests CLI refs
| | |
|---|---|
| **Branch** | `sam/fix-deprecated-flakytests-cli` |
| **PR** | https://github.com/trunk-io/docs/pull/432 |
| **Linear** | [TRUNK-17167](https://linear.app/trunk/issue/TRUNK-17167) — In Review |
| **Follow-up** | [TRUNK-17573](https://linear.app/trunk/issue/TRUNK-17573) — broader cleanup of remaining deprecated refs |
| **Type** | fix |
| **Changes** | Fixed 4 high-priority files: `jasmine.md`, `other-test-frameworks.md`, `otherci.md`, `uploader.md` |
| **Review focus** | Verify CLI command names match current product (`trunk flakytests` vs deprecated forms) |

---

## Draft-based Changes

### PR #433 — Merge queue graph UI docs
| | |
|---|---|
| **Branch** | `sam/merge-queue-graph-ui-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/433 |
| **Linear** | [TRUNK-17575](https://linear.app/trunk/issue/TRUNK-17575) — In Review |
| **Draft** | `.claude/drafts/new-merge-graph-ui.md` |
| **Type** | update |
| **Changes** | Rewrote `monitor-queue-status.md` with graph view UI details |
| **Review focus** | Verify UI descriptions match actual graph view; screenshots may be needed |

### PR #434 — Manual test status overrides
| | |
|---|---|
| **Branch** | `sam/flaky-test-manual-overrides` |
| **PR** | https://github.com/trunk-io/docs/pull/434 |
| **Linear** | [TRUNK-17576](https://linear.app/trunk/issue/TRUNK-17576) — In Review |
| **Draft** | `.claude/drafts/flaky-tests-rules-engine.md` |
| **Type** | update |
| **Changes** | Expanded manual override section in `detection.md` |
| **Review focus** | Confirm override behaviors and status options match product |

### PR #435 — Cypress junit plugin recommendation
| | |
|---|---|
| **Branch** | `sam/cypress-junit-plugin-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/435 |
| **Linear** | [TRUNK-17577](https://linear.app/trunk/issue/TRUNK-17577) — In Review |
| **Draft** | `.claude/drafts/falky-test-cyprus.md` |
| **Type** | update |
| **Changes** | Added `cypress-junit-plugin` recommendation to `cypress.md` |
| **Review focus** | Verify plugin name, install instructions, and config example |

### PR #436 — Bamboo CI provider docs
| | |
|---|---|
| **Branch** | `sam/bamboo-ci-provider-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/436 |
| **Linear** | [TRUNK-17578](https://linear.app/trunk/issue/TRUNK-17578) — In Review |
| **Draft** | `.claude/drafts/atlassian-bamboo.md` |
| **Type** | new-feature |
| **Changes** | New `bamboo.md` CI provider page, added to `summary.md` and CI providers include |
| **Review focus** | Verify Bamboo script task syntax and variable names match actual Bamboo CI |

### PR #437 — Concurrency settings clarification
| | |
|---|---|
| **Branch** | `sam/concurrency-settings-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/437 |
| **Linear** | [TRUNK-17579](https://linear.app/trunk/issue/TRUNK-17579) — In Review |
| **Draft** | `.claude/drafts/concurrency-settings.md` |
| **Type** | explainer |
| **Changes** | Clarified concurrency wording in `advanced-settings.md` and `batching.md` |
| **Review focus** | Confirm bisection concurrency behavior matches product |

### PR #438 — Google Cloud Build CI provider docs
| | |
|---|---|
| **Branch** | `sam/google-cloud-build-ci-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/438 |
| **Linear** | [TRUNK-17580](https://linear.app/trunk/issue/TRUNK-17580) — In Review |
| **Draft** | `.claude/drafts/google-cloud.md` |
| **Type** | new-feature |
| **Changes** | New `google-cloud-build.md` CI provider page, added to `summary.md` and CI providers include |
| **Review focus** | Verify GCB `cloudbuild.yaml` syntax, substitution variables, and `gcloud` commands |

### PR #439 — Merge Queue API reference improvements
| | |
|---|---|
| **Branch** | `sam/merge-queue-api-reference` |
| **PR** | https://github.com/trunk-io/docs/pull/439 |
| **Linear** | [TRUNK-17581](https://linear.app/trunk/issue/TRUNK-17581) — In Review |
| **Draft** | `.claude/drafts/merge-queue-api-endpoints.md` |
| **Type** | update |
| **Changes** | Rewrote `merge.md` API reference with curl examples |
| **Review focus** | Verify API endpoints, request/response schemas, and authentication method |

---

## P2: Backlog Tickets

### PR #440 — FAQ: missing repos in dropdown
| | |
|---|---|
| **Branch** | `sam/merge-faq-repo-not-in-dropdown` |
| **PR** | https://github.com/trunk-io/docs/pull/440 |
| **Linear** | [TRUNK-16724](https://linear.app/trunk/issue/TRUNK-16724) — In Review |
| **Sources** | `.claude/drafts/merge-faq-repo-dropdown.sources.md` |
| **Type** | explainer |
| **Changes** | New FAQ entry in `common-problems.md` about repos not appearing in dropdown |
| **Review focus** | Verify the troubleshooting steps match actual product behavior |

### PR #441 — SSO and Authentication docs
| | |
|---|---|
| **Branch** | `sam/improve-sso-login-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/441 |
| **Linear** | [TRUNK-16793](https://linear.app/trunk/issue/TRUNK-16793) — In Review |
| **Sources** | `.claude/drafts/sso-documentation.sources.md` |
| **Type** | new-feature |
| **Changes** | New `sso-and-authentication.md` page, cross-links from `connecting-to-trunk.md`, `managing-your-organization.md`, `billing.md` |
| **Review focus** | Confirm supported IdPs, SSO setup flow, and whether SSO-only enforcement is supported. This page is high-level since SSO is configured server-side — verify nothing is inaccurate. |

### PR #442 — GitHub IP allow list docs
| | |
|---|---|
| **Branch** | `sam/github-ip-allow-lists-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/442 |
| **Linear** | [TRUNK-16633](https://linear.app/trunk/issue/TRUNK-16633) — In Review |
| **Sources** | `.claude/drafts/github-ip-allowlist.sources.md` |
| **Type** | new-feature |
| **Changes** | New `github-ip-allow-lists.md` page, cross-reference from `github-app-permissions.md` |
| **Review focus** | **IP addresses are placeholders** — infra team must confirm actual IPs before merging. Watch the [Loom video](https://www.loom.com/share/9a3627f6ff264fbf8e11309c237efe0c) to verify steps. |

### PR #443 — Flaky Tests onboarding improvements
| | |
|---|---|
| **Branch** | `sam/improve-flaky-tests-onboarding-docs` |
| **PR** | https://github.com/trunk-io/docs/pull/443 |
| **Linear** | [TRUNK-16920](https://linear.app/trunk/issue/TRUNK-16920) — In Review |
| **Sources** | `.claude/drafts/flaky-tests-onboarding.sources.md` |
| **Type** | explainer |
| **Changes** | Rewrote Getting Started page, new `test-identification.md` page, enhanced `otherci.md` and `uploader.md` |
| **Review focus** | Confirm test identification explanation matches backend behavior (@eli/@gabe). Verify credential path in UI. Check env var callouts are accurate. |

---

## Review Checklist

- [ ] PR #430 — Multi-branch merge queues
- [ ] PR #431 — Codeowners link fix
- [ ] PR #432 — Deprecated CLI refs
- [ ] PR #433 — Graph UI docs
- [ ] PR #434 — Manual overrides
- [ ] PR #435 — Cypress plugin
- [ ] PR #436 — Bamboo CI
- [ ] PR #437 — Concurrency settings
- [ ] PR #438 — Google Cloud Build
- [ ] PR #439 — API reference
- [ ] PR #440 — FAQ repo dropdown
- [ ] PR #441 — SSO docs
- [ ] PR #442 — IP allow list (needs infra input)
- [ ] PR #443 — FT onboarding (needs eng input)
