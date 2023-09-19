from __future__ import annotations

from ._base import ASTNode

# from typing import Union


__all__ = ["Load", "Store", "Del", "Name", "Starred"]


class Load(ASTNode):
    pass


class Store(ASTNode):
    pass


class Del(ASTNode):
    pass


class Name(ASTNode):
    id: str
    ctx: Load | Store | Del


class Starred(ASTNode):
    value: ASTNode  # usually Name
    ctx: Load | Store | Del


# VariableNode = Union[Name, Load, Store, Del, Starred]
