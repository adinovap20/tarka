"""
This file contains the AST Visitor that visits the abstract syntax tree
for the abstract syntax tree.
"""

from typing import Any

from tarka.ast import *


class ASTVisitor:
    """
    Generic AST Visitor that implements Visitor pattern in python
    """

    def visit(self, node: ASTNode) -> Any:
        """
        Visit method that visits given node.

        :param self: ASTVisitor
        :param node: Node to Visit
        :type node: ASTNode
        :return: Return value of the function called by visitor
        :rtype: Any
        """
        methodName = f"visit_{type(node).__name__}"
        visitor = getattr(self, methodName, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: ASTNode) -> None:
        """
        Fallback function on failure that raises method not defined exception

        :param self: ASTVisitor
        :param node: Node to visit
        :type node: ASTNode
        """
        raise Exception(f"No visit_{type(node).__name__} method defined")
