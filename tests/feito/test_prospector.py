import os
import unittest


from feito import prospector


class ProspectorTestCase(unittest.TestCase):

    def test_run(self):
        code_analysis = prospector.run([os.getcwd() + '/tests/feito/fixtures/analyze_file.py'])
        stub_analysis = {
            'source': 'pylint',
            'code': 'syntax-error',
            'location': {
                'path': 'tests/feito/fixtures/analyze_file.py',
                'module': 'tests.feito.fixtures.analyze_file',
                'function': None,
                'line': 1,
                'character': 0
            },
            'message': 'unexpected indent (<string>, line 1)'
        }
        assert stub_analysis in code_analysis['messages']
