import os
from unittest import TestCase

from feito import Repository


class RepositoryTestCase(TestCase):

    def setUp(self):
        self.repo = Repository(os.getenv('REPOSITORY_NAME'))

    def test_repo_name(self):
        repo_name = self.repo.repo_name

        assert repo_name == os.getenv('REPOSITORY_NAME')

    def test_last_commit_id(self):
        commit_id = self.repo.last_commit_id

        assert commit_id == os.getenv('COMMIT_ID')
