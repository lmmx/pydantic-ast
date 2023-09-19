from __future__ import annotations

from ._base import ASTNode

__all__ = [
    "If",
    "For",
    "While",
    "Break",
    "Continue",
    "Try",
    "TryStar",
    "ExceptHandler",
    "With",
    "withitem",
]


class If(ASTNode):
    test: ASTNode
    body: list[ASTNode]
    orelse: list[ASTNode]


class For(ASTNode):
    target: ASTNode
    iter: ASTNode
    body: list[ASTNode]
    orelse: list[ASTNode]
    type_comment: str | None


class While(ASTNode):
    test: ASTNode
    body: list[ASTNode]
    orelse: list[ASTNode]


class Break(ASTNode):
    pass


class Continue(ASTNode):
    pass


class Try(ASTNode):
    body: list[ASTNode]
    handlers: list[ASTNode]
    orelse: list[ASTNode]
    finalbody: list[ASTNode]


class TryStar(ASTNode):
    body: list[ASTNode]
    handlers: list[ASTNode]
    orelse: list[ASTNode]
    finalbody: list[ASTNode]


class ExceptHandler(ASTNode):
    type: ASTNode
    name: str | None
    body: list[ASTNode]


class withitem(ASTNode):
    context_expr: ASTNode
    optional_vars: ASTNode | None


class With(ASTNode):
    items: list[withitem]
    body: list[ASTNode]
    type_comment: str | None
