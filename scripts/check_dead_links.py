#!/usr/bin/env python3
"""Report dead or moved GitHub links listed in awesome-japanese-nlp-resources.json.

Uses the GitHub REST API when GITHUB_TOKEN is set (recommended in CI; about
900 requests, well under the 1,000/hour GITHUB_TOKEN limit). Without a token
it falls back to HEAD requests against github.com.

The script only reports. It never edits the list, because README files are
generated from the JSON by the maintainer.

Usage:
  python scripts/check_dead_links.py [--output report.md]

Exit code: 1 when at least one link is missing (404) or blocked (451), else 0.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "awesome-japanese-nlp-resources.json"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
UA = "awesome-japanese-nlp-resources-link-check"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def load_entries():
    contents = json.loads(DATA.read_text(encoding="utf-8"))["contents"]
    entries = []
    for category, items in contents.items():
        for url in items:
            entries.append((category, url.rstrip("/")))
    return entries


def check_api(url):
    owner_repo = url.split("github.com/", 1)[1]
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner_repo}",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": UA,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code in (404, 451):
            return ("missing" if err.code == 404 else "blocked", str(err.code))
        return ("error", f"HTTP {err.code}")
    except Exception as err:  # network errors are reported, not fatal
        return ("error", type(err).__name__)
    new_url = data.get("html_url", "").rstrip("/")
    if new_url.lower() != url.lower():
        return ("moved", new_url)
    if data.get("archived"):
        return ("archived", "")
    return ("ok", "")


def check_head(url):
    opener = urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        opener.open(req, timeout=20)
        return ("ok", "")
    except urllib.error.HTTPError as err:
        if err.code in (301, 302):
            return ("moved", err.headers.get("Location", "").rstrip("/"))
        if err.code in (404, 451):
            return ("missing" if err.code == 404 else "blocked", str(err.code))
        return ("error", f"HTTP {err.code}")
    except Exception as err:
        return ("error", type(err).__name__)


def with_retry(check, url, attempts=4):
    """Retry rate limits (403/429), server errors, and network errors with backoff."""
    for i in range(attempts):
        status, detail = check(url)
        retryable = status == "error" and not detail.startswith("HTTP 4") or detail in ("HTTP 403", "HTTP 429")
        if not retryable or i == attempts - 1:
            return status, detail
        time.sleep(2 ** (i + 1))
    return status, detail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="write a Markdown report to this file")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    entries = load_entries()
    check = check_api if TOKEN else check_head
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda e: (e, with_retry(check, e[1])), entries))

    groups = {}
    for (category, url), (status, detail) in results:
        groups.setdefault(status, []).append((category, url, detail))

    titles = [
        ("missing", "Missing (404)", "Repository deleted or made private. Consider removing."),
        ("blocked", "Blocked (451)", "Unavailable for legal reasons. Consider removing."),
        ("moved", "Moved", "Repository renamed or transferred. Consider updating the URL."),
        ("archived", "Archived", "Still available but read-only. For information only."),
        ("error", "Could not check", "Temporary errors. Re-run before acting."),
    ]
    lines = [
        "# Dead link report",
        "",
        f"Checked {len(entries)} links in `awesome-japanese-nlp-resources.json` "
        f"({'GitHub API' if TOKEN else 'HEAD requests'}).",
        "",
    ]
    for key, title, note in titles:
        items = sorted(groups.get(key, []), key=lambda x: x[1].lower())
        lines.append(f"## {title}: {len(items)}")
        lines.append("")
        if items:
            lines.append(note)
            lines.append("")
            for category, url, detail in items:
                suffix = f" -> {detail}" if key == "moved" and detail else (f" ({detail})" if key == "error" else "")
                lines.append(f"- [{category}] {url}{suffix}")
            lines.append("")
    report = "\n".join(lines).rstrip() + "\n"
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    print(report)
    return 1 if groups.get("missing") or groups.get("blocked") else 0


if __name__ == "__main__":
    sys.exit(main())
