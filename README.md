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
