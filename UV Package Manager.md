




1
UV Package Manager
**uv — What It Is**

A fast Python package and project manager written in Rust by Astral (the same company behind the Ruff linter). Replaces pip, pip-tools, pipx, poetry, pyenv, virtualenv, and twine with a single tool. 10–100x faster than pip due to its Rust implementation and aggressive caching.




2
UV Package Manager
**Why Rust for Python tooling?**

Python is interpreted and slow for CPU-bound work like dependency resolution and file I/O at scale. Rust gives compiled-language performance, predictable memory use, and parallel-friendly concurrency. Astral's bet (uv + Ruff) is that the developer experience tools should be fast even if the language they serve isn't.




3
UV Package Manager
**Lockfile — The Core Concept**

A lockfile pins **exact versions** and **cryptographic hashes** for every dependency (direct *and* transitive) so the same code installs identically across machines and over time. It solves "works on my machine" by freezing a known-good resolution. Commit it to git for applications.




4
UV Package Manager
**`uv.lock` vs. `pyproject.toml`**

- **`pyproject.toml`** — declares *intent*: version ranges (`fastapi>=0.110`), edited by humans.
- **`uv.lock`** — captures *resolution*: exact versions (`fastapi==0.121.1`) plus SHA256 hashes for every package and platform-specific wheel. Generated and edited by uv.





5
UV Package Manager
Application Lockfile vs. Library Version Constraints

The single most important packaging distinction:
- Applications (deployable services, CLIs) — pin exact versions in a lockfile. You control the deploy environment, you want determinism. Commit `uv.lock`.
- Libraries (published to PyPI for others) — declare version ranges so consumers can resolve their own combination. Pinning exact versions in a library makes it impossible to combine with other libraries. Don't ship `uv.lock` with a library.




6
UV Package Manager
Dependency Resolution — Why It's Hard

Finding a set of package versions that satisfies all constraints simultaneously is formally equivalent to SAT (boolean satisfiability) — NP-hard in the general case. That's why old pip was slow or gave up. Modern resolvers (uv uses PubGrub) handle it with smart backtracking. The hard part isn't downloading packages — it's the math.





7
UV Package Manager
Direct vs. Transitive Dependencies

- Direct — packages your project explicitly lists (e.g., `fastapi` in `pyproject.toml`).
- Transitive — dependencies of your dependencies (e.g., `starlette`, `pydantic` pulled in by `fastapi`). The lockfile pins both; `pyproject.toml` only declares direct ones.





8
UV Package Manager
Global Cache (Hard-Links)

uv stores each unique package version once on disk in a global cache, then uses hard-links to make it appear inside each project's `.venv`. Ten projects depending on `numpy 2.1.0` = one copy on disk, not ten. Same disk-space-efficiency idea as pnpm in JavaScript.





9
UV Package Manager
PEP 621 — Why Standardization Matters

PEP 621 defines the standard `[project]` table in `pyproject.toml`. Before it, every tool (poetry, flit, setuptools) used its own custom table. The standard means you can switch tools (poetry → uv) without rewriting metadata. Interoperability, not performance.





10
UV Package Manager
PEP 735 — Dependency Groups

The standardized table for dev/test/optional dependency sets:

```toml
[dependency-groups]
dev = ["ruff>=0.5"]   # synced by default
test = ["pytest>=8"]
```

Different from `[project.optional-dependencies]`, which is for "extras" consumers opt into when installing your published package.




11
UV Package Manager
`uv add` vs. `uv pip install`

- `uv add <pkg>` — project-level. Edits `pyproject.toml`, updates `uv.lock`, installs. The package is *declared* as a project dependency. Atomic.
- `uv pip install <pkg>` — environment-level. Just installs into the venv. Doesn't touch project metadata. Mirrors classic pip behavior, useful for ad-hoc installs and legacy workflows.

Rule: declare with `uv add`, hack with `uv pip install`.




12
UV Package Manager
`uv add` vs. `uv tool install`

- `uv add ruff` — adds Ruff as a dependency of *the current project*.
- `uv tool install ruff` — installs Ruff globally into uv's isolated tool cache, available everywhere. Equivalent to `pipx install`.

Use `uv tool install` for CLI utilities (ruff, black, mypy) you want available outside any specific project. `uvx <tool>` is the shortcut for one-off runs.




13
UV Package Manager
`uv run` — What It Actually Does

`uv run <cmd>` does three things automatically: (1) locks if needed, (2) syncs the env, (3) executes the command with the right Python and dependencies on PATH. Replaces `source .venv/bin/activate && python ...` with one command.




14
UV Package Manager
`uv sync` — "Exact" by Default

Default behavior is *exact*: any package in the venv that's not in the lockfile gets removed. So if you `uv pip install something` manually, then run `uv sync`, that package is uninstalled. Use `--inexact` to keep extraneous packages. (Counter-intuitively, `uv run` uses inexact syncing by default.)




15
UV Package Manager
`--locked` vs. `--frozen` vs. `--no-sync`

| Flag | Behavior | When to use |
|------|----------|-------------|
| `--locked` | Error if lockfile is stale; do not update it | CI builds — strictest |
| `--frozen` | Use lockfile as-is; skip the staleness check | Trust the lockfile, want speed |
| `--no-sync` | Skip installing/updating env entirely | Just run, don't touch deps |

Mnemonic: locked = strict, frozen = trust, no-sync = skip.




16
UV Package Manager
Targeted Upgrade — `uv lock --upgrade-package <pkg>`

Re-resolves only the named package (and its transitive deps if needed) to the latest compatible version. All other locked versions stay put. Compare to `uv lock --upgrade` (no package) — upgrades everything. Targeted upgrades are the safer pattern for security patches.




17
UV Package Manager
`.python-version`

Created by `uv python pin 3.12`. Same convention as pyenv, so it's portable across tools. uv installs and manages standalone Python builds independent of the system Python — meaning uv can use Python 3.12 even if your OS only has 3.9.





18
UV Package Manager
Why Virtual Environments Exist

To isolate per-project dependencies. Without a venv, `pip install` modifies the system-wide Python, causing version conflicts between projects ("project A needs Django 4, project B needs Django 5"). A venv is just a directory with its own Python interpreter and `site-packages`. uv creates them automatically — no manual `python -m venv` step.





19
UV Package Manager
Wheels (`.whl`) vs. Source Distributions (`.sdist`)

- Wheel — pre-built binary distribution. Installs by unpacking, no compilation. Fast.
- Sdist — source archive. May require a compiler (especially for C extensions). Slow.

Lockfiles list both, plus platform-specific wheels (`manylinux`, `macosx_arm64`, `win_amd64`) so the right binary is selected per machine without rebuilding.





20
UV Package Manager
Reproducibility — The Goal

Same code → same behavior, across machines, environments, and time. Achieved by combining: a lockfile (exact versions), cryptographic hashes (verify integrity), platform-specific wheels (no surprise compilation), and tools that respect those constraints (`uv sync --locked`). Without reproducibility, debugging deploys becomes guesswork.





21
UV Package Manager
The Big Picture — uv as Consolidation

Python historically required juggling: `pyenv` (Python versions), `virtualenv` (envs), `pip` (install), `pip-tools` (lockfiles), `pipx` (CLI tools), `poetry` (project mgmt), `twine` (publish). Each with its own config and quirks. uv collapses all of it into one binary with one mental model. Same trend Cargo brought to Rust and npm/pnpm brought to JavaScript — Python is catching up.




22
UV Package Manager
CI/CD Pattern (Memorize)

```bash
uv sync --locked          # strict install — error if lockfile stale
uv run pytest             # run tests in the synced env
uv lock --check           # verify lockfile current with pyproject.toml
```

Pre-commit hook to run `uv lock --check` on changes to `pyproject.toml` keeps the lockfile honest locally too.




23
UV Package Manager





24
UV Package Manager





25
UV Package Manager





26
UV Package Manager





27
UV Package Manager





28
UV Package Manager





29
UV Package Manager





30
UV Package Manager





31
UV Package Manager





32
UV Package Manager





33
UV Package Manager





34
UV Package Manager





35
UV Package Manager





36
UV Package Manager





37
UV Package Manager





38
UV Package Manager





39
UV Package Manager





40
UV Package Manager





41
UV Package Manager





42
UV Package Manager





43
UV Package Manager





44
UV Package Manager





45
UV Package Manager





46
UV Package Manager





47
UV Package Manager





48
UV Package Manager





49
UV Package Manager





50
UV Package Manager





