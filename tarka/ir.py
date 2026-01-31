"""
This module contains visitor to convert Tarka code into the Tarka Intermediate Representation
"""

from tarka.ast import *
from tarka.visitor import ASTVisitor
from tarkairbind.nodes import *


class IRVisitor(ASTVisitor):
    """
    Visitor for the AST to generate Tarka IR.
    """

    def __init__(self) -> None:
        """
        Initializes the IRVisitor

        :param self: IRVisitor
        """
        self.module = IRModule()
        self.curFunc: IRFuncInst | None = None

    def GetCode(self) -> str:
        return self.module.GetCode()

    def visit_Program(self, node: Program) -> None:
        """
        Visit Program node.

        :param self: IRVisitor
        :param node: Program Node
        :type node: Program
        """
        self.curFunc = IRFuncInst("main")
        for stmt in node.stmts:
            self.visit(stmt)
        self.module.inst.append(self.curFunc)
        self.curFunc = None

    def visit_ExitStmt(self, node: ExitStmt) -> None:
        """
        Visits Exit Statement

        :param self: IRVisitor
        :param node: ExitStmt Node
        :type node: ExitStmt
        """
        if not self.curFunc:
            raise Exception("No function to append exit statement in")
        if isinstance(node.expr, IntLitExpr):
            irExitIntInst = IRExitIntInst(node.expr.val)
            self.curFunc.inst.append(irExitIntInst)

    def visit_IntLitExpr(self, node: IntLitExpr) -> None:
        """
        Visits IntLitExpr Statement

        :param self: IRVisitor
        :param node: IntLitExpr Node
        :type node: IntLitExpr
        """
        pass
