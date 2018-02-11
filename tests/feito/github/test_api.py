import unittest

import requests_mock

from feito.github import API


class APITestCase(unittest.TestCase):
    GITHUB_API_URL = 'https://api.github.com'

    @requests_mock.Mocker()
    def test_create_comment_commit(self, mock):
        user = 'spencerWilliams'
        repo = 'basin-street-blues'
        token = 'knfw784t9jg573h'
        mock.post(
            f"{self.GITHUB_API_URL}/repos/{user}/{repo}/pulls/1/comments",
            request_headers={'authorization': f'token {token}'}
        )

        api = API(user, repo, token)
        api.create_comment_commit(
            body='That sax is gold',
            commit_id='bb6a298654dd59dd6e4feb087d13b81778e6e565',
            path='file_actions.py',
            position=1,
            pr_id=1
        )

        assert mock.called == True
        assert mock.last_request.json() == {
            'body': 'That sax is gold',
            'commit_id': 'bb6a298654dd59dd6e4feb087d13b81778e6e565',
            'path': 'file_actions.py',
            'position': 1
        }
