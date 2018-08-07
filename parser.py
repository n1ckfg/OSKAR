import sys
import traceback

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor, Node

def new_children(node, children):
    return Node(node.expr, node.full_text, node.start, node.end, children)

def is_empty(node):
    return node.expr.name == "_" or node.start == node.end

class OskarVisitor(NodeVisitor):
    def generic_visit(self, node, children):
        return new_children(node, [self.visit(n) for n in node])
        # return node

    def visit_start(self, node, children):
        return children[0] # children

    def visit_top_level(self, node, children):
        return children[0]

    def visit_function_definition(self, node, children):
        identifier, parameters, _, _, expression = children
        return new_children(node, [identifier, parameters, expression])

    def visit_identifier(self, node, children):
        _, symbol, _ = children
        return symbol

    def visit_parameter(self, node, children):
        identifier, default = children
        return new_children(node, [identifier] if is_empty(default) else [identifier, default])

    def visit_parameters(self, node, children):
        _, _, (parameters,), _, _ = children
        head, rest = parameters
        rest = map(lambda r: r.children[2], rest) # how to document what were skipping?
        return new_children(node, [head, *rest])

    def visit_expression(self, node, children):
        expression, _ = children
        return new_children(node, expression)

    def visit_operator(self, node, children):
        op, _ = children
        return new_children(node, [op])

# optional transform arguments?

with open("grammar.peg", "r") as f:
    grammar_source = f.read()
    grammar = Grammar(grammar_source)

with open(sys.argv[1], "r") as f:
    example_source = f.read().strip()
    parsed = grammar.parse(example_source)
    print(example_source)
    print(parsed)
