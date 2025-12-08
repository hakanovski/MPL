import unittest
import sys
import os

# Ana dizini (root) Python yoluna ekle ki 'src' klasörünü bulabilsin.
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
        """Her testten önce taze bir Interpreter yaratır."""
        self.interpreter = Interpreter()

    def run_script(self, code):
        """MPL kodunu (string) alır, işler ve motorun son halini döndürür."""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.interpreter.interpret(ast)
        return self.interpreter.environment

    def test_bind_variable(self):
        """TEST 1: Değişken atama (Bind) çalışıyor mu?"""
        code = 'bind mana to 100'
        env = self.run_script(code)
        
        # Beklenti: Hafızada 'mana' değeri 100 olmalı.
        # MPL değişkenleri Token objesi olarak saklayabilir, bu yüzden ismine göre çekiyoruz.
        # Not: Interpreter yapımıza göre environment.values sözlüğüne bakacağız.
        
        # Basit kontrol: Değerler sözlüğünde 'mana' var mı?
        # (Not: Senin Interpreter yapında environment.values direkt string key kullanıyorsa:)
        self.assertIn('mana', env.values) 
        self.assertEqual(env.values['mana'], 100)
        print("✅ [TEST] Binding Spell Passed.")

    def test_math_operations(self):
        """TEST 2: Matematik (Simya) çalışıyor mu?"""
        code = 'bind result to 33 + 10'
        env = self.run_script(code)
        
        self.assertEqual(env.values['result'], 43)
        print("✅ [TEST] Alchemy (Math) Passed.")

    def test_string_concatenation(self):
        """TEST 3: Kelime birleştirme çalışıyor mu?"""
        code = 'bind greeting to "Hello" + " World"'
        env = self.run_script(code)
        
        self.assertEqual(env.values['greeting'], "Hello World")
        print("✅ [TEST] String Weaving Passed.")

if __name__ == '__main__':
    print("⚡ [TESTING] Initiating Safety Seals...")
    unittest.main()
