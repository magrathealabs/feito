[![CircleCI](https://circleci.com/gh/magrathealabs/feito.svg?style=shield&circle-token=7ca1c63859e4f72f377a16e2e2f817e1b097c919)](https://circleci.com/gh/magrathealabs/feito)
<a href="https://codeclimate.com/github/magrathealabs/feito/maintainability"><img src="https://api.codeclimate.com/v1/badges/57b6a6aab2f6c67de971/maintainability" /></a>
[![PyPI version](https://badge.fury.io/py/feito.svg)](https://badge.fury.io/py/feito)
[![code review by feito](https://img.shields.io/badge/code%20review%20by-feito-blue.svg)](https://github.com/magrathealabs/feito)

# Feito

Automated code review in Python done with Prospector

## Setting up

Right now, Feito only supports GitHub.

### Installation

`$ pip install feito`

### Requirements for usage

In order to have an account to comment as Feito in your PRs, a GitHub OAuth Token must be acquired. Follow this [link](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/#creating-a-token). When the Scopes section arrives, the `admin:repo_hook` and `repo` checkboxes must be selected. Copy the Token (really, copy it, you won't be able to visualize it afterward) and save it somewhere.

### Setting environment variables

#### Locally

This lib is meant to be run in CI programs, not locally, as a mean to automate code lintage. However, this is still possible.
The following environment variables must be exported:

```sh
PULL_REQUEST_ID (e.g., 1)
REPOSITORY_USERNAME (e.g. magrathealabs)
OAUTH_TOKEN (Github OAuth Token)
COMMIT_ID (e.g. 08a943e797af4121c1e809d3b2288bbd70dcb0b7)
REPOSITORY_NAME (e.g. feito)
```

#### In CIs

In CircleCI, your `circle.yml` (v1.0) or `.circleci/config.yml` (v2.0) file can be modified with the following code:

```sh
export PULL_REQUEST_ID=`echo $CIRCLE_PULL_REQUEST | grep -o -E '[0-9]+'`
export REPOSITORY_NAME=${CIRCLE_PROJECT_REPONAME}
export REPOSITORY_USERNAME=${CIRCLE_PROJECT_USERNAME}
export COMMIT_ID=${CIRCLE_SHA1}
feito
```

The `OAUTH_TOKEN` was set in Circle's own area for environment variables, and therefore does not need to be exported in the configuration file.

For more insight, check out this project's `.circleci/config.yml`.


### Usage

After exporting the environment variables above, execute `feito`. In a few moments, the analysis done by Prospector will be shown in your PR

## Steps taken in Feito

Feito analysis is done with [Prospector](https://github.com/landscapeio/prospector). When `python run.py` is called, these are the actions taken:<br>
**1)** Gets the added, modified, renamed and copied files from the diff against the master branch.<br>
**2)** Filters the files by removing every non Python file.<br>
**3)** Runs Prospector on the Python files returned from the step above.<br>
**4)** Formats the returned Prospector analysis into a list of dictionaries containing the message, the line which triggered this review and the file path.<br>
**5)** Iterates throught this list and send a POST request for each dictionary, with its data properly formatted, that end up being the commit review message.


## Badge

Show the world you're using Feito! Add the badge code review by feito to your project.

[![code review by feito](https://img.shields.io/badge/code%20review%20by-feito-blue.svg)](https://github.com/magrathealabs/feito)

## License

The package is available as open source under the terms of the MIT License.


## Contributing

Make your modifications, run the tests with `pytest` and then open a PR.
