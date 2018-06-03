import json
import subprocess


class Prospector:

    def __init__(self, repo):
        self.repo = repo

    def run(self):
        """
        Runs prospector in the input files and returns a json with the analysis
        """

        # TODO: Rename both
        patch_list = self.repo.patch_list()

        for patch in patch_list:
            file = patch['file']
            arg_prospector = f'prospector --output-format json {file}'
            analysis = subprocess.run(arg_prospector, stdout=subprocess.PIPE, shell=True)
            patch['prospector'] = json.loads(analysis.stdout)

        return patch_list
