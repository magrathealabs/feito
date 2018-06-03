class Messages:

    def __init__(self, analysis_list):
        """
        params analysis: list of dictionaries -> List contating dictionaries with the
            prospector analysis.
        """
        self.analysis_list = analysis_list

    def commit_format(self):
        """
        Formats the analysis into a simpler dictionary with the line, file and message values to
            be commented on a commit.
        Returns a list of dictionaries
        """
        formatted_analysis = []
        for analyze in self.analysis_list['prospector']:
            for message in analyze['messages']:
                formatted_analysis.append({
                    'message': f"{message['source']}: {message['message']}. Code: {message['code']}",
                    'file': message['location']['path'],
                    # TODO: Finish
                    # 'line': format_line_number(message['location']['line'], ),
                })

        return formatted_analysis

    def parse_hunk(hunk):


    @staticmethod
    def format_line_number(line_comment_no, hunk):
        lines_add = 0
        for line in hunk:
            if line.target_line_no is None:
                lines_add += 1
            elif line.target_line_no == line_comment_no:
                return line_comment_no + lines_add

