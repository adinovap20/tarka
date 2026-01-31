"""
Lexer for Tarka Language
"""

from tarka.errors import LexerError
from tarka.token import GetKeywordOrIdentifierTokenType, Token, TokenType


class Lexer:
    """
    Lexer class
    """

    def __init__(self, code: str) -> None:
        """
        Creates instance of Lexer class

        :param self: Lexer
        :param code: Code to tokenize
        :type code: str
        """
        self.code: str = code
        self.codeLen: int = len(code)
        self.curPos = int(-1)
        self.curChar = str("\0")
        self.line = int(1)
        self.col = int(0)

    def GetTokens(self) -> list[Token]:
        """
        Returns list of tokens tokenized from Token

        :param self: Lexer
        :return: List of tokens
        :rtype: list[Token]
        """
        tokens: list[Token] = []
        self.__readChar()
        while self.curPos < self.codeLen:
            if self.curChar in [" ", "\r", "\t"]:
                self.__readWhiteSpace()
            elif self.curChar == "\n":
                tok = self.__readNewline()
                tokens.append(tok)
            elif self.curChar.isalpha() or self.curChar == "_":
                tok = self.__readIdentifier()
                tokens.append(tok)
            elif self.curChar.isdigit():
                tok = self.__readNumber()
                tokens.append(tok)
            else:
                raise LexerError(self.curChar, self.line, self.col)
        return tokens

    def __readChar(self) -> None:
        """
        Moves the current pointer to the next character

        :param self: Lexer
        """
        self.curPos += 1
        if self.curPos >= self.codeLen:
            return
        if self.curChar == "\n":
            self.line += 1
            self.col = 0
        self.curChar = self.code[self.curPos]
        self.col += 1

    def __readWhiteSpace(self) -> None:
        """
        Skips the whitespace

        :param self: Lexer
        """
        self.__readChar()

    def __readNewline(self) -> Token:
        """
        Reads the Newline

        :param self: Lexer
        """
        tok = Token(TokenType.EX_NEWLINE, "\n", self.line, self.col)
        self.__readChar()
        return tok

    def __readIdentifier(self) -> Token:
        """
        Returns the Identifier or Keyword token

        :param self: Lexer
        :return: Identifier or Keyword token
        :rtype: Token
        """
        beg: int = self.curPos
        line: int = self.line
        col: int = self.col
        while self.curPos < self.codeLen and (self.curChar.isalpha() or self.curChar == "_"):
            self.__readChar()
        ident = self.code[beg : self.curPos]
        tokType = GetKeywordOrIdentifierTokenType(ident)
        return Token(tokType, ident, line, col)

    def __readNumber(self) -> Token:
        """
        Returns the specific number token

        :param self: Lexer
        :return: Number Token
        :rtype: Token
        """
        beg: int = self.curPos
        line: int = self.line
        col: int = self.col
        while self.curPos < self.codeLen and self.curChar.isdigit():
            self.__readChar()
        number = self.code[beg : self.curPos]
        return Token(TokenType.LIT_INT, number, line, col)
