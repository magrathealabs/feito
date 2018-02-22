import json
import subprocess


class Prospector:

    def __init__(self, repo):
        self.repo = repo

    def run(self):
        """
        Runs prospector in the input files and returns a json with the analysis
        """
        arg_prospector = f'prospector --output-format json {self.repo.diff_files()}'
        analysis = subprocess.run(arg_prospector, stdout=subprocess.PIPE, shell=True)
        return json.loads(analysis.stdout)
