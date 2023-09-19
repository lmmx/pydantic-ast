from __future__ import annotations

from .._base import ASTNode

__all__ = ["DictComp", "GeneratorExp", "ListComp", "SetComp", "comprehension"]


class comprehension(ASTNode):
    target: ASTNode
    iter: ASTNode
    ifs: list[ASTNode]
    is_async: int  # 0 or 1


class DictComp(ASTNode):
    key: ASTNode
    value: ASTNode
    generators: list[comprehension]


class GeneratorExp(ASTNode):
    elt: ASTNode
    generators: list[comprehension]


class ListComp(ASTNode):
    elt: ASTNode
    generators: list[comprehension]


class SetComp(ASTNode):
    elt: ASTNode
    generators: list[comprehension]
