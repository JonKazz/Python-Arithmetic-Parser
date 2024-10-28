from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER   = 0
    PLUS     = 1
    MINUS    = 2
    MULTIPLY = 3
    DIVIDE   = 4
    MODULUS  = 5
    EXPONENT = 6
    LPAREN   = 7
    RPAREN   = 8
    

@dataclass
class Token:
    type: TokenType
    value: any = None
    
    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
