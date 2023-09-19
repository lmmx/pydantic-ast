from __future__ import annotations

from ._base import ASTNode

__all__ = ["AST", "Module", "Expression", "Interactive", "FunctionType"]


class AST(ASTNode):
    lineno: int
    col_offset: int
    end_lineno: int
    end_col_offset: int
    fields: list[ASTNode]  # list of nodes, _fields in stdlib


class Module(ASTNode):
    body: list[ASTNode]  # StatementNode]
    type_ignores: list[str]


class Expression(ASTNode):
    body: ASTNode  # ExpressionNode


class Interactive(ASTNode):
    body: list[ASTNode]  # list[StatementNode]


class FunctionType(ASTNode):
    argtypes: list[ASTNode]  # ExpressionNode]
    returns: ASTNode  # ExpressionNode
