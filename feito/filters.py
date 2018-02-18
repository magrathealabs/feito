class Filters:

    @staticmethod
    def filter_python_files(files):
        """
        param files: list of strings -> File names

        For a list of file name strings. it returns
        only those that are a Python file
        """
        return list(filter(lambda file: file[-2:] == 'py', files))

    @staticmethod
    def filter_diff_files(diff_objects):
        """
        params diff_objects: list of Repo diff objects (e.g., [<git.diff.Diff at ...>, git.diff.Diff at ...>])

        For a list of diff objects, only the files that
        have been added, modified or renamed are returned
        """
        accepted_changes = ['A', 'M', 'R']
        for diff in diff_objects:
            if diff.change_type not in accepted_changes:
                diff_objects.remove(diff)

        return list(map(lambda file: file.b_path, diff_objects))
