# AGENTS.md — Sovereign Governance & Validation Contract (`c5-socint-extraction-suite`)

## 1. Binary Validation Commands (Zero-Exploration Gate)
- **Static Linter (Fail-Closed):** `ruff check . -q`
- **Syntax & Import Verification:** `python3 -m py_compile *.py`
- **Test Runner:** `pytest -q`

## 2. Repository Invariants
- **Domain:** Omnivector Social Intelligence (SOCINT) & Forensic Extraction across 11 platforms with SQLite vault persistence.
- **Zero-Secret Invariant:** Never hardcode cookies, bearer tokens, or session credentials in source files; all secrets must be resolved via environment variables or macOS Keychain.
- **Language Invariant:** All public-facing documentation and commit messages must be in technical English.

## 3. Exploration Restrictions (`INV_C5_ARGON_GOVERNANCE`)
- Never read raw `.db`, `.sqlite`, `.jsonl` dumps, or `.venv/` directories into context.
- Inspect schema definitions only via `sqlite3 <db> ".schema"` or Python module headers.
