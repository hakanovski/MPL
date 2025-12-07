"""
src/parser.py
Updated to support Arithmetic Expressions (PEMDAS).
"""
from dataclasses import dataclass
from typing import List, Optional, Any
from .lexer import Token, TokenType

# AST Nodes
@dataclass
class Stmt: pass
@dataclass
class Expr: pass

@dataclass
class Block(Stmt): statements: List[Stmt]
@dataclass
class Cycle(Stmt): frequency: Expr; body: Stmt
@dataclass
class Conditional(Stmt): condition: Expr; then_branch: Stmt; else_branch: Optional[Stmt] = None

@dataclass
class Invoke(Stmt): entity: str; params: List['Param']
@dataclass
class Bind(Stmt): name: str; value: Expr
@dataclass
class Summon(Stmt): module_name: str
@dataclass
class Circle(Stmt): body: Stmt
@dataclass
class Seal(Stmt): target: str
@dataclass
class Omen(Stmt): target: str
@dataclass
class Hex(Stmt): target: str; params: List['Param']
@dataclass
class Morph(Stmt): target: str; target_type: TokenType
@dataclass
class Pact(Stmt): target: str; request: Expr
@dataclass
class Banish(Stmt): target: str
@dataclass
class Purge(Stmt): target: Optional[str]
@dataclass
class Abyss(Stmt): message: Expr
@dataclass
class Echo(Stmt): message: Expr

@dataclass
class Literal(Expr): value: Any
@dataclass
class Variable(Expr): name: Token
@dataclass
class Binary(Expr): left: Expr; operator: Token; right: Expr
@dataclass
class Param: name: str; value: Expr

class ParserError(Exception): pass

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[Stmt]:
        statements = []
        while not self.is_at_end():
            stmt = self.declaration()
            if stmt: statements.append(stmt)
        return statements

    def declaration(self):
        try: return self.statement()
        except ParserError as e:
            print(f"Syntax Error: {e}"); return None

    def statement(self) -> Stmt:
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
        if self.match(TokenType.CYCLE): return self.cycle_stmt()
        if self.match(TokenType.IF): return self.if_stmt()
        if self.match(TokenType.LBRACE): return self.block()
        raise self.error(self.peek(), "Expect valid ritual command.")

    # --- Handlers ---
    def invoke_stmt(self):
        self.consume(TokenType.DOT, "Expect '.' after 'invoke'.")
        entity = self.consume(TokenType.IDENTIFIER, "Expect entity name.")
        self.consume(TokenType.LPAREN, "Expect '('.")
        params = [] if self.check(TokenType.RPAREN) else self.parameters()
        self.consume(TokenType.RPAREN, "Expect ')'.")
        return Invoke(entity.lexeme, params)

    def bind_stmt(self):
        name = self.consume(TokenType.IDENTIFIER, "Expect name.")
        self.consume(TokenType.TO, "Expect 'to'.")
        return Bind(name.lexeme, self.expression())

    def summon_stmt(self): return Summon(self.consume(TokenType.IDENTIFIER, "Expect lib.").lexeme)
    def circle_stmt(self): return Circle(self.statement())
    def seal_stmt(self): return Seal(self.consume(TokenType.IDENTIFIER, "Expect target.").lexeme)
    def omen_stmt(self): return Omen(self.consume(TokenType.IDENTIFIER, "Expect target.").lexeme)
    
    def hex_stmt(self):
        target = self.consume(TokenType.IDENTIFIER, "Expect target.")
        self.consume(TokenType.WITH, "Expect 'with'.")
        return Hex(target.lexeme, self.parameters())

    def morph_stmt(self):
        target = self.consume(TokenType.IDENTIFIER, "Expect target.")
        self.consume(TokenType.INTO, "Expect 'into'.")
        type_token = self.advance() # Assume valid type checked in lexer/runtime
        return Morph(target.lexeme, type_token.type)

    def pact_stmt(self):
        target = self.consume(TokenType.IDENTIFIER, "Expect target.")
        self.consume(TokenType.WITH, "Expect 'with'.")
        return Pact(target.lexeme, self.expression())

    def banish_stmt(self): return Banish(self.consume(TokenType.IDENTIFIER, "Expect target.").lexeme)
    
    def purge_stmt(self):
        target = self.previous().lexeme if self.match(TokenType.IDENTIFIER) else None
        return Purge(target)

    def abyss_stmt(self): return Abyss(self.expression())
    def echo_stmt(self): return Echo(self.expression())

    def cycle_stmt(self):
        self.consume(TokenType.LPAREN, "Expect '('."); freq = self.expression()
        self.consume(TokenType.RPAREN, "Expect ')'."); return Cycle(freq, self.statement())

    def if_stmt(self):
        cond = self.expression(); then = self.statement()
        els = self.statement() if self.match(TokenType.ELSE) else None
        return Conditional(cond, then, els)

    def block(self):
        stmts = []
        while not self.check(TokenType.RBRACE) and not self.is_at_end(): stmts.append(self.declaration())
        self.consume(TokenType.RBRACE, "Expect '}'.")
        return Block(stmts)

    def parameters(self):
        params = []
        while True:
            name = self.consume(TokenType.IDENTIFIER, "Expect param name.").lexeme
            self.consume(TokenType.ASSIGN, "Expect '='.")
            params.append(Param(name, self.expression()))
            if not self.match(TokenType.COMMA): break
        return params

    # --- Expressions (UPDATED FOR MATH) ---
    def expression(self): return self.equality()

    def equality(self):
        expr = self.comparison()
        while self.match(TokenType.EQ, TokenType.NEQ):
            expr = Binary(expr, self.previous(), self.comparison())
        return expr

    def comparison(self):
        expr = self.term() # UPDATED: Calls term() instead of primary()
        while self.match(TokenType.GT, TokenType.LT, TokenType.GTE, TokenType.LTE):
            expr = Binary(expr, self.previous(), self.term())
        return expr

    def term(self):
        # Handles Addition and Subtraction
        expr = self.factor()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            expr = Binary(expr, self.previous(), self.factor())
        return expr

    def factor(self):
        # Handles Multiplication and Division
        expr = self.primary()
        while self.match(TokenType.STAR, TokenType.SLASH):
            expr = Binary(expr, self.previous(), self.primary())
        return expr

    def primary(self):
        if self.match(TokenType.BOOLEAN, TokenType.NUMBER, TokenType.STRING): return Literal(self.previous().literal)
        if self.match(TokenType.IDENTIFIER): return Variable(self.previous())
        raise self.error(self.peek(), "Expect expression.")

    # Helpers
    def match(self, *types):
        for t in types:
            if self.check(t): self.advance(); return True
        return False
    def check(self, t): return False if self.is_at_end() else self.peek().type == t
    def advance(self):
        if not self.is_at_end(): self.current += 1
        return self.previous()
    def is_at_end(self): return self.peek().type == TokenType.EOF
    def peek(self): return self.tokens[self.current]
    def previous(self): return self.tokens[self.current - 1]
    def consume(self, t, msg):
        if self.check(t): return self.advance()
        raise self.error(self.peek(), msg)
    def error(self, token, msg): return ParserError(f"[Line {token.line}] {msg}")
