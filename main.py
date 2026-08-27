#--------------------------------------------------------------------------------------------

#Github User Activity CLI Program

#--------------------------------------------------------------------------------------------

#imports
import urllib.request
import json

#--------------------------------------------------------------------------------------------

# { User Input for Github Username }

Github_Username = input("Enter Github username: ")

#--------------------------------------------------------------------------------------------

# { Github API Requests & Response }

Github_API_URL = f"https://api.github.com/users/{Github_Username}/events"

Response = urllib.request.urlopen(Github_API_URL)

Github_User_Activity_Data = json.loads(Response.read())

print(Github_User_Activity_Data)

#--------------------------------------------------------------------------------------------

#fetch Github user activity from Github API
   #return user data in JSON format

#display Github users recent activity in CLI
   #format user data for display in CLI

#clean simple CLI menu for user input and displayed activity

#--------------------------------------------------------------------------------------------
