import sys
import json
import urllib.request, urllib.error

events = {
    'WatchEvent': ' starred ',
    'PushEvent': ' pushed in ',
    'CreateEvent': ' created ',
    'ForkEvent': ' forked ',
    'IssueCommentEvent':  ' added a comment to ',
    'PullRequestEvent': ' opened a pull request in '
}

def get_user(username: str):
    url = f"https://api.github.com/users/{username}/events"

    req = urllib.request.Request(url, headers={'User-Agent': 'Python-urllib', 'Accept': 'application/vnd.github+json'})
    try:
        with urllib.request.urlopen(req) as response:
            raw_data = response.read().decode("utf-8")
            data = json.loads(raw_data)
            return {"status": 200, "data": data}

    except urllib.error.HTTPError as e:
        error_data = json.loads(e.read().decode("utf-8"))
        message = error_data.get("message", "Unknown error") #either get real message from error response or chosen fallback
        return {'status': e.code, "data": message}
    except urllib.error.URLError:
        return {"status": 0, "data": "Network error - check your connection"}


def show_events(eventArray, username: str):
    if not eventArray:
        print(f"No recent activity for {username}")
        return
    
    for event in eventArray:
        display_event_message(username, event['type'], event['repo']['name'])

def display_event_message(username: str, event_type: str, repo_name: str):
    if event_type not in events:
         print(event_type + " doesn't exist!")
         return
    print(username + events[event_type] +  "repository: " + repo_name)

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[1].strip()!="":
        user_data = get_user(args[1])
        status = user_data["status"]
        event_data = user_data["data"]
        if status != 200:
            print(f"Something went wrong: {event_data}")
            sys.exit(1)
        show_events(event_data, args[1])
        sys.exit()
    print("github-activity <username>")
    sys.exit(1)


