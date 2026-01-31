"""
Errors in Tarka
"""

from tarka.token import Token, TokenType


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
        super().__init__(f"Lexer Error - Unknown character: {c} at line {line}:{col}")


class ParserError(Exception):
    """
    Parser Error
    """

    def __init__(self, msg: str, line: int, col: int) -> None:
        """
        Raises the ParserError exception

        :param self: ParserError
        :param msg: Msg to raise
        :type msg: str
        :param line: Line number of error
        :type line: int
        :param col: Column number of error
        :type col: int
        """
        super().__init__(f"Parser Error - {msg} at line {line}:{col}")


class ParserErrorUnexpectedTokenFoundEOF(ParserError):
    """
    Parser Error for unexpected token but found end of file.
    """

    def __init__(self, exp: TokenType, look: int, line: int, col: int) -> None:
        super().__init__(f"Expected '{exp.name}', but found EOF {look} tokens after token", line, col)


class ParserErrorUnexpectedToken(ParserError):
    """
    Parser Error for unexpected token
    """

    def __init__(self, exp: TokenType, found: Token) -> None:
        lit = "\\n" if found.lit == "\n" else found.lit
        super().__init__(f"Expected '{exp.name}', but found '{lit}'", found.line, found.col)


class ParserErrorNoMatchingStmt(ParserError):
    """
    Parser Error for no matching statement
    """

    def __init__(self, tok: Token) -> None:
        """
        Raises the ParserErrorNoMatchingStmt exception

        :param self: ParserErrorNoMatchingStmt
        :param tok: Token that did not match
        :type tok: Token
        """
        lit = "\\n" if tok.lit == "\n" else tok.lit
        super().__init__(f"No matching statement found for '{lit}' of type {tok.type.name}", tok.line, tok.col)


class ParserErrorNoMatchingExpr(ParserError):
    """
    Parser Error for no matching expression
    """

    def __init__(self, tok: Token) -> None:
        """
        Raises ParserErrorNoMatchingExpr exception

        :param self: ParserErrorNoMatchingExpr
        :param tok: Token that did not match any expression
        :type tok: Token
        """
        super().__init__(f"No matching expression found for '{tok.lit}' of type {tok.type.name}", tok.line, tok.col)


class SemanticError(Exception):
    """
    Semantic Error
    """

    def __init__(self, msg: str, line: int, col: int) -> None:
        """
        Initializes Semantic Error

        :param self: Semantic Error
        :param msg: Error Message
        :type msg: str
        :param line: Line no of the error
        :type line: int
        :param col: Column no of the error
        :type col: int
        """
        super().__init__(f"Semantic Error - {msg} at line {line}:{col}")


class SemanticErrorInvalidExitCode(SemanticError):
    """
    Semantic Error when exit code is not between 0 and 255.
    """

    def __init__(self, code: int, line: int, col: int) -> None:
        """
        Raises SemanticErrorInvalidExitCode

        :param self: SemanticError
        :param code: Exit code found
        :type code: int
        :param line: Line no of the occurrence
        :type line: int
        :param col: Column no of the occurrence
        :type col: int
        """
        super().__init__(f"Exit code should be between 0 and 255, inclusive. Invalid exit code {code}", line, col)
