import unittest
import importlib

ejercicio2 = importlib.import_module("ejercicio2.solucion")


class TestEjercicio2(unittest.TestCase):
    def has_sumar_function(self):
        return hasattr(ejercicio2, "sumar")
    
    def test_sumar_function_exists(self):
        """Validar que exista la función 'sumar'."""
        self.assertTrue(self.has_sumar_function(), "La función 'sumar' no existe.")
        

    def test_suma(self):
        """Validar que la función 'sumar' retorne la suma correcta de dos números."""
        if not self.has_sumar_function():
            self.skipTest("La función 'sumar' no existe.")
        
        self.assertIsNotNone(ejercicio2.sumar(1, 1), "La función 'sumar' no debería retornar None.")
        self.assertEqual(ejercicio2.sumar(2, 3), 5, "La suma de 2 y 3 debería ser 5.")
        self.assertEqual(ejercicio2.sumar(-1, 1), 0, "La suma de -1 y 1 debería ser 0.")
        self.assertEqual(ejercicio2.sumar(0, 0), 0, "La suma de 0 y 0 debería ser 0.")