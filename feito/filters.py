class Filters:

    @staticmethod
    def filter_python_files(files):
        """
        param files: list of strings -> File names

        For a list of file name strings. it returns
        only those that are a Python file
        """
        return list(filter(lambda file: file[-2:] == 'py', files))
