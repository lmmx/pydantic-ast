# Pydantic AST

Pydantic models covering Python AST types.

<!-- [![downloads](https://static.pepy.tech/badge/pydantic-ast/month)](https://pepy.tech/project/pydantic-ast) -->
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![PyPI](https://img.shields.io/pypi/v/pydantic-ast.svg)](https://pypi.org/project/pydantic-ast)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pydantic-ast.svg)](https://pypi.org/project/pydantic-ast)
[![License](https://img.shields.io/pypi/l/pydantic-ast.svg)](https://pypi.python.org/pypi/pydantic-ast)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lmmx/pydantic-ast/master.svg)](https://results.pre-commit.ci/latest/github/lmmx/pydantic-ast/master)

<!-- [![build status](https://github.com/lmmx/pydantic_ast/actions/workflows/master.yml/badge.svg)](https://github.com/lmmx/pydantic_ast/actions/workflows/master.yml) -->

## Installation

```py
pip install pydantic-ast
```

## Usage

Use it as a drop-in replacement to `ast.parse` with a more readable representation.

```py
>>> import ast
>>> import pydantic_ast
>>> source = "x = 1"
>>> ast.parse(source)
<ast.Module object at 0x7fef82567610>
>>> pydantic_ast.parse(source)
body=[Assign(targets=[Name(id='x', ctx=Store())], value=Constant(value=1), type_comment=None)] type_ignores=[]
```

Use it on the command line to quickly get an AST of a Python program or a section of one

```sh
echo '"Hello world"' | pydantic-ast
```
⇣
```
body=[Expr(value=Constant(value='Hello world'))] type_ignores=[]
```

Use it on ASTs you got from elsewhere to make them readable, or to inspect parts of them more easily.
The `AST_to_pydantic` class is a `ast.NodeTransformer` that converts nodes in the AST to
`pydantic_ast` model types when the tree nodes are visited.

```py
>>> from pydantic_ast import AST_to_pydantic
>>> source = "123 + 345 == expected"
>>> my_mystery_ast = ast.parse(source)
>>> ast_model = AST_to_pydantic().visit(my_mystery_ast)
>>> ast_model
body=[Expr(value=Compare(left=BinOp(left=Constant(value=123), op=Add(), right=Constant(value=345)), ops=[Eq()], comparators=[Name(id='expected', ctx=Load())]))] type_ignores=[]
>>> ast_model.body
[Expr(value=Compare(left=BinOp(left=Constant(value=123), op=Add(), right=Constant(value=345)), ops=[Eq()], comparators=[Name(id='expected', ctx=Load())]))]
```

It's simply much easier to drill down into a tree when you can see the fields in a repr.

```py
>>> ast_model.body[0].value
Compare(left=BinOp(left=Constant(value=123), op=Add(), right=Constant(value=345)), ops=[Eq()],
comparators=[Name(id='expected', ctx=Load())])
>>> ast_model.body[0].value.left
BinOp(left=Constant(value=123), op=Add(), right=Constant(value=345))
>>> ast_model.body[0].value.left.left
Constant(value=123)
>>> ast_model.body[0].value.left.left.value
123
```

## Development

- To set up pre-commit hooks (to keep the CI bot happy) run `pre-commit install-hooks` so all git
  commits trigger the pre-commit checks. I use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
  This runs `black`, `flake8`, `autopep8`, `pyupgrade`, etc.

- To set up a dev env, I first create a new conda environment and use it in PDM with `which python > .pdm-python`.
  To use `virtualenv` environment instead of conda, skip that. Run `pdm install` and a `.venv` will be created if no
  Python binary path is found in `.pdm-python`.

- To run tests, run `pdm run python -m pytest` and the PDM environment will be used to run the test suite.
