from __future__ import annotations

from typing import Literal, Union

from ._base import ASTNode

__all__ = [
    "Constant",
    "FormattedValue",
    "JoinedStr",
    "List",
    "Tuple",
    "Set",
    "Dict",
]

Const = Union[int, float, str, None]
ConstU = Union[Const, tuple[Const], frozenset[Const]]


class Constant(ASTNode):
    value: Literal[...] | ConstU  # type: ignore[valid-type]


class FormattedValue(ASTNode):
    value: ASTNode  # ExpressionNode | VariableNode | LiteralNode
    conversion: int
    format_spec: JoinedStr | None


class JoinedStr(ASTNode):
    values: list[FormattedValue | Constant]


class List(ASTNode):
    elts: list[ASTNode]
    ctx: ASTNode  # Load | Store


class Tuple(ASTNode):
    elts: list[ASTNode]
    ctx: ASTNode  # Load | Store


class Set(ASTNode):
    elts: list[ASTNode]


class Dict(ASTNode):
    keys: list[ASTNode]
    values: list[ASTNode]


# LiteralNode = Union[Constant, FormattedValue, JoinedStr, List, Tuple, Set, Dict]
