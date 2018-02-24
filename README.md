# Feito

Automated code review in Python done with Prospector

## Setting up

Right now, Feito only supports GitHub.

### 1) Requirements

An account in GitHub must have its OAuth Token acquired. Follow this [link](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/#creating-a-token). When the Scopes section arrives, the `admin:repo_hook` and `repo` checkboxes must be selected. Copy the Token (really, copy it, you won't be able visualize after) and save it somewhere.

### 2) Setup environment

#### Environment variables

This lib is meant to be run in CI programs, not locally. However, this is still possible.
The following environment variables must be exported:

```
PULL_REQUEST_ID (e.g., 1)
REPOSITORY_USERNAME (e.g. Michael)
OAUTH_TOKEN (Github OAuth Token)
```

Other variables, for example, `COMMIT_ID` and `REPOSITORY_NAME`, are optional because they can be fetched from the local development data. In CIs, like CircleCI, these 5 variables are avaliable without our need to configure them.

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
