from __future__ import annotations

from .comprehensions import DictComp, GeneratorExp, ListComp, SetComp, comprehension
from .core import (
    Add,
    And,
    Attribute,
    BinOp,
    BitAnd,
    BitOr,
    BitXor,
    BoolOp,
    Call,
    Compare,
    Div,
    Eq,
    Expr,
    FloorDiv,
    Gt,
    GtE,
    IfExp,
    In,
    Invert,
    Is,
    IsNot,
    LShift,
    Lt,
    LtE,
    MatMult,
    Mod,
    Mult,
    NamedExpr,
    Not,
    NotEq,
    NotIn,
    Or,
    Pow,
    RShift,
    Sub,
    UAdd,
    UnaryOp,
    USub,
    keyword,
)
from .subscripting import Slice, Subscript

# from typing import Union


__all__ = [
    # core
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
    # subscripting
    "Slice",
    "Subscript",
    # comprehensions
    "DictComp",
    "GeneratorExp",
    "ListComp",
    "SetComp",
    "comprehension",
]

# Listed below in the same order as the Python docs (3.11.5)

# fmt: off
# ExpressionNode = Union[
#     # core
#     Expr, UnaryOp, UAdd, USub, Not, Invert, BinOp, Add, Sub, Mult, Div,
#     FloorDiv, Mod, Pow, LShift, RShift, BitOr, BitXor, BitAnd, MatMult,
#     BoolOp, And, Or, Compare, Eq, NotEq, Lt, LtE, Gt, GtE, Is, IsNot,
#     In, NotIn, Call, keyword, IfExp, Attribute, NamedExpr,
#     # subscripting
#     Slice, Subscript,
#     # comprehensions
#     DictComp, GeneratorExp, ListComp, SetComp, comprehension
# ]
# fmt: on
