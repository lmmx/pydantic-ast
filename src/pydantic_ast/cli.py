import sys

import pydantic

import pydantic_ast


class CLIParser(BaseModel):
    # source: Path | None

    # def read(self) -> str:
    #     return sys.stdin.read() if self.source is None else self.source.read_text()
    source: Path


# def read_command_line(source: str | None = None) -> None:
def read_command_line(source: str = "-") -> None:
    input_text = CLIParser(source=source).source.read_text()
    result = pydantic_ast.parse(input_text)
    print(result)
    return
