"""
Entry point for the application
"""

import argparse

from tarka.ast_printer import ASTPrinter
from tarka.ir import IRVisitor
from tarka.lexer import Lexer
from tarka.parser import Parser
from tarka.semantic import SemanticAnalyzer


def run() -> None:
    """
    This function runs the tarka compiler
    """
    parser = argparse.ArgumentParser(description="Tarka Compiler Options")
    parser.add_argument("file", type=str, help="Path of tarka (*.tk) file to compile.")
    parser.add_argument("--ir", type=str, help="IR file path (*.tir) file to dump ir in.")
    args = parser.parse_args()
    filePath: str = args.file
    with open(filePath, "r") as f:
        code = f.read()
    code += "\n"
    lexer = Lexer(code)
    tokens = lexer.GetTokens()
    print("=== Lexical Analysis ===")
    print(", ".join(str(token) for token in tokens))
    print("=== Syntax Analysis ===")
    parser = Parser(tokens)
    program = parser.Parse()
    printer = ASTPrinter()
    printer.visit(program)
    print("=== Semantic Analysis ===")
    analyzer = SemanticAnalyzer()
    analyzer.visit(program)
    print("Semantic Analysis Complete")
    print("=== IR Generation ===")
    irVisitor = IRVisitor()
    irVisitor.visit(program)
    if not args.ir:
        raise Exception("Please use --ir flag to output ir file")
    with open(args.ir, "w") as f:
        f.write(irVisitor.GetCode())
    print(f"Dumped IR in file {args.ir}")


if __name__ == "__main__":
    run()
