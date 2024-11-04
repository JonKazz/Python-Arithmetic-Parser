from nodes import *

class Interpreter:
    def visit(self, node):
        if isinstance(node, NumberNode):
            return self.visit_NumberNode(node)
        elif isinstance(node, AddNode):
            return self.visit_AddNode(node)
        elif isinstance(node, SubtractNode):
            return self.visit_SubtractNode(node)
        elif isinstance(node, MultiplyNode):
            return self.visit_MultiplyNode(node)
        elif isinstance(node, DivideNode):
            return self.visit_DivideNode(node)
        elif isinstance(node, ModulusNode):
            return self.visit_ModulusNode(node)
        elif isinstance(node, ExponentNode):
            return self.visit_ExponentNode(node)
        elif isinstance(node, PlusNode):
            return self.visit_PlusNode(node)
        elif isinstance(node, MinusNode):
            return self.visit_MinusNode(node)
        else:
            raise Exception(f"No visit method defined for node type: {type(node).__name__}")

    def visit_NumberNode(self, node):
        return node.value

    def visit_AddNode(self, node):
        return self.visit(node.node_a) + self.visit(node.node_b)
    
    def visit_SubtractNode(self, node):
        return self.visit(node.node_a) - self.visit(node.node_b)
    
    def visit_MultiplyNode(self, node):
        return self.visit(node.node_a) * self.visit(node.node_b)
    
    def visit_DivideNode(self, node):
        try:
            return self.visit(node.node_a) / self.visit(node.node_b)
        except:
            raise Exception("Divide by Zero Error")
    
    def visit_ModulusNode(self, node):
        try:
            return self.visit(node.node_a) % self.visit(node.node_b)
        except:
            raise Exception("Divide by Zero Error")
    
    def visit_ExponentNode(self, node):
        return self.visit(node.node_a) ** self.visit(node.node_b)
    
    def visit_PlusNode(self, node):
        return self.visit(node.node)
    
    def visit_MinusNode(self, node):
        return -self.visit(node.node)