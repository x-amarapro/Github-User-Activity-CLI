#--------------------------------------------------------------------------------------------

# { Github User Activity CLI Program }

#--------------------------------------------------------------------------------------------


#imports
import urllib.request
import json
from datetime import datetime


#--------------------------------------------------------------------------------------------


# { User Input for Github Username }

program_running = True

while program_running:
    Github_Username = input("Enter Github username: ")

# { Github API Requests & Response }

    Github_User_Activity_API = f"https://api.github.com/users/{Github_Username}/events"

    try:
        Github_User_Activity_Response = urllib.request.urlopen(Github_User_Activity_API)

    except urllib.error.HTTPError:
        print(f"Error: User \"{Github_Username}\" not found. Please try again.")
        continue

    Github_User_Activity_Data = json.loads(Github_User_Activity_Response.read())

    #print(Github_User_Activity_Data)

# { Formatted CLI Response }

    for event in Github_User_Activity_Data:
        if event['type'] == 'PushEvent':

            Github_Compare_API = f"https://api.github.com/repos/{event['repo']['name']}/compare/{event['payload']['before']}...{event['payload']['head']}"
            Github_Compare_Response = urllib.request.urlopen(Github_Compare_API)
            Github_Compare_Data = json.loads(Github_Compare_Response.read())
            Github_Compare_Commits = Github_Compare_Data['total_commits']

            if Github_Compare_Commits == 1:
                print(
                    f"{event['actor']['display_login']} "
                    f"pushed {Github_Compare_Commits} commit to {event['repo']['name']} "
                    f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
                )

            else:
                print(
                    f"{event['actor']['display_login']} "
                    f"pushed {Github_Compare_Commits} commits to {event['repo']['name']} "
                    f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
                )

        elif event['type'] == 'PullRequestEvent':
            print(
                f"{event['actor']['display_login']} "
                f"{event['payload']['action']} a pull request in {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'CreateEvent':
            print(
                f"{event['actor']['display_login']} " 
                f"created a {event['payload']['ref_type']} "
                f"in {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'DeleteEvent':
            print(
                f"{event['actor']['display_login']} " 
                f"deleted a {event['payload']['ref_type']} "
                f"in {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'IssueEvent':
            print(
                f"{event['actor']['display_login']} "
                f"{event['payload']['action']} an issue in {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'ForkEvent':
            print(
                f"{event['actor']['display_login']} "
                f"forked {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'WatchEvent':
            print(
                f"{event['actor']['display_login']} "
                f"starred {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'MemberEvent':
            print(
                f"{event['actor']['display_login']} "
                f"added {event['payload']['member']['login']} as a collaborator to {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

        elif event['type'] == 'ReleaseEvent':
            print(
                f"{event['actor']['display_login']} "
                f"published a release in {event['repo']['name']} "
                f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
            )

#--------------------------------------------------------------------------------------------



