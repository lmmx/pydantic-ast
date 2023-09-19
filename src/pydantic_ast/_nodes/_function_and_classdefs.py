from __future__ import annotations

from ._base import ASTNode
from ._expr.core import keyword

__all__ = [
    "FunctionDef",
    "Lambda",
    "arguments",
    "arg",
    "Return",
    "Yield",
    "YieldFrom",
    "Global",
    "Nonlocal",
    "ClassDef",
]


class arg(ASTNode):
    arg: str
    annotation: ASTNode | None


class arguments(ASTNode):
    posonlyargs: list[arg]
    args: list[arg]
    vararg: arg | None
    kwonlyargs: list[arg]
    kw_defaults: list[ASTNode | None]
    kwarg: arg | None
    defaults: list[ASTNode]


class FunctionDef(ASTNode):
    name: str
    args: arguments
    body: list[ASTNode]
    decorator_list: list[ASTNode]
    returns: ASTNode | None
    type_comment: str | None


class Lambda(ASTNode):
    args: arguments
    body: ASTNode


class Return(ASTNode):
    value: ASTNode | None


class Yield(ASTNode):
    value: ASTNode


class YieldFrom(ASTNode):
    value: ASTNode


class Global(ASTNode):
    names: list[str]


class Nonlocal(ASTNode):
    names: list[str]


class ClassDef(ASTNode):
    name: str
    bases: list[ASTNode]
    keywords: list[keyword]
    body: list[ASTNode]
    decorator_list: list[ASTNode]
