"""
src/lexer.py
====================================
The Lexer (Tokenizer) for MPL.
Responsible for breaking down raw ritual scripts into meaningful Tokens.
This constitutes the first stage of the Magic Runtime Engine (MRE).
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, List, Optional

class TokenType(Enum):
    # --- THE 13 SEALED VERBS (Core Actions) ---
    INVOKE = auto()   # Execute functions/rituals
    BIND = auto()     # Assign variables
    SUMMON = auto()   # Import modules/libraries
    CIRCLE = auto()   # Error handling block (try/catch)
    SEAL = auto()     # Make immutable / Protect data
    OMEN = auto()     # Read input / System signals
    HEX = auto()      # Manipulate/Set properties
    MORPH = auto()    # Type conversion (casting)
    PACT = auto()     # Network/API requests
    BANISH = auto()   # Delete/Destroy variables
    PURGE = auto()    # Clear buffers/memory
    ABYSS = auto()    # Raise exceptions
    ECHO = auto()     # Output to console (print)

    # --- Structural Keywords ---
    CYCLE = auto()    # Loops (Tesla Protocol)
    IF = auto()       # Conditional
    ELSE = auto()     # Conditional fallback
    TO = auto()       # Preposition (bind x TO y)
    WITH = auto()     # Preposition (invoke x WITH params)
    INTO = auto()     # Preposition (morph x INTO y)
    
    # --- Data Types (The Elements) ---
    TYPE_SIGIL = auto()   # String
    TYPE_FLUX = auto()    # Float
    TYPE_MANA = auto()    # Integer
    TYPE_VESSEL = auto()  # Dictionary/Object
    TYPE_VOID = auto()    # NoneType

    # --- Literals ---
    IDENTIFIER = auto()   # Variable/Function names
    STRING = auto()       # "text"
    NUMBER = auto()       # 123, 3.14
    BOOLEAN = auto()      # True, False

    # --- Symbols & Operators ---
    DOT = auto()          # .
    COMMA = auto()        # ,
    LPAREN = auto()       # (
    RPAREN = auto()       # )
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    ASSIGN = auto()       # =
    ARROW = auto()        # ->
    
    # --- Comparison Operators ---
    EQ = auto()           # ==
    NEQ = auto()          # !=
    GT = auto()           # >
    LT = auto()           # <
    GTE = auto()          # >=
    LTE = auto()          # <=

    # --- End of File ---
    EOF = auto()

@dataclass
class Token:
    """
    Represents a single atomic unit of the language.
    """
    type: TokenType
    lexeme: str
    literal: Any
    line: int

    def __repr__(self):
        return f"Token({self.type.name}, '{self.lexeme}', {self.literal})"

class LexerError(Exception):
    """Raised when the Lexer encounters forbidden runes."""
    pass

class Lexer:
    """
    Scans the raw source code (ritual) and produces a list of Tokens.
    """
    
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1

        # Keywords mapping (The Words of Power)
        self.keywords = {
            # Actions
            "invoke": TokenType.INVOKE,
            "bind": TokenType.BIND,
            "summon": TokenType.SUMMON,
            "circle": TokenType.CIRCLE,
            "seal": TokenType.SEAL,
            "omen": TokenType.OMEN,
            "hex": TokenType.HEX,
            "morph": TokenType.MORPH,
            "pact": TokenType.PACT,
            "banish": TokenType.BANISH,
            "purge": TokenType.PURGE,
            "abyss": TokenType.ABYSS,
            "echo": TokenType.ECHO,

            # Structure
            "cycle": TokenType.CYCLE,
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "to": TokenType.TO,
            "with": TokenType.WITH,
            "into": TokenType.INTO,

            # Types
            "Sigil": TokenType.TYPE_SIGIL,
            "Flux": TokenType.TYPE_FLUX,
            "Mana": TokenType.TYPE_MANA,
            "Vessel": TokenType.TYPE_VESSEL,
            "Void": TokenType.TYPE_VOID,
            
            # Booleans
            "True": TokenType.BOOLEAN,
            "False": TokenType.BOOLEAN,
        }

    def scan_tokens(self) -> List[Token]:
        """
        The main ritual loop. Scans tokens until EOF is reached.
        """
        while not self.is_at_end():
            # We are at the beginning of the next lexeme.
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        """
        Recognizes the next character and decides which Token it belongs to.
        """
        c = self.advance()

        # Handle Single-Character Tokens
        if c == '(': self.add_token(TokenType.LPAREN)
        elif c == ')': self.add_token(TokenType.RPAREN)
        elif c == '{': self.add_token(TokenType.LBRACE)
        elif c == '}': self.add_token(TokenType.RBRACE)
        elif c == ',': self.add_token(TokenType.COMMA)
        elif c == '.': self.add_token(TokenType.DOT)
        
        # Handle Operators and Two-Character Tokens
        elif c == '-':
            # Check for Arrow '->'
            if self.match('>'):
                self.add_token(TokenType.ARROW)
            else:
                raise LexerError(f"Unexpected character '-' at line {self.line}. Did you mean '->'?")
        elif c == '=':
            self.add_token(TokenType.EQ if self.match('=') else TokenType.ASSIGN)
        elif c == '!':
            if self.match('='): self.add_token(TokenType.NEQ)
            else: raise LexerError(f"Unexpected character '!' at line {self.line}")
        elif c == '<':
            self.add_token(TokenType.LTE if self.match('=') else TokenType.LT)
        elif c == '>':
            self.add_token(TokenType.GTE if self.match('=') else TokenType.GT)

        # Handle Whitespace
        elif c in [' ', '\r', '\t']:
            pass # Ignore whitespace
        elif c == '\n':
            self.line += 1

        # Handle Comments
        elif c == '#':
            while self.peek() != '\n' and not self.is_at_end():
                self.advance()

        # Handle String Literals
        elif c == '"':
            self.string()

        # Handle Numbers, Identifiers, Keywords
        else:
            if c.isdigit():
                self.number()
            elif self.is_alpha(c):
                self.identifier()
            else:
                raise LexerError(f"Unknown glyph '{c}' at line {self.line}")

    # --- Helper Methods ---

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        
        text = self.source[self.start : self.current]
        type_ = self.keywords.get(text, TokenType.IDENTIFIER)
        
        # Determine boolean literal value
        literal = None
        if type_ == TokenType.BOOLEAN:
            literal = True if text == "True" else False
            
        self.add_token(type_, literal)

    def number(self):
        while self.peek().isdigit():
            self.advance()

        # Look for fractional part
        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance() # Consume the "."
            while self.peek().isdigit():
                self.advance()
        
        value_str = self.source[self.start : self.current]
        # Convert to float if dot exists, else int
        if '.' in value_str:
            self.add_token(TokenType.NUMBER, float(value_str))
        else:
            self.add_token(TokenType.NUMBER, int(value_str))

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.is_at_end():
            raise LexerError("Unterminated string.")

        self.advance() # The closing "
        
        # Trim quotes
        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value)

    def match(self, expected: str) -> bool:
        if self.is_at_end(): return False
        if self.source[self.current] != expected: return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.is_at_end(): return '\0'
        return self.source[self.current]
    
    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]

    def advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def add_token(self, type_: TokenType, literal: Any = None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type_, text, literal, self.line))

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def is_alpha(self, c: str) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

    def is_alpha_numeric(self, c: str) -> bool:
        return self.is_alpha(c) or c.isdigit()
