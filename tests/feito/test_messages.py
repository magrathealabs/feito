from unittest import TestCase

from feito import Messages


class MessagesTestCase(TestCase):

    def test_format(self):
        stub_messages = {
            'messages': [{
                'source': 'pylint',
                'code': 'syntax-error',
                'location': {
                    'path': 'tests/feito/fixtures/analyze_file.py',
                    'module': 'tests.feito.fixtures.analyze_file',
                    'function': None,
                    'line': 1,
                    'character': 0
                },
                'message': 'unexpected indent (<string>, line 1)',
            },{
                'source': 'pylint',
                'code': 'too-many-arguments',
                'location': {
                    'path': 'feito/github/api.py',
                    'module': 'feito.github.api',
                    'function': 'API.create_comment_commit',
                    'line': 25,
                    'character': 4
                },
                'message': 'Too many arguments (6/5)'
            }]
        }

        formatted_messages = Messages(stub_messages).commit_format()

        assert formatted_messages == [{
            'message': 'pylint: unexpected indent (<string>, line 1). Code: syntax-error',
            'file': 'tests/feito/fixtures/analyze_file.py',
            'line': 1
        },{
            'message': 'pylint: Too many arguments (6/5). Code: too-many-arguments',
            'file': 'feito/github/api.py',
            'line': 25
        }]
