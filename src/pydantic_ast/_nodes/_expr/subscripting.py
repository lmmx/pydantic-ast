from __future__ import annotations

from .._base import ASTNode

__all__ = ["Slice", "Subscript"]


class Slice(ASTNode):
    lower: ASTNode | None
    upper: ASTNode | None
    step: ASTNode | None


class Subscript(ASTNode):
    value: ASTNode
    slice: ASTNode
    ctx: ASTNode  # Load | Store | Del
