from __future__ import annotations

from ._base import ASTNode

__all__ = [
    "Match",
    "match_case",
    "MatchValue",
    "MatchSingleton",
    "MatchSequence",
    "MatchStar",
    "MatchMapping",
    "MatchClass",
    "MatchAs",
    "MatchOr",
]


class match_case(ASTNode):
    pattern: ASTNode
    guard: ASTNode | None
    body: list[ASTNode]


class Match(ASTNode):
    subject: ASTNode
    cases: list[match_case]


class MatchValue(ASTNode):
    value: ASTNode


class MatchSingleton(ASTNode):
    value: ASTNode


class MatchSequence(ASTNode):
    patterns: list[ASTNode]


class MatchStar(ASTNode):
    name: str | None


class MatchMapping(ASTNode):
    keys: list[ASTNode]
    patterns: list[ASTNode]
    rest: str | None


class MatchClass(ASTNode):
    cls: ASTNode
    patterns: list[ASTNode]
    kwd_attrs: list[str]
    kwd_patterns: list[ASTNode]


class MatchAs(ASTNode):
    pattern: ASTNode | None
    name: str | None


class MatchOr(ASTNode):
    patterns: list[ASTNode]
