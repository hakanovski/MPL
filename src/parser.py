"""
src/parser.py
====================================
The Parser (Architect).
It takes a list of Tokens from the Lexer and constructs an Abstract Syntax Tree (AST).
This transforms a flat list of words into a structured hierarchy of 13 Sealed Actions.
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

# --- Structural Statements ---

@dataclass
class Block(Stmt):
    statements: List[Stmt]

@dataclass
class Cycle(Stmt):
    frequency: Expr  # The loop count (Standard or Resonant 3-6-9)
    body: Stmt

@dataclass
class Conditional(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Optional[Stmt] = None

# --- The 13 Sealed Actions (Nodes) ---

@dataclass
class Invoke(Stmt):
    entity: str
    params: List['Param']

@dataclass
class Bind(Stmt):
    name: str
    value: Expr

@dataclass
class Summon(Stmt):
    module_name: str

@dataclass
class Circle(Stmt):
    body: Stmt  # The protected block (try/catch equivalent)

@dataclass
class Seal(Stmt):
    target: str # Variable to lock/protect

@dataclass
class Omen(Stmt):
    target: str # Variable to store the read data into

@dataclass
class Hex(Stmt):
    target: str
    params: List['Param']

@dataclass
class Morph(Stmt):
    target: str
    target_type: TokenType

@dataclass
class Pact(Stmt):
    target: str
    request: Expr

@dataclass
class Banish(Stmt):
    target: str

@dataclass
class Purge(Stmt):
    target: Optional[str] = None # If None, clear everything

@dataclass
class Abyss(Stmt):
    message: Expr

@dataclass
class Echo(Stmt):
    message: Expr

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
            # In a production compiler, we would synchronize here.
            print(f"Syntax Error: {e}")
            return None

    def statement(self) -> Stmt:
        # --- Dispatcher for The 13 Sealed Verbs ---
        if self.match(TokenType.INVOKE): return self.invoke_stmt()
        if self.match(TokenType.BIND): return self.bind_stmt()
        if self.match(TokenType.SUMMON): return self.summon_stmt()
        if self.match(TokenType.CIRCLE): return self.circle_stmt()
        if self.match(TokenType.SEAL): return self.seal_stmt()
        if self.match(TokenType.OMEN): return self.omen_stmt()
        if self.match(TokenType.HEX): return self.hex_stmt()
        if self.match(TokenType.MORPH): return self.morph_stmt()
        if self.match(TokenType.PACT): return self.pact_stmt()
        if self.match(TokenType.BANISH): return self.banish_stmt()
        if self.match(TokenType.PURGE): return self.purge_stmt()
        if self.match(TokenType.ABYSS): return self.abyss_stmt()
        if self.match(TokenType.ECHO): return self.echo_stmt()

        # --- Structural ---
        if self.match(TokenType.CYCLE): return self.cycle_stmt()
        if self.match(TokenType.IF): return self.if_stmt()
        if self.match(TokenType.LBRACE): return self.block()

        raise self.error(self.peek(), "Expect valid ritual command.")

    # --- Statement Handlers ---

    def invoke_stmt(self) -> Stmt:
        # invoke . entity ( params )
        self.consume(TokenType.DOT, "Expect '.' after 'invoke'.")
        entity = self.consume(TokenType.IDENTIFIER, "Expect entity name.")
        self.consume(TokenType.LPAREN, "Expect '(' after entity.")
        params = []
        if not self.check(TokenType.RPAREN):
            params = self.parameters()
        self.consume(TokenType.RPAREN, "Expect ')' after parameters.")
        return Invoke(entity.lexeme, params)

    def bind_stmt(self) -> Stmt:
        # bind name to value
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        self.consume(TokenType.TO, "Expect 'to' assignment.")
        value = self.expression()
        return Bind(name.lexeme, value)

    def summon_stmt(self) -> Stmt:
        # summon library_name
        module = self.consume(TokenType.IDENTIFIER, "Expect library name to summon.")
        return Summon(module.lexeme)

    def circle_stmt(self) -> Stmt:
        # circle { statements }
        # Used for error handling / safe execution
        body = self.statement() # Expects a block
        return Circle(body)

    def seal_stmt(self) -> Stmt:
        # seal variable_name
        target = self.consume(TokenType.IDENTIFIER, "Expect variable to seal.")
        return Seal(target.lexeme)

    def omen_stmt(self) -> Stmt:
        # omen variable_name
        # Reads input/system data into the variable
        target = self.consume(TokenType.IDENTIFIER, "Expect variable to receive the omen.")
        return Omen(target.lexeme)

    def hex_stmt(self) -> Stmt:
        # hex target with params
        target = self.consume(TokenType.IDENTIFIER, "Expect target to hex.")
        self.consume(TokenType.WITH, "Expect 'with' params.")
        params = self.parameters()
        return Hex(target.lexeme, params)

    def morph_stmt(self) -> Stmt:
        # morph target into Type
        target = self.consume(TokenType.IDENTIFIER, "Expect target to morph.")
        self.consume(TokenType.INTO, "Expect 'into'.")
        
        valid_types = [TokenType.TYPE_SIGIL, TokenType.TYPE_MANA, TokenType.TYPE_FLUX, TokenType.TYPE_VESSEL]
        if self.peek().type in valid_types:
            target_type = self.advance().type
        else:
            raise self.error(self.peek(), "Expect valid element type (Sigil, Mana, Flux, Vessel).")
            
        return Morph(target.lexeme, target_type)

    def pact_stmt(self) -> Stmt:
        # pact target with request
        target = self.consume(TokenType.IDENTIFIER, "Expect entity/url for pact.")
        self.consume(TokenType.WITH, "Expect 'with' request data.")
        request = self.expression()
        return Pact(target.lexeme, request)

    def banish_stmt(self) -> Stmt:
        # banish target
        target = self.consume(TokenType.IDENTIFIER, "Expect target to banish.")
        return Banish(target.lexeme)

    def purge_stmt(self) -> Stmt:
        # purge (optional target)
        target = None
        if self.match(TokenType.IDENTIFIER):
            target = self.previous().lexeme
        return Purge(target)

    def abyss_stmt(self) -> Stmt:
        # abyss "Error Message"
        msg = self.expression()
        return Abyss(msg)

    def echo_stmt(self) -> Stmt:
        # echo expression
        msg = self.expression()
        return Echo(msg)

    # --- Structural Handlers ---

    def cycle_stmt(self) -> Stmt:
        self.consume(TokenType.LPAREN, "Expect '(' after cycle.")
        freq = self.expression()
        self.consume(TokenType.RPAREN, "Expect ')' after frequency.")
        body = self.statement()
        return Cycle(freq, body)

    def if_stmt(self) -> Stmt:
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
        # Support loose parameter format for now (identifier = expr)
        while True:
            # Break if next token is NOT an identifier (safety check)
            if not self.check(TokenType.IDENTIFIER):
                break
                
            name = self.consume(TokenType.IDENTIFIER, "Expect parameter name.")
            self.consume(TokenType.ASSIGN, "Expect '='.")
            value = self.expression()
            params.append(Param(name.lexeme, value))
            
            if not self.match(TokenType.COMMA):
                break
        return params

    # --- Expression Logic ---

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
        if self.match(TokenType.GT, TokenType.LT, TokenType.GTE, TokenType.LTE):
            operator = self.previous()
            right = self.primary()
            expr = Binary(expr, operator, right)
        return expr

    def primary(self) -> Expr:
        if self.match(TokenType.BOOLEAN): return Literal(self.previous().literal)
        if self.match(TokenType.NUMBER): return Literal(self.previous().literal)
        if self.match(TokenType.STRING): return Literal(self.previous().literal)
        if self.match(TokenType.IDENTIFIER): return Variable(self.previous())
        
        raise self.error(self.peek(), "Expect expression.")

    # --- Helper Methods ---

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
