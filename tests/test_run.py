import os
from unittest import TestCase
from unittest import mock

import requests_mock

from tests.feito.support.prospector_analysis_stub_return import stub_return
import run as run_feito
from feito import Prospector


class RunTest(TestCase):

    @requests_mock.Mocker()
    @mock.patch.object(Prospector, 'run', return_value=stub_return)
    def test_run(self, mock_requ, _):
        self.__mock_github_api(mock_requ)

        run_feito.run()

        sent_data = [data.json() for data in mock_requ.request_history]

        assert sent_data == [{
            'body': 'pep8: unexpected indentation. Code: E113',
            'commit_id': '475348957349843957',
            'path': 'tests/feito/fixtures/analyze_file.py',
            'position': 1
        }, {
            'body': 'pylint: unexpected indent (<string>, line 1). Code: syntax-error',
            'commit_id': '475348957349843957',
            'path': 'tests/feito/fixtures/analyze_file.py',
            'position': 1
        }, {
            'body': 'pep8: expected an indented block. Code: E112',
            'commit_id': '475348957349843957',
            'path': 'tests/feito/fixtures/analyze_file.py',
            'position': 2
        }]

    def __mock_github_api(self, mock):
        github_api = 'https://api.github.com'
        user = os.getenv('REPOSITORY_USERNAME')
        repo = os.getenv('REPOSITORY_NAME')
        token = os.getenv('OAUTH_TOKEN')
        pr_id = os.getenv('PULL_REQUEST_ID')

        mock.post(
            f"{github_api}/repos/{user}/{repo}/pulls/{pr_id}/comments",
            request_headers={'authorization': f'token {token}'},
            json='ok'
        )
