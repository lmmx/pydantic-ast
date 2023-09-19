import sys
from pathlib import Path

from pydantic import BaseModel

import pydantic_ast


class CLIParser(BaseModel):
    source: Path | None

    def read(self) -> str:
        return sys.stdin.read() if self.source is None else self.source.read_text()


# def read_command_line(source: str | None = None) -> None:
def read_command_line(source: str | None = None) -> None:
    input_text = CLIParser(source=source).read()
    result = pydantic_ast.parse(input_text)
    print(result)
    return
