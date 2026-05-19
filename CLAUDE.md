# Infinite Leverage — 8-Agent Team Active

This session has the Infinite Leverage plugin loaded. An 8-agent specialist team is available. Route work to the right agent using the trigger phrases below — or tag explicitly with `@agent-name`.

## Agent Routing

### Dev Team

| Trigger phrase | Agent | Skill |
|---|---|---|
| "plan", "spec", "write an epic", "acceptance criteria" | @product-manager | — |
| "create issues", "break into tickets", "to issues" | @product-manager | `pm-to-issues` |
| "validate plan", "check against epics", "grill with docs" | @product-manager | `pm-grill-with-docs` |
| "build", "implement", "code this", "write the function" | @developer | — |
| "debug", "why is this broken", "diagnose" | @developer | `dev-diagnose` |
| "zoom out", "give me context on this module" | @developer | `dev-zoom-out` |
| "grill me", "stress-test this plan", "what could go wrong" | @developer | `dev-grill` |
| "tdd", "test-driven", "red-green-refactor" | @developer | `dev-tdd` |
| "spike", "prototype", "is this feasible" | @developer | `dev-prototype` |
| "improve architecture", "refactor this module", "tech debt" | @developer | `dev-improve-arch` |
| "handoff", "wrapping up", "passing to QA" | @developer | `dev-handoff` |
| "triage", "classify this bug", "prioritise this bug" | @qa | `qa-triage` |
| "test strategy", "what to test", "test plan" | @qa | `qa-best-practices` |
| "ci/cd", "pipeline", "github actions" | @devops | — |
| "pre-commit", "husky", "lint-staged" | @devops | `devops-setup-pre-commit` |
| "git hooks", "protect main", "guardrails" | @devops | `devops-git-guardrails` |

### Marketing Team

| Trigger phrase | Agent | Skill |
|---|---|---|
| "marketing strategy", "new campaign", "client brief" | @writer | `marketing-strategist` |
| "write a post", "draft content", "blog post" | @writer | — |
| "seo", "meta description", "keyword research" | @writer | `writer-seo-content` |
| "social post", "instagram caption", "linkedin post" | @writer | — |
| "generate image", "hero image", "create a visual" | @designer | `designer-image-generation` |
| "design system", "brand tokens", "colour palette" | @designer | `designer-design-system` |
| "mockup", "wireframe", "ui design" | @designer | `designer-ui-ux` |
| "publish", "build the page", "push to site" | @web-publisher | `web-publisher-publish` |
| "email campaign", "newsletter", "send to subscribers" | @email-marketer | `email-marketer-nurture` |

## Hard Rules (cannot be overridden)

1. **Developer never starts without an approved PM plan.** Route to PM first if no plan exists.
2. **QA never skips triage.** Every bug is classified before being assigned.
3. **DevOps never deploys directly.** All deployments go through `git push` → CI/CD.
4. **Web Publisher never pushes to GitHub.** Commits locally — operator runs `git push`.
5. **Email Marketer never sends without operator approval.** All campaigns are drafted only.
6. **No agent merges its own PR.** Developer opens → QA verifies → operator merges.
7. **Designer generates images only after copy is approved.**

## Setup

If you haven't set up the 8-agent team yet, run `/infiniteleverage-init`.
If you're onboarding a new project, run `/infiniteleverage-onboard`.
If the template has a newer version, run `/infiniteleverage-patch`.
