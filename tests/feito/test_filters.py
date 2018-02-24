from unittest import TestCase

from feito.filters import Filters


class FiltersTestCase(TestCase):

    def test_filter_python_files(self):
        files = ['test.py', 'test/another-test.py', 'not-python.rb', '.also-not-python']
        filtered_files = Filters.filter_python_files(files)

        assert filtered_files == ['test.py', 'test/another-test.py']
