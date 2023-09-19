import ast
import logging
from ast import NodeTransformer

import pydantic_ast

__all__ = ["AST_to_pydantic", "parse"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AST_to_pydantic(NodeTransformer):
    def generic_visit(self, node):
        node_class_name = node.__class__.__name__
        if hasattr(pydantic_ast, node_class_name):
            new_node_class = getattr(pydantic_ast, node_class_name)
            field_kwargs = {}
            for field_name in node._fields:
                field_value = getattr(node, field_name)
                match field_value:
                    case list() as list_of_nodes:
                        field_result = [
                            self.visit(each_node) for each_node in list_of_nodes
                        ]
                    case ast.AST() as single_ast_node:
                        field_result = self.visit(single_ast_node)
                    case _ as simple_value:
                        field_result = simple_value
                logger.debug(f"FIELD --> {field_name}: {field_result}")
                field_kwargs.update({field_name: field_result})
            ret = new_node_class(**field_kwargs)
            kwarg_debug = f"**{field_kwargs}" if field_kwargs else ""
            logger.debug(f"MODEL {node_class_name}({kwarg_debug})")
        else:
            ret = node
        return ret


def parse(*args, **kwargs):
    parsed = ast.parse(*args, **kwargs)
    return AST_to_pydantic().visit(parsed)
