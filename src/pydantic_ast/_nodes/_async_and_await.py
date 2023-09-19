from __future__ import annotations

from ._base import ASTNode
from ._control_flow import withitem
from ._function_and_classdefs import arguments

__all__ = ["AsyncFunctionDef", "Await", "AsyncFor", "AsyncWith"]


class AsyncFunctionDef(ASTNode):
    name: str
    args: arguments
    body: list[ASTNode]
    decorator_list: list[ASTNode]
    returns: ASTNode
    type_comment: str | None


class Await(ASTNode):
    value: ASTNode


class AsyncFor(ASTNode):
    target: ASTNode
    iter: ASTNode
    body: list[ASTNode]
    orelse: list[ASTNode]
    type_comment: str | None


class AsyncWith(ASTNode):
    items: list[withitem]
    body: list[ASTNode]
    type_comment: str | None
