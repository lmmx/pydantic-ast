import argparse
import sys
from pathlib import Path

from pydantic import BaseModel

import pydantic_ast


class CLIParser(BaseModel):
    source: Path | None

    def read(self) -> str:
        if self.source is not None:
            return self.source.read_text()
        elif not sys.stdin.isatty():
            return sys.stdin.read()
        else:
            # Handle the case where there's no input (either file or pipe)
            raise ValueError("No input provided.")


def read_command_line():
    parser = argparse.ArgumentParser(description="Process some input.")
    parser.add_argument("source", nargs="?", type=Path, help="a source file to process")
    args = parser.parse_args()
    try:
        input_text = CLIParser(source=args.source).read()
    except ValueError as exc:
        sys.exit(f"Error: {exc}")
    result = pydantic_ast.parse(input_text)
    print(result)
    return
