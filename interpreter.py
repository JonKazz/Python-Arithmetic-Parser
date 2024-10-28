from nodes import *

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

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