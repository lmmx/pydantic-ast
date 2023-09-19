from __future__ import annotations

from .._base import ASTNode

__all__ = ["Import", "ImportFrom", "alias"]


class alias(ASTNode):
    name: str
    asname: str | None


class Import(ASTNode):
    names: list[alias]


class ImportFrom(ASTNode):
    module: str | None
    names: list[alias]
    level: int  # relative level, 0 means absolute import
