from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '1234567890'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
    
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    
    def generate_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in DIGITS or self.current_char == '.':
                tokens.append(self.generate_number())
            elif self.current_char == '+':
                self.advance()
                tokens.append(Token(TokenType.PLUS))
            elif self.current_char == '-':
                self.advance()
                tokens.append(Token(TokenType.MINUS))
            elif self.current_char == '*':
                self.advance()
                if self.current_char == '*':
                    self.advance()
                    tokens.append(Token(TokenType.EXPONENT))
                else:
                    tokens.append(Token(TokenType.MULTIPLY))
            elif self.current_char == '%':
                self.advance()
                tokens.append(Token(TokenType.MODULUS))
            elif self.current_char == '/':
                self.advance()
                tokens.append(Token(TokenType.DIVIDE))
            elif self.current_char == '(':
                self.advance()
                tokens.append(Token(TokenType.LPAREN))
            elif self.current_char == ')':
                self.advance()
                tokens.append(Token(TokenType.RPAREN))
            else:
                raise Exception(f"Illegal Character: '{self.current_char}'")
        
        return tokens 
    
    
    def generate_number(self):
        number_str = self.current_char
        self.advance()
        
        while self.current_char is not None and (self.current_char in DIGITS or self.current_char == '.'):
            number_str += self.current_char
            self.advance()
        
        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str = number_str + '0'
        
        return Token(TokenType.NUMBER, float(number_str))
