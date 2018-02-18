import os
from unittest import TestCase
from unittest import mock

from git import Repo

from feito import Repository

# Note: always run this test case from the project root directory. It gets the actual repository
# name from the path and if run from any folder above or below, it won't find a directory and thus
# raise an error.
class RepositoryTestCase(TestCase):

    def setUp(self):
        self.repo = Repository()

    def test_repo_name(self):
        repo_name = self.repo.repo_name

        assert repo_name == os.getenv('REPO_NAME')

    def test_last_commit_id(self):
        commit_id = self.repo.last_commit_id

        assert commit_id == os.getenv('COMMIT_ID')
