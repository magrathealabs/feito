from git import Repo


class GitRepo:

    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def diff_files(self, index_or_tree='master'):
        """
        Returns an array of blob b files in the diff with the current branch
        and the index or tree (default to the master branch)

        param index_or_tree: str
        """
        diff = self.repo.index.diff(index_or_tree)
        return list(map(lambda file: file.b_path, diff))
