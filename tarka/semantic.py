"""
This file contains the Semantic Analyzer for the tarka abstract syntax tree
"""

from tarka.ast import *
from tarka.errors import *
from tarka.visitor import ASTVisitor


class SemanticAnalyzer(ASTVisitor):
    """
    Semantic Analyzer for Semantic Errors
    """

    def __init__(self) -> None:
        """
        Initializes the SemanticAnalyzer

        :param self: SemanticAnalyzer
        """
        pass

    def getExprType(self, node: Expression) -> str:
        if isinstance(node, IntLitExpr):
            return "int"
        raise Exception(f"Exception in getting expression type for expression at line {node.line}:{node.col}")

    def visit_Program(self, node: Program) -> None:
        """
        Visit Program node.

        :param self: SemanticAnalyzer
        :param node: Program Node
        :type node: Program
        """
        for stmt in node.stmts:
            self.visit(stmt)

    def visit_ExitStmt(self, node: ExitStmt) -> None:
        """
        Visits Exit Statement

        :param self: SemanticAnalyzer
        :param node: ExitStmt Node
        :type node: ExitStmt
        """
        if isinstance(node.expr, IntLitExpr):
            if node.expr.val < 0 or node.expr.val > 255:
                raise SemanticErrorInvalidExitCode(node.expr.val, node.expr.line, node.expr.col)
        exprType = self.getExprType(node.expr)
        if exprType != "int":
            raise SemanticErrorTypeMissmatch(exprType, "int", node.expr.line, node.expr.col)

    def visit_IntLitExpr(self, node: IntLitExpr) -> None:
        """
        Visits IntLitExpr Statement

        :param self: SemanticAnalyzer
        :param node: IntLitExpr Node
        :type node: IntLitExpr
        """
        pass
