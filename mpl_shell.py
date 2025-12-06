"""
mpl_shell.py
====================================
The Interactive Shell (REPL).
Allows the Magi to cast spells directly from the terminal.
"""

import sys
from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter

def main():
    # Initialize the Runtime Engine
    interpreter = Interpreter()
    
    print("========================================")
    print("🔮 MPL (Magick Programming Language) v0.2.0")
    print("   The Portal is Open.")
    print("   Type 'exit' to close the connection.")
    print("========================================")

    while True:
        try:
            # 1. OMEN: Read input from the Mage
            text = input('mpl> ')
            
            if text.strip() == "exit":
                print("Closing portal...")
                break
            
            if not text.strip():
                continue

            # 2. LEXER: Break into tokens
            lexer = Lexer(text)
            tokens = lexer.scan_tokens()
            
            # Debug: Uncomment to see raw tokens
            # print(f"Tokens: {tokens}")

            # 3. PARSER: Build the AST
            parser = Parser(tokens)
            statements = parser.parse()
            
            if not statements:
                continue

            # 4. INTERPRETER: Execute the Ritual
            interpreter.interpret(statements)

        except KeyboardInterrupt:
            print("\nConnection interrupted.")
            break
        except Exception as e:
            print(f"🌑 Abyss Error: {e}")

if __name__ == '__main__':
    main()
