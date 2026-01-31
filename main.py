"""
Entry point for the application
"""

import argparse

from tarka.lexer import Lexer


def run() -> None:
    """
    This function runs the tarka compiler
    """
    parser = argparse.ArgumentParser(description="Tarka Compiler Options")
    parser.add_argument("file", type=str, help="Path of tarka (*.tk) file to compile.")
    args = parser.parse_args()
    filePath: str = args.file
    with open(filePath, "r") as f:
        code = f.read()
    code += "\n"
    lexer = Lexer(code)
    tokens = lexer.GetTokens()
    print("=== Lexical Analysis ==")
    print(", ".join(str(token) for token in tokens))


if __name__ == "__main__":
    run()
