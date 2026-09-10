#--------------------------------------------------------------------------------------------

#Github User Activity CLI Program

#--------------------------------------------------------------------------------------------


#imports
import urllib.request
import json
from datetime import datetime


#--------------------------------------------------------------------------------------------


# { User Input for Github Username }

Github_Username = input("Enter Github username: ")


#--------------------------------------------------------------------------------------------


# { Github API Requests & Response }

Github_User_Activity_API = f"https://api.github.com/users/{Github_Username}/events"

Github_User_Activity_Response = urllib.request.urlopen(Github_User_Activity_API)

Github_User_Activity_Data = json.loads(Github_User_Activity_Response.read())

#print(Github_User_Activity_Data)


#--------------------------------------------------------------------------------------------


# { Formatted CLI Response }

for event in Github_User_Activity_Data[0:4]:
    if event['type'] == 'PushEvent':

        Github_Compare_API = f"https://api.github.com/repos/{event['repo']['name']}/compare/{event['payload']['before']}...{event['payload']['head']}"
        Github_Compare_Response = urllib.request.urlopen(Github_Compare_API)
        Github_Compare_Data = json.loads(Github_Compare_Response.read())

        Github_Compare_Commits = Github_Compare_Data['total_commits']

        print(
            f"{event['actor']['display_login']} "
            f"pushed {Github_Compare_Commits} commits to {event['repo']['name']} "
            f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
)

    elif event['type'] == 'CreateEvent':
        print(
            f"{event['actor']['display_login']} " 
            f"created a {event['payload']['ref_type']} "
            f"in {event['repo']['name']} "
            f"on {datetime.strptime(event['created_at'],'%Y-%m-%dT%H:%M:%SZ',).strftime('%B %d, %Y %H:%M:%S')}"
)




#--------------------------------------------------------------------------------------------

#clean simple CLI menu for user input and displayed activity

#--------------------------------------------------------------------------------------------