import json
import subprocess


def run(files):
    """
    Runs prospector in the input files and return a json with the analysis

    param files: list -> List of files, with relative path to the root project path, that should be analized
    """
    args_prospector = ['prospector', '--output-format', 'json'] + files
    analysis = subprocess.run(args_prospector, stdout=subprocess.PIPE)
    return json.loads(analysis.stdout)
