import unittest
import sys
import os

# Add the project root to the Python path so the 'src' folder can be found.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter

class TestMPLEngine(unittest.TestCase):
    """
    🛡️ THE PROTECTION CIRCLE (Unit Tests)
    Verifies that the Magick Engine performs logical operations correctly.
    """

    def setUp(self):
        """Creates a fresh Interpreter instance before each test."""
        self.interpreter = Interpreter()

    def run_script(self, code):
        """
        Takes raw MPL source code (string), executes the pipeline (Lexer -> Parser -> Interpreter),
        and returns the final state of the Environment (Memory).
        """
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.interpreter.interpret(ast)
        return self.interpreter.environment

    def test_bind_variable(self):
        """TEST 1: Does variable assignment (Bind) work?"""
        code = 'bind mana to 100'
        env = self.run_script(code)
        
        # Expectation: The variable 'mana' must exist in memory with the value 100.
        self.assertIn('mana', env.values) 
        self.assertEqual(env.values['mana'], 100)
        print("✅ [TEST] Binding Spell Passed.")

    def test_math_operations(self):
        """TEST 2: Do Alchemy (Math) operations work?"""
        code = 'bind result to 33 + 10'
        env = self.run_script(code)
        
        # Expectation: 33 + 10 should equal 43.
        self.assertEqual(env.values['result'], 43)
        print("✅ [TEST] Alchemy (Math) Passed.")

    def test_string_concatenation(self):
        """TEST 3: Does String Weaving work?"""
        code = 'bind greeting to "Hello" + " World"'
        env = self.run_script(code)
        
        # Expectation: Strings should be joined correctly.
        self.assertEqual(env.values['greeting'], "Hello World")
        print("✅ [TEST] String Weaving Passed.")

if __name__ == '__main__':
    print("⚡ [TESTING] Initiating Safety Seals...")
    unittest.main()
