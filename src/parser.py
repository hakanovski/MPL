"""
src/parser.py
====================================
The Parser.
It takes a list of Tokens from the Lexer and constructs an Abstract Syntax Tree (AST).
This transforms a flat list of words into a structured hierarchy of intent.
"""

from dataclasses import dataclass
from typing import List, Optional, Any
from .lexer import Token, TokenType

# ==========================================
# AST NODES (The Shape of the Ritual)
# ==========================================

@dataclass
class Stmt:
    """Base class for all Statements."""
    pass

@dataclass
class Expr:
    """Base class for all Expressions."""
    pass

# --- Statements ---

@dataclass
class Block(Stmt):
    statements: List[Stmt]

@dataclass
class Invocation(Stmt):
    entity: str
    params: List['Param']

@dataclass
class Binding(Stmt):
    name: str
    value: Expr

@dataclass
class Cycle(Stmt):
    frequency: Expr  # The loop count (Standard or Resonant 3-6-9)
    body: Stmt

@dataclass
class Transmutation(Stmt):
    target: str
    target_type: str

@dataclass
class Conditional(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Optional[Stmt] = None

@dataclass
class Casting(Stmt):
    spell_name: str
    params: List['Param']

# --- Expressions ---

@dataclass
class Literal(Expr):
    value: Any

@dataclass
class Variable(Expr):
    name: Token

@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

@dataclass
class Param:
    name: str
    value: Expr

# ==========================================
# THE PARSER (The Architect)
# ==========================================

class ParserError(Exception):
    """Raised when the ritual syntax is violated."""
    pass

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[Stmt]:
        """
        The main entry point. Converts tokens into a list of statements.
        """
        statements = []
        while not self.is_at_end():
            stmt = self.declaration()
            if stmt:
                statements.append(stmt)
        return statements

    def declaration(self) -> Optional[Stmt]:
        try:
            return self.statement()
        except ParserError as e:
            # In a full compiler, we might synchronize here to recover.
            # For now, we stop at the first error.
            print(f"Syntax Error: {e}")
            return None

    def statement(self) -> Stmt:
        if self.match(TokenType.INVOKE):
            return self.invocation_statement()
        if self.match(TokenType.BIND):
            return self.binding_statement()
        if self.match(TokenType.CYCLE):
            return self.cycle_statement()
        if self.match(TokenType.TRANSMUTE):
            return self.transmutation_statement()
        if self.match(TokenType.CAST):
            return self.casting_statement()
        if self.match(TokenType.IF):
            return self.if_statement()
        if self.match(TokenType.LBRACE):
            return self.block()
        
        # If no statement matches, it might be an expression statement
        # (For now, we enforce statements strictly)
        raise self.error(self.peek(), "Expect valid ritual statement (invoke, bind, cycle, etc.)")

    # --- Statement Handlers ---

    def invocation_statement(self) -> Stmt:
        # Grammar: invoke . entity ( params )
        self.consume(TokenType.DOT, "Expect '.' after 'invoke'.")
        entity_token = self.consume(TokenType.IDENTIFIER, "Expect entity name after '.'.")
        
        self.consume(TokenType.LPAREN, "Expect '(' after entity name.")
        params = []
        if not self.check(TokenType.RPAREN):
            params = self.parameters()
        self.consume(TokenType.RPAREN, "Expect ')' after parameters.")
        
        return Invocation(entity_token.lexeme, params)

    def binding_statement(self) -> Stmt:
        # Grammar: bind name to value
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        self.consume(TokenType.TO, "Expect 'to' after variable name.")
        value = self.expression()
        return Binding(name.lexeme, value)

    def cycle_statement(self) -> Stmt:
        # Grammar: cycle ( frequency ) { ... }
        self.consume(TokenType.LPAREN, "Expect '(' after 'cycle'.")
        frequency = self.expression() # This will be the number (3, 6, 9, or other)
        self.consume(TokenType.RPAREN, "Expect ')' after cycle frequency.")
        
        body = self.statement() # Usually a Block
        return Cycle(frequency, body)

    def transmutation_statement(self) -> Stmt:
        # Grammar: transmute target -> type
        target = self.consume(TokenType.IDENTIFIER, "Expect target variable.")
        self.consume(TokenType.ARROW, "Expect '->' operator.")
        
        # Expect a Type Token (Sigil, Mana, etc.)
        if self.match(TokenType.TYPE_SIGIL, TokenType.TYPE_MANA, TokenType.TYPE_FLUX, TokenType.TYPE_VESSEL):
            target_type = self.previous().lexeme
        else:
            raise self.error(self.peek(), "Expect valid type (Sigil, Mana, Flux, Vessel).")
            
        return Transmutation(target.lexeme, target_type)

    def casting_statement(self) -> Stmt:
        # Grammar: cast spell_name [with params]
        spell = self.consume(TokenType.IDENTIFIER, "Expect spell name.")
        params = []
        if self.match(TokenType.WITH):
            params = self.parameters()
        return Casting(spell.lexeme, params)

    def if_statement(self) -> Stmt:
        # Grammar: if condition block [else block]
        condition = self.expression()
        then_branch = self.statement()
        else_branch = None
        if self.match(TokenType.ELSE):
            else_branch = self.statement()
        return Conditional(condition, then_branch, else_branch)

    def block(self) -> Stmt:
        statements = []
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            statements.append(self.declaration())
        
        self.consume(TokenType.RBRACE, "Expect '}' after block.")
        return Block(statements)

    def parameters(self) -> List[Param]:
        params = []
        while True:
            name = self.consume(TokenType.IDENTIFIER, "Expect parameter name.")
            self.consume(TokenType.ASSIGN, "Expect '=' after parameter name.")
            value = self.expression()
            params.append(Param(name.lexeme, value))
            
            if not self.match(TokenType.COMMA):
                break
        return params

    # --- Expression Handlers (Simplified for 0.1.0) ---

    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        expr = self.comparison()
        while self.match(TokenType.EQ, TokenType.NEQ):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self) -> Expr:
        expr = self.primary()
        # Handle basic comparison logic if needed
        # For now, sticking to simple expressions
        return expr

    def primary(self) -> Expr:
        if self.match(TokenType.BOOLEAN): return Literal(self.previous().literal)
        if self.match(TokenType.NUMBER): return Literal(self.previous().literal)
        if self.match(TokenType.STRING): return Literal(self.previous().literal)
        if self.match(TokenType.IDENTIFIER): return Variable(self.previous())
        
        raise self.error(self.peek(), "Expect expression.")

    # --- Helpers ---

    def match(self, *types: TokenType) -> bool:
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False

    def check(self, type_: TokenType) -> bool:
        if self.is_at_end(): return False
        return self.peek().type == type_

    def advance(self) -> Token:
        if not self.is_at_end(): self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def consume(self, type_: TokenType, message: str) -> Token:
        if self.check(type_): return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token: Token, message: str) -> ParserError:
        location = "at end" if token.type == TokenType.EOF else f"at '{token.lexeme}'"
        return ParserError(f"[Line {token.line}] Error {location}: {message}")

