class Messages:

    def __init__(self, analysis):
        """
        params analysis: list of dictionaries -> List contating dictionaries with the
            prospector analysis.
        """
        self.analysis = analysis

    def commit_format(self):
        """
        Formats the analysis into a simpler dictionary with the line, file and message values to
            be commented on a commit.
        Returns a list of dictionaries
        """
        formatted_analyses = []
        for analyze in self.analysis['messages']:
            formatted_analyses.append({
                'message': f"{analyze['source']}: {analyze['message']}. Code: {analyze['code']}",
                'file': analyze['location']['path'],
                'line': analyze['location']['line'],
            })

        return formatted_analyses
