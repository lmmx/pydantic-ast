from __future__ import annotations

from .._base import ASTNode

__all__ = [
    "Expr",
    "UnaryOp",
    "UAdd",
    "USub",
    "Not",
    "Invert",
    "BinOp",
    "Add",
    "Sub",
    "Mult",
    "Div",
    "FloorDiv",
    "Mod",
    "Pow",
    "LShift",
    "RShift",
    "BitOr",
    "BitXor",
    "BitAnd",
    "MatMult",
    "BoolOp",
    "And",
    "Or",
    "Compare",
    "Eq",
    "NotEq",
    "Lt",
    "LtE",
    "Gt",
    "GtE",
    "Is",
    "IsNot",
    "In",
    "NotIn",
    "Call",
    "keyword",
    "IfExp",
    "Attribute",
    "NamedExpr",
]


class Expr(ASTNode):
    value: ASTNode  # Constant | Name | Lambda | Yield | YieldFrom


# Unary operators


class UAdd(ASTNode):
    pass


class USub(ASTNode):
    pass


class Not(ASTNode):
    pass


class Invert(ASTNode):
    pass


class UnaryOp(ASTNode):
    op: UAdd | USub | Not | Invert
    operand: ASTNode


# Binary operators


class Add(ASTNode):
    pass


class Sub(ASTNode):
    pass


class Mult(ASTNode):
    pass


class Div(ASTNode):
    pass


class FloorDiv(ASTNode):
    pass


class Mod(ASTNode):
    pass


class Pow(ASTNode):
    pass


class LShift(ASTNode):
    pass


class RShift(ASTNode):
    pass


class BitOr(ASTNode):
    pass


class BitXor(ASTNode):
    pass


class BitAnd(ASTNode):
    pass


class MatMult(ASTNode):
    pass


class BinOp(ASTNode):
    left: ASTNode
    op: (
        Add
        | Sub
        | Mult
        | Div
        | FloorDiv
        | Mod
        | Pow
        | LShift
        | RShift
        | BitOr
        | BitXor
        | BitAnd
        | MatMult
    )
    right: ASTNode


class And(ASTNode):
    pass


class Or(ASTNode):
    pass


class BoolOp(ASTNode):
    op: And | Or
    values: list[ASTNode]


class Eq(ASTNode):
    pass


class NotEq(ASTNode):
    pass


class Lt(ASTNode):
    pass


class LtE(ASTNode):
    pass


class Gt(ASTNode):
    pass


class GtE(ASTNode):
    pass


class Is(ASTNode):
    pass


class IsNot(ASTNode):
    pass


class In(ASTNode):
    pass


class NotIn(ASTNode):
    pass


class Compare(ASTNode):
    left: ASTNode
    ops: list[Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn]
    comparators: list[ASTNode]


class keyword(ASTNode):
    arg: str | None
    value: ASTNode


class Call(ASTNode):
    func: ASTNode
    args: list[ASTNode]
    keywords: list[keyword]


class IfExp(ASTNode):
    test: ASTNode
    body: ASTNode
    orelse: ASTNode


class Attribute(ASTNode):
    value: ASTNode
    attr: str
    ctx: ASTNode  # Load | Store | Del


class NamedExpr(ASTNode):
    target: ASTNode
    value: ASTNode
