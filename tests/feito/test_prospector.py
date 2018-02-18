from unittest import TestCase
from unittest import mock

from feito import Prospector


class ProspectorTestCase(TestCase):

    @mock.patch('feito.prospector.Prospector')
    def test_run(self, repo_mock):
        repo_mock.repo.diff_files.return_value = 'tests/feito/fixtures/analyze_file.py'

        pros = Prospector(repo_mock.repo)
        analysis = pros.run()

        stub_analysis =  {
            'source': 'pep8',
            'code': 'E113',
            'location': {
                'path': 'tests/feito/fixtures/analyze_file.py',
                'module': None,
                'function': None,
                'line': 1, 'character': 5
            },
            'message': 'unexpected indentation'
          }

        assert stub_analysis in analysis['messages']
