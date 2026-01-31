"""
Errors in Tarka
"""


class LexerError(Exception):
    """
    Unknown character error while lexical analysis
    """

    def __init__(self, c: str, line: int, col: int) -> None:
        """
        Raises the LexerError exception

        :param self: LexerError
        :param c: Unknown character
        :type c: str
        :param line: Line number of unknown character
        :type line: int
        :param col: Column number of unknown character
        :type col: int
        """
        super().__init__(f"Unknown character: {c} at line {line}:{col}")
