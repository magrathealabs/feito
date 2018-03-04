import os
import subprocess

from feito.filters import Filters


class Repository:

    GIT_DIFF_COMMAND = 'git diff --name-only --diff-filter=ACMR master'

    def __init__(self, repo):
        self.repo_name = repo
        self.last_commit_id = os.getenv('COMMIT_ID')

    def diff_files(self):
        diff_files = subprocess.run(self.GIT_DIFF_COMMAND, stdout=subprocess.PIPE, shell=True)
        diff_list = diff_files.stdout.decode().split('\n')[:-1]

        filtered_python_files = Filters.filter_python_files(diff_list)

        return " ".join(filtered_python_files)
