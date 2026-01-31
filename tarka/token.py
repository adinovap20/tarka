"""
This file contains Token structure and TokenType enum
"""

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    """
    TokenType enum containing all Token types.
    """

    # Keywords
    KW_EXIT = auto()
    """TokenType for **exit**"""

    # Literals
    LIT_INT = auto()
    """TokenType for **int**"""
    LIT_IDENT = auto()
    """Literal Identifier"""

    # Extra
    EX_UNKNOWN = auto()
    """TokenType for **unknown token**"""
    EX_NEWLINE = auto()
    """TokenType for **newline**"""


@dataclass
class Token:
    """
    Structure for Token
    """

    type: TokenType
    """Type of the Token"""
    lit: str
    """Literal for token struct"""
    line: int
    """Line number of the token"""
    col: int
    """Column number of the token"""

    def __str__(self) -> str:
        """
        __str__ magic function to print(str(Token))

        :param self: Token
        :return: Representation of Token
        :rtype: str
        """
        lit = "\\n" if self.lit == "\n" else self.lit
        return f"[{self.type.name}, '{lit}', {self.line}:{self.col}]"


keywords: dict[str, TokenType] = {
    "exit": TokenType.KW_EXIT,
}
"""Dictionary containing identifiers and their corresponding keyword token types"""


def GetKeywordOrIdentifierTokenType(ident: str) -> TokenType:
    """
    If the **ident** is keyword then this function returns the respective keyword
    token, otherwise it returns the literal identifier token.

    :param ident: Identifier string
    :type ident: str
    :return: Keyword TokenType or Identifier TokenType
    :rtype: TokenType
    """
    return keywords.get(ident, TokenType.LIT_IDENT)
