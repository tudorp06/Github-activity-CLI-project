# github-activity CLI

Fetch and display a GitHub user's recent public activity. Built for roadmap.sh — Python, zero dependencies.

## Features
- `github-activity <username>` from anywhere (PATH + .bat wrapper)
- 6 event types: Push, Watch (star), Fork, Create, IssueComment, PullRequest
- Graceful errors: bad username, rate limit, offline (URLError)

## Requirements
- Python 3.x, no pip packages

## Install (Windows)
1. Clone, keep `script.py` + `github-activity.bat` together
2. Add that folder to PATH
3. New terminal → `github-activity torvalds`

## Usage
github-activity torvalds
github-activity this-user-does-not-exist-123
offline → "Network error - check your connection"

## How it works
- `urllib` + GitHub `/users/<name>/events`, User-Agent header
- PushEvent payloads often lack `commits` → prints generic "pushed": The Github API structure for retrieving a {username} list of events has changed, and now the payload no longer contains the number of commits, instead it documents changes, "before/after".
