#---------------------------------------------------------------------------------------

# GitHub User Activity CLI

A simple command-line program built with Python that fetches and displays a GitHub user's recent activity using the GitHub API.

## Features

* Accepts a GitHub username through user input
* Fetches recent activity from the GitHub Events API
* Displays different types of GitHub activity in the terminal
* Formats GitHub timestamps into a more readable format
* Displays the number of commits associated with push events
* Handles HTTP errors gracefully
* Allows the user to try another username after an invalid username

## Technologies

* Python
* GitHub REST API
* `urllib`
* `json`
* `datetime`

No external libraries or frameworks are required.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/x-amarapro/Github-User-Activity-CLI.git
```

2. Navigate into the project directory:

```bash
cd Github-User-Activity-CLI
```

3. Run the program:

```bash
python main.py
```

4. Enter a GitHub username when prompted.

## Example

```text
Enter GitHub username: sindresorhus

sindresorhus pushed 4 commits to sindresorhus/awesome
sindresorhus starred sindresorhus/awesome
sindresorhus opened an issue in sindresorhus/...
```

## What I Practiced

This project was built to practice working with APIs and JSON data in Python. It also provided practice with:

* Making HTTP requests with `urllib`
* Parsing JSON responses
* Working with lists and dictionaries
* Accessing nested dictionary data
* Iterating through API results
* Conditional logic with `if`/`elif`
* Formatting dates and times
* Handling HTTP exceptions with `try`/`except`
* Using HTTP status codes to determine how the program should respond
* Working with the GitHub Compare API to determine commit counts

## Project Goal

This project was completed as part of my programming practice using the [Roadmap.sh GitHub User Activity project](https://roadmap.sh/projects/github-user-activity).

The goal was to build a functional CLI application while strengthening my understanding of APIs, JSON, Python control flow, and error handling.

#---------------------------------------------------------------------------------------