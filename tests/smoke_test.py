#!/usr/bin/env python3
"""Structural smoke tests for the security-agents-bundle catalog.

Validates that every agent and skill is well-formed and installable, that catalog
install paths resolve, and that internal links are not broken. Deterministic; no
model calls. Exit non-zero on any failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILS: list[str] = []
CHECKS = 0

VALID_MODELS = {
    "inherit", "opus", "sonnet", "haiku", "fable",
}


def check(cond: bool, msg: str) -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILS.append(msg)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    body = text[3:end].strip("\n")
    out: dict[str, str] = {}
    for line in body.splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip()
    return out


def valid_model(val: str) -> bool:
    val = val.strip()
    return val in VALID_MODELS or val.startswith("claude-")


def check_agents() -> None:
    for f in sorted((ROOT / "agents").glob("*.md")):
        text = f.read_text()
        fm = parse_frontmatter(text)
        check(fm is not None, f"{f.name}: missing/invalid frontmatter")
        if fm is None:
            continue
        check(fm.get("name") == f.stem, f"{f.name}: name '{fm.get('name')}' != filename '{f.stem}'")
        check(bool(fm.get("description")), f"{f.name}: empty description")
        check(len(fm.get("description", "")) <= 1536, f"{f.name}: description over 1536 chars")
        check("model" in fm and valid_model(fm["model"]), f"{f.name}: invalid model '{fm.get('model')}'")
        check("tools" in fm, f"{f.name}: missing tools allowlist")
        # every reviewer in this bundle is read-only by construction
        dt = fm.get("disallowedTools", "")
        check("Write" in dt and "Edit" in dt, f"{f.name}: reviewer must disallow Write and Edit")


def check_skills() -> None:
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir():
            continue
        sk = d / "SKILL.md"
        check(sk.exists(), f"skills/{d.name}: missing SKILL.md")
        if not sk.exists():
            continue
        fm = parse_frontmatter(sk.read_text())
        check(fm is not None, f"skills/{d.name}/SKILL.md: missing/invalid frontmatter")
        if fm is None:
            continue
        check(fm.get("name") == d.name, f"skills/{d.name}: name '{fm.get('name')}' != dir '{d.name}'")
        check(bool(fm.get("description")), f"skills/{d.name}: empty description")
        check("when_to_use" in fm, f"skills/{d.name}: missing when_to_use")
        check(fm.get("license") == "MIT", f"skills/{d.name}: license should be MIT")


def check_install_paths() -> None:
    for f in sorted((ROOT / "catalog").glob("*.md")):
        for m in re.finditer(r"Install: `([^`]+)`", f.read_text()):
            target = ROOT / m.group(1)
            check(target.exists(), f"{f.name}: Install path '{m.group(1)}' does not exist")


def check_internal_links() -> None:
    for f in sorted(ROOT.rglob("*.md")):
        for m in re.finditer(r"\]\((?!https?://)([^)#]+)(?:#[^)]*)?\)", f.read_text()):
            rel = m.group(1)
            if not rel or rel.startswith("<"):
                continue
            target = (f.parent / rel).resolve()
            check(target.exists(), f"{f.relative_to(ROOT)}: broken link '{rel}'")


def main() -> int:
    check_agents()
    check_skills()
    check_install_paths()
    check_internal_links()
    if FAILS:
        print(f"FAIL — {len(FAILS)} of {CHECKS} checks failed:\n")
        for m in FAILS:
            print(f"  ✗ {m}")
        return 1
    print(f"PASS — {CHECKS} checks green across {len(list((ROOT / 'agents').glob('*.md')))} agents "
          f"and {len([d for d in (ROOT / 'skills').iterdir() if d.is_dir()])} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
