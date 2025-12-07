"""
src/main.py
====================================
The Entry Point (The Gate).
Initializes the Resolver, Lexer, Parser, and Interpreter.
Usage: python src/main.py <ritual_file.ms>
"""

import sys
import os
import argparse
from resolver import Resolver, OntologyError
from lexer import Lexer, LexerError
from parser import Parser, ParserError
from interpreter import Interpreter, RuntimeException

def main():
    # 1. Setup Arguments (Dosya yolunu al)
    parser = argparse.ArgumentParser(description="MPL (Magick Programming Language) Interpreter v0.9.0")
    parser.add_argument("file", help="The path to the .ms ritual file to execute")
    parser.add_argument("--debug", action="store_true", help="Show AST and Token streams")
    
    args = parser.parse_args()
    
    # Dosya var mı kontrol et
    if not os.path.exists(args.file):
        print(f"❌ Error: Ritual file '{args.file}' not found.")
        sys.exit(1)

    # 2. Read Source Code (Dosyayı oku)
    with open(args.file, "r", encoding="utf-8") as f:
        source_code = f.read()

    print(f"🌙 MPL Interpreter Initialized. Loading '{args.file}'...")

    try:
        # 3. Load Knowledge (Ontology & Goetia)
        # Resolver'ı iki veritabanı ile başlatıyoruz
        # Not: Dosya yollarının 'data' klasöründe olduğundan emin ol
        resolver = Resolver(
            magi_path="data/MAGI_225.json",
            solomon_path="data/72_solomon_sigil_shapes.json"
        )
        
        # 4. Lexical Analysis (Tokenization)
        lexer = Lexer(source_code)
        tokens = lexer.scan_tokens()
        
        if args.debug:
            print("\n--- [DEBUG] TOKENS ---")
            for t in tokens: print(t)
            print("----------------------\n")

        # 5. Parsing (AST Construction)
        parser_instance = Parser(tokens)
        statements = parser_instance.parse()

        if not statements:
            print("⚠️ The ritual contains no valid statements.")
            sys.exit(0)

        # 6. Execution (Interpretation)
        interpreter = Interpreter()
        
        # Resolver'ı Interpreter'a enjekte et (Bilgiyi aktar)
        interpreter.resolver = resolver 
        
        print("⚡ Beginning Ritual Execution...\n")
        interpreter.interpret(statements)
        print("\n✨ Ritual Concluded Successfully.")

    except LexerError as e:
        print(f"🛑 [LEXER ERROR] {e}")
    except ParserError as e:
        print(f"🛑 [PARSER ERROR] {e}")
    except RuntimeException as e:
        print(f"💥 [RUNTIME ERROR] {e}")
    except Exception as e:
        print(f"💀 [FATAL ERROR] An unhandled spirit crashed the engine: {e}")

if __name__ == "__main__":
    main()
