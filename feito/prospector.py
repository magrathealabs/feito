import json
import subprocess


def run():
    """
    Runs prospector in the input files and returns a json with the analysis

    param files: list -> List of files, with relative path to the root project path, that should be analized
    """

    arg_prospector = 'prospector --output-format=json $(git diff master --name-only)'
    analysis = subprocess.run(arg_prospector, stdout=subprocess.PIPE, shell=True)
    return json.loads(analysis.stdout)
