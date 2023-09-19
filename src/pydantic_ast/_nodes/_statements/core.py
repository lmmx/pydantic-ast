from __future__ import annotations

from .._base import ASTNode

__all__ = [
    "Assign",
    "AnnAssign",
    "AugAssign",
    "Raise",
    "Assert",
    "Delete",
    "Pass",
]


class Assign(ASTNode):
    targets: list[ASTNode]
    value: ASTNode
    type_comment: str | None


class AnnAssign(ASTNode):
    target: ASTNode
    annotation: ASTNode
    value: ASTNode | None
    simple: int  # 0 or 1


class AugAssign(ASTNode):
    target: ASTNode
    op: ASTNode
    value: ASTNode


class Raise(ASTNode):
    exc: ASTNode
    cause: ASTNode | None


class Assert(ASTNode):
    test: ASTNode
    msg: ASTNode


class Delete(ASTNode):
    targets: list[ASTNode]


class Pass(ASTNode):
    pass
