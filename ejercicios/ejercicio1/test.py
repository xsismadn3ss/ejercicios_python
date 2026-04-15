import unittest
import importlib

ejercicio1 = importlib.import_module("ejercicio1.solucion")


class TestEjercicio1(unittest.TestCase):
    def test_exitencia_funcion(self):
        """Validar si la función suma existe en el modulo"""

        self.assertTrue(
            hasattr(ejercicio1, "sumar"),
            "La función sumar no existe en el módulo ejercicio1.solucion"
        )

    def test_suma_positiva(self):
        """Validar la suma de dos números positivos"""

        resultado = ejercicio1.sumar(2, 3)
        self.assertEqual(resultado, 5)

    def test_suma_negativa(self):
        """Validar la suma de dos números negativos"""

        resultado = ejercicio1.sumar(-2, -3)
        self.assertEqual(resultado, -5)