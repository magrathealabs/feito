import os

from unittest.mock import Mock
from unittest import TestCase

from feito import Filters


class FiltersTestCase(TestCase):

    def test_filter_python_files(self):
        files = ['test.py', 'test/another-test.py', 'not-python.rb', '.also-not-python']
        filtered_files = Filters.filter_python_files(files)

        assert filtered_files == ['test.py', 'test/another-test.py']

    def test_filter_diff_files(self):
        added_file = Mock()
        added_file.change_type = 'A'
        added_file.b_path = 'added.py'
        modified_file = Mock()
        modified_file.change_type = 'M'
        modified_file.b_path = 'modified.py'
        removed_file = Mock()
        removed_file.change_type = 'R'
        removed_file.b_path = 'renamed.py'
        deleted_file = Mock()
        deleted_file.change_type = 'D'
        deleted_file.b_path = 'deleted.py'
        diff_files = [added_file, modified_file, removed_file, deleted_file]

        filtered_files = Filters.filter_diff_files(diff_files)

        assert filtered_files == ['added.py', 'modified.py', 'renamed.py']
