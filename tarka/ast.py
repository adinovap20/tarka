"""
This file contains all the nodes required to build AST
"""

from dataclasses import dataclass


@dataclass
class ASTNode:
    """
    Parent class of all nodes of the AST
    """

    line: int
    col: int


@dataclass
class Statement(ASTNode):
    """
    Parent class of all statement nodes of the AST
    """

    pass


@dataclass
class Expression(ASTNode):
    """
    Parent class of all expression nodes of the AST
    """

    pass


@dataclass
class Program(ASTNode):
    """
    Root node of the AST which contain list of statements
    """

    stmts: list[Statement]
    """List of statements"""


@dataclass
class IntLitExpr(Expression):
    """
    Node for integer literal expression. E.g., 5.
    """

    val: int
    """Value of the Integer literal"""


@dataclass
class ExitStmt(Statement):
    """
    Node for exit statement. E.g., `exit 10`
    """

    expr: Expression
    """Expression to exit"""
