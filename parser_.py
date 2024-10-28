from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
        
    def raise_error(self):
        raise Exception("Invalid Syntax")
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def parse(self):
        if self.current_token is None:
            return None
        
        result = self.expression()
        
        if self.current_token is not None:
            self.raise_error()
            
        return result
    
    # Addition and Subtraction (Precedence #4)
    def expression(self):
        result = self.term()
        
        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())
        return result
    
    # Multiplication, Division, and Modulus (Precedence #3)
    def term(self):
        result = self.factor()
        
        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULUS):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())
            elif self.current_token.type == TokenType.MODULUS:
                self.advance()
                result = ModulusNode(result, self.factor())
        return result

    # Exponentiation (Precedence #2)
    def factor(self):
        result = self.primary()
        while self.current_token is not None and self.current_token.type == TokenType.EXPONENT:
            self.advance()
            result = ExponentNode(result, self.primary())
        return result

    # Parenthesis and Unary (Precedence #1)
    def primary(self):
        token = self.current_token
        
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expression()
            
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.primary())
        
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.primary())
        
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        else:
            self.raise_error()
            
