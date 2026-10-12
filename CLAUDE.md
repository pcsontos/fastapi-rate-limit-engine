# Agent Context & Engineering Guidelines

## Objective
Build a production-grade, distributed rate limiting engine in Python (FastAPI + Redis)
supporting five pluggable rate-limiting algorithms:
Token Bucket, Leaking Bucket, Fixed Window, Sliding Window Log, and Sliding Window Counter.

## Standards & Tooling
- Package manager: uv (`uv add`, `uv run`)
- Lint & Format: `uv run ruff check .` and `uv run ruff format .`
- Static Type Checking: `uv run pyright` (strict mode, no untyped code, no `Any`)
- Runtime Validation: Pydantic v2 (`pydantic`, `pydantic-settings`)
- Tests: `uv run pytest -v tests/`
- Load Testing: `uv run locust -f tests/load/locustfile.py`

## Behavioral Constraints
1. **TDD:** Write unit/integration tests before writing implementation code.
2. **Separation of Concerns:** Keep core algorithms independent of FastAPI.
   FastAPI is merely the delivery mechanism / middleware adapter.
3. **Concurrency Safety:** Always assume high concurrent traffic; Redis operations
   must be atomic using Lua scripts.
4. **Git Hygiene (Strict):**
   - Use Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`).
   - Do not add `Co-Authored-By` trailers, session links, or "Generated with" footers to commits or pull requests.
   - Make small, incremental commits per feature/algorithm.
5. **No AI-Slop:**
   - Do not write obvious inline comments (`# Increment counter`). Only comment non-obvious architectural rationale (*why*, never *what*).
   - Do not use emojis in code, logs, docstrings, or documentation.
6. **Production Tone:** Frame all documentation, docstrings, and ADRs as a standalone,
   production-grade open-source engineering project.
7. **Phase-End Interview Defense Gate:** At the end of each development phase, act as a strict
   Senior Python & Distributed Systems Interviewer and quiz the developer on the implementation
   details, Python internals, and edge cases before proceeding to the next phase.
   - Read the phase's actual code, tests, and ADRs first; ask about that code, not generic trivia.
   - Ask one question at a time and wait for the answer. Give no hints and no solutions up front.
   - Probe shallow or wrong answers with follow-ups; reveal the correct answer only after closing the question.
   - Grade each question (solid / partial / missing). The phase closes only when nothing is missing.
   - Write the session record to the developer's private notes, not to this repo. Turn any
     undocumented decision or real defect found into an ADR, issue, or test here.

## Agent skills

### Issue tracker

Issues and specs live in this repo's GitHub Issues (`pcsontos/fastapi-rate-limit-engine`), managed with the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

The five canonical triage roles use their default label strings: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.
