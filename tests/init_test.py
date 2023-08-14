from pytest import mark, raises

import pydantic_ast


@mark.parametrize("x,y", [("", "")])
def test_xy(x, y):
    with raises(AssertionError):
        assert not pydantic_ast
