import json
import subprocess


def run():
    """
    Runs prospector in the input files and returns a json with the analysis
    """

    arg_prospector = f'prospector --output-format json {filter_python_files()}'
    analysis = subprocess.run(arg_prospector, stdout=subprocess.PIPE, shell=True)
    return json.loads(analysis.stdout)

def filter_python_files():
    diff_files = subprocess.run('git diff master... --name-only', stdout=subprocess.PIPE, shell=True)
    decoded_diff_files = diff_files.stdout.decode()[:-1].split()
    for file in decoded_diff_files:
        if file[-2:] != 'py':
            decoded_diff_files.remove(file)

    return " ".join(decoded_diff_files)
