"""
src/lexer.py
====================================
The Lexer (Tokenizer) for MPL.
Updated to include Arithmetic Operators.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, List, Optional

class TokenType(Enum):
    # --- THE 13 SEALED VERBS ---
    INVOKE = auto(); BIND = auto(); SUMMON = auto()
    CIRCLE = auto(); SEAL = auto(); OMEN = auto()
    HEX = auto(); MORPH = auto(); PACT = auto()
    BANISH = auto(); PURGE = auto(); ABYSS = auto(); ECHO = auto()

    # --- Structural ---
    CYCLE = auto(); IF = auto(); ELSE = auto()
    TO = auto(); WITH = auto(); INTO = auto()
    
    # --- Types ---
    TYPE_SIGIL = auto(); TYPE_FLUX = auto()
    TYPE_MANA = auto(); TYPE_VESSEL = auto(); TYPE_VOID = auto()

    # --- Literals ---
    IDENTIFIER = auto(); STRING = auto(); NUMBER = auto(); BOOLEAN = auto()

    # --- Symbols & Operators ---
    DOT = auto(); COMMA = auto()
    LPAREN = auto(); RPAREN = auto(); LBRACE = auto(); RBRACE = auto()
    ASSIGN = auto(); ARROW = auto()
    
    # --- Arithmetic (NEW) ---
    PLUS = auto()   # +
    MINUS = auto()  # -
    STAR = auto()   # *
    SLASH = auto()  # /

    # --- Comparison ---
    EQ = auto(); NEQ = auto(); GT = auto(); LT = auto(); GTE = auto(); LTE = auto()

    EOF = auto()

@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: Any
    line: int
    def __repr__(self): return f"Token({self.type.name}, '{self.lexeme}', {self.literal})"

class LexerError(Exception): pass

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0; self.current = 0; self.line = 1
        self.keywords = {
            "invoke": TokenType.INVOKE, "bind": TokenType.BIND, "summon": TokenType.SUMMON,
            "circle": TokenType.CIRCLE, "seal": TokenType.SEAL, "omen": TokenType.OMEN,
            "hex": TokenType.HEX, "morph": TokenType.MORPH, "pact": TokenType.PACT,
            "banish": TokenType.BANISH, "purge": TokenType.PURGE, "abyss": TokenType.ABYSS,
            "echo": TokenType.ECHO, "cycle": TokenType.CYCLE, "if": TokenType.IF,
            "else": TokenType.ELSE, "to": TokenType.TO, "with": TokenType.WITH,
            "into": TokenType.INTO, "Sigil": TokenType.TYPE_SIGIL, "Flux": TokenType.TYPE_FLUX,
            "Mana": TokenType.TYPE_MANA, "Vessel": TokenType.TYPE_VESSEL, "Void": TokenType.TYPE_VOID,
            "True": TokenType.BOOLEAN, "False": TokenType.BOOLEAN
        }

    def scan_tokens(self) -> List[Token]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()

        if c == '(': self.add_token(TokenType.LPAREN)
        elif c == ')': self.add_token(TokenType.RPAREN)
        elif c == '{': self.add_token(TokenType.LBRACE)
        elif c == '}': self.add_token(TokenType.RBRACE)
        elif c == ',': self.add_token(TokenType.COMMA)
        elif c == '.': self.add_token(TokenType.DOT)
        
        # --- ARITHMETIC (UPDATED) ---
        elif c == '+': self.add_token(TokenType.PLUS)
        elif c == '*': self.add_token(TokenType.STAR)
        elif c == '/': self.add_token(TokenType.SLASH)
        elif c == '-':
            # Check for Arrow '->' or Minus '-'
            if self.match('>'): self.add_token(TokenType.ARROW)
            else: self.add_token(TokenType.MINUS)
            
        elif c == '=': self.add_token(TokenType.EQ if self.match('=') else TokenType.ASSIGN)
        elif c == '!': 
            if self.match('='): self.add_token(TokenType.NEQ)
            else: raise LexerError(f"Unexpected character '!' at line {self.line}")
        elif c == '<': self.add_token(TokenType.LTE if self.match('=') else TokenType.LT)
        elif c == '>': self.add_token(TokenType.GTE if self.match('=') else TokenType.GT)

        elif c in [' ', '\r', '\t']: pass
        elif c == '\n': self.line += 1
        elif c == '#':
            while self.peek() != '\n' and not self.is_at_end(): self.advance()
        elif c == '"': self.string()
        else:
            if c.isdigit(): self.number()
            elif self.is_alpha(c): self.identifier()
            else: raise LexerError(f"Unknown glyph '{c}' at line {self.line}")

    # Helpers
    def identifier(self):
        while self.is_alpha_numeric(self.peek()): self.advance()
        text = self.source[self.start : self.current]
        type_ = self.keywords.get(text, TokenType.IDENTIFIER)
        literal = True if text == "True" else (False if text == "False" else None)
        self.add_token(type_, literal)

    def number(self):
        while self.peek().isdigit(): self.advance()
        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance()
            while self.peek().isdigit(): self.advance()
        val = self.source[self.start : self.current]
        self.add_token(TokenType.NUMBER, float(val) if '.' in val else int(val))

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n': self.line += 1
            self.advance()
        if self.is_at_end(): raise LexerError("Unterminated string.")
        self.advance()
        val = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, val)

    def match(self, expected):
        if self.is_at_end() or self.source[self.current] != expected: return False
        self.current += 1; return True
    def peek(self): return '\0' if self.is_at_end() else self.source[self.current]
    def peek_next(self): return '\0' if self.current + 1 >= len(self.source) else self.source[self.current + 1]
    def advance(self): self.current += 1; return self.source[self.current - 1]
    def add_token(self, type_, literal=None): self.tokens.append(Token(type_, self.source[self.start : self.current], literal, self.line))
    def is_at_end(self): return self.current >= len(self.source)
    def is_alpha(self, c): return ('a'<=c<='z') or ('A'<=c<='Z') or c=='_'
    def is_alpha_numeric(self, c): return self.is_alpha(c) or c.isdigit()
