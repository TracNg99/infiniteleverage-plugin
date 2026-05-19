#!/usr/bin/env python3
"""
Inject a compact token-usage briefing into Claude's context at SessionStart.
Reads ~/.claude/projects/ JSONL directly — no external tools, works offline.
Never raises — a failure here must never block the session.
"""
import json, os
from pathlib import Path
from datetime import datetime, timezone, timedelta

_PROJECTS = Path.home() / ".claude" / "projects"


def _sum_tokens(project_dir: Path, since: datetime) -> int:
    total = 0
    for f in project_dir.glob("*.jsonl"):
        try:
            for line in f.read_text(errors="ignore").splitlines():
                obj = json.loads(line)
                ts_raw = obj.get("timestamp", "")
                if not ts_raw:
                    continue
                ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                if ts >= since:
                    u = obj.get("usage", {})
                    total += u.get("input_tokens", 0) + u.get("output_tokens", 0)
        except Exception:
            pass
    return total


def main() -> None:
    cwd = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    slug = cwd.replace("/", "-")   # ~/.claude/projects/ uses this encoding
    now = datetime.now(timezone.utc)
    project_dir = _PROJECTS / slug

    session = _sum_tokens(project_dir, now - timedelta(hours=1)) if project_dir.exists() else 0
    daily   = _sum_tokens(project_dir, now - timedelta(hours=24)) if project_dir.exists() else 0
    weekly  = _sum_tokens(project_dir, now - timedelta(days=7)) if project_dir.exists() else 0

    # Weekly comparison across all active projects
    all_weekly: dict[str, int] = {}
    if _PROJECTS.exists():
        for p in _PROJECTS.iterdir():
            if p.is_dir():
                t = _sum_tokens(p, now - timedelta(days=7))
                if t > 0:
                    all_weekly[p.name] = t

    name = Path(cwd).name
    parts = [
        f"[Usage: /{name} — "
        f"session {session:,}t · today {daily:,}t · week {weekly:,}t."
    ]

    if len(all_weekly) > 1:
        top = sorted(all_weekly.items(), key=lambda x: x[1], reverse=True)[:3]
        top_str = " · ".join(f"{p.split('-')[-1]} {v:,}t" for p, v in top)
        parts.append(f" Top this week: {top_str}.")

    if daily > 50_000:
        parts.append(" High daily usage — consider /compact to manage context window.")

    parts.append("]")
    print("".join(parts))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
