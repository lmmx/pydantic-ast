import ast

from pydantic_ast import AST_to_pydantic, parse


def test_convert_assignment():
    code = "x = 1"
    parsed = ast.parse(code)
    converted_parsed = AST_to_pydantic().visit(parsed)
    wrapped_parsed = parse(code)
    assert wrapped_parsed == converted_parsed
