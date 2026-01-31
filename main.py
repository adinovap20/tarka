"""
Entry point for the application
"""

import argparse

from tarka.ast_printer import ASTPrinter
from tarka.lexer import Lexer
from tarka.parser import Parser


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
    print("=== Syntax Analysis ==")
    parser = Parser(tokens)
    program = parser.Parse()
    printer = ASTPrinter()
    printer.visit(program)


if __name__ == "__main__":
    run()
