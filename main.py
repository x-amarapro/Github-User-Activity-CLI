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

Github_API_URL = f"https://api.github.com/users/{Github_Username}/events"

Response = urllib.request.urlopen(Github_API_URL)

Github_User_Activity_Data = json.loads(Response.read())

#print(Github_User_Activity_Data)
#print(Github_User_Activity_Data[1]['payload'])

#for event in Github_User_Activity_Data:
#   print(event['type'])


#--------------------------------------------------------------------------------------------

# { Formatted CLI Response }

for event in Github_User_Activity_Data[0:2]:
    if event['type'] == 'PushEvent':
        print(
            f"{event['actor']['display_login']} "
            f"pushed to {event['repo']['name']} "
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