"""
src/main.py
====================================
The Entry Point (The Gate).
Reads the .ms file and initiates the interpretation process.
"""

import sys
import os
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter

def main():
    """
    The main ritual execution flow.
    Called when running 'mpl' from command line.
    """
    # 1. Argüman Kontrolü
    if len(sys.argv) < 2:
        print("🌙 MPL - Magick Programming Language v0.9.5")
        print("Usage: mpl run <ritual_file.ms>")
        return

    command = sys.argv[1]

    # 2. Komut: 'run'
    if command == "run" and len(sys.argv) >= 3:
        filename = sys.argv[2]
        
        if not os.path.exists(filename):
            print(f"⚠️ [ERROR] The scroll '{filename}' does not exist in this realm.")
            return

        print(f"🌙 MPL Interpreter Initialized. Loading '{filename}'...")

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                source_code = file.read()

            # --- The Pipeline ---
            lexer = Lexer(source_code)
            tokens = lexer.scan_tokens()
            
            # (Hata ayıklama için tokenleri görmek istersen burayı açabilirsin)
            # print(tokens) 
            
            parser = Parser(tokens)
            ast = parser.parse()
            
            print("📚 Magi Loaded.")
            print("⚡ Beginning Ritual Execution...")
            
            interpreter = Interpreter()
            interpreter.interpret(ast)
            
            print("✨ Ritual Concluded Successfully.")

        except Exception as e:
            print(f"💥 [BACKFIRE] Ritual Failed: {e}")
    
    # 3. Bilinmeyen Komut
    else:
        print(f"Unknown command: '{command}'. Try 'mpl run <file.ms>'")

if __name__ == "__main__":
    main()
