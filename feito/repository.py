import os
import subprocess

from unidiff import PatchSet

from feito.filters import Filters


class Repository:

    GIT_DIFF_FILES = 'git diff --name-only --diff-filter=ACMR master'

    def __init__(self, repo):
        self.repo_name = repo
        self.last_commit_id = os.getenv('COMMIT_ID')

    def patch_list(self):
        diff_files = subprocess.run(self.GIT_DIFF_FILES, stdout=subprocess.PIPE, shell=True)
        diff_list = diff_files.stdout.decode().split('\n')[:-1]

        filtered_python_files = Filters.filter_python_files(diff_list)
        patch_list = self.build_patch_list(filtered_python_files)

        return patch_list

    @staticmethod
    def build_patch_list(files):
        patch_list = []
        for file in files:
            diff = subprocess.run(f'git diff master {file}', stdout=subprocess.PIPE, shell=True)
            patch = PatchSet(diff.stdout.decode())
            patch_list.append({'file': file, 'hunks': [hunk for hunk in patch[0]]})

        return patch_list
