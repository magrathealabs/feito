import requests


class API:
    GITHUB_API_URL = 'https://api.github.com'

    # TODO: Add username and password authentication methods
    def __init__(self, user, repo, token=None, password=None):
        """
        param user: str -> Github username
        param token: str -> Github oauth token
        param repo: str -> Github repository name
        param password: str -> Github user password
        """
        self.user = user
        self.repo = repo
        self.token = token
        self.password = password

        if token:
            self.auth_header = {'authorization': f'token {token}'}

    def create_comment_commit(self, body, commit_id, path, position, pr_id):
        """
        Posts a comment to a given commit at a certain pull request.
        Check https://developer.github.com/v3/pulls/comments/#create-a-comment

        param body: str -> Comment text
        param commit_id: str -> SHA of the commit
        param path: str -> Relative path of the file to be commented
        param position: int -> The position in the diff to add a review comment
        param pr_id: int -> Github pull request id
        """
        comments_url = f"{self.GITHUB_API_URL}/repos/{self.user}/{self.repo}/pulls/{pr_id}/comments"
        data = {'body': body, 'commit_id': commit_id, 'path': path, 'position': position}

        return requests.post(comments_url, json=data, headers=self.auth_header)
