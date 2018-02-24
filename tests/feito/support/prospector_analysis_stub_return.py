stub_return = {
    'summary': {
        'started': '2018-02-14 09:46:02.106964',
        'libraries': [],
        'strictness': None,
        'profiles': 'default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings',
        'tools': [
            'dodgy', 'mccabe', 'pep8', 'profile-validator', 'pyflakes', 'pylint'
        ],
        'message_count': 3,
        'completed': '2018-02-14 09:46:02.182521',
        'time_taken': '0.08',
        'formatter': 'json'
    },
    'messages': [{
        'source': 'pep8',
        'code': 'E113',
        'location': {
            'path': 'tests/feito/fixtures/analyze_file.py',
            'module': None,
            'function': None,
            'line': 1,
            'character': 5
        },
      'message': 'unexpected indentation'
    }, {
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
    }, {
      'source': 'pep8',
      'code': 'E112',
      'location': {
          'path': 'tests/feito/fixtures/analyze_file.py',
          'module': None,
          'function': None,
          'line': 2,
          'character': 5
      },
      'message': 'expected an indented block'
  }]
}
