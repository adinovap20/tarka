"""
The file contains the AST Printer that visits the AST and prints it.
"""

from tarka.ast import *
from tarka.visitor import ASTVisitor


class ASTPrinter(ASTVisitor):
    """
    ASTPrinter for pretty printing the AST properly.
    """

    def __init__(self) -> None:
        """
        Initializes ASTPrinter with ident variable.

        :param self: ASTPrinter
        """
        self.ident = 0

    def visit_Program(self, node: Program) -> None:
        """
        Visit Program Node.

        :param self: ASTPrinter
        :param node: Program node
        :type node: Program
        """
        print(" " * self.ident + "Program:")
        self.ident += 4
        for stmt in node.stmts:
            self.visit(stmt)
        self.ident -= 4

    def visit_ExitStmt(self, node: ExitStmt) -> None:
        """
        Visit ExitStmt Node.

        :param self: ASTPrinter
        :param node: ExitStmt node
        :type node: ExitStmt
        """
        print(" " * self.ident + "ExitStmt:")
        self.ident += 4
        self.visit(node.expr)
        self.ident -= 4

    def visit_IntLitExpr(self, node: IntLitExpr) -> None:
        """
        Visit IntLitExpr Node.

        :param self: ASTPrinter
        :param node: IntLitExpr node.
        :type node: IntLitExpr
        """
        print(" " * self.ident + f"IntLitExpr: {node.val}")
