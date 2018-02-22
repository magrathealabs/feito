# Feito

Automated code review in Python done with Prospector

## Setting up

### 1) Requirements

A [Github OAuth Token](https://help.github.com/articles/git-automation-with-oauth-tokens/)

### 2) Setup environment

#### Environment variables

This lib is meant to be run in CI programs, not locally. However, this is still possible.
The following environment variables must be exported:

```
GITHUB_PR_ID (e.g., 1)
REPO_USERNAME (e.g. Michael)
TOKEN (Github OAuth Token)
```

Other variables, for example, `COMMIT_ID` and `REPO_NAME`, are optional because they can be fetched from the local development data. In CIs, like CircleCI, these 5 variables are avaliable without our need to configure them.

#### Dependencies

Download the dependencies with `pip install -r requirements.txt`

## Steps taken in Feito

Feito analysis is done with [Prospector](https://github.com/landscapeio/prospector). When `python run.py` is called, these are the actions taken:<br>
**1)** Gets the added, modified, renamed and copied files from the diff against the master branch.<br>
**2)** Filters the files by removing every non Python file.<br>
**3)** Runs Prospector on the Python files returned from the step above.<br>
**4)** Formats the returned Prospector analysis into a list of dictionaries containing the message, the line which triggered this review and the file path.<br>
**5)** Iterates throught this list and send a POST request for each dictionary, with its data properly formatted, that end up being the commit review message.


## Contributing

Make your modifications, run the tests with `pytest` and then open a PR.
