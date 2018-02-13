import os

from git import Repo

from feito import Filters


class Repository:

    def __init__(self):
        self.repo = Repo(os.getcwd())
        self.repo_name = self.__repo_name()
        self.last_commit_id = self.__commit_id()

    def __repo_name(self):
        return self.repo.working_dir.split('/')[-1]

    def __commit_id(self):
        return self.repo.head.commit.hexsha

    def diff_files(self):
        hcommit = self.repo.head.commit
        diff_objs = hcommit.diff('HEAD~1')

        filtered_diff_files = Filters.filter_diff_files(diff_objs)
        filtered_python_files = Filters.filter_python_files(filtered_diff_files)

        return " ".join(filtered_python_files)
