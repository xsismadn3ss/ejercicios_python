import importlib
import unittest


class TestEjercicio4(unittest.TestCase):
    def setUp(self):
        self.ejercicio4 = importlib.import_module("ejercicio4.solucion")

    def test_numero_mayor_fn_exists(self):
        """Validar que la funcion numero_mayor existe"""
        self.assertTrue(
            hasattr(self.ejercicio4, "numero_mayor"),
            "La función numero_mayor no existe",
        )

    def test_numero_mayor(self):
        """Validar funcionamiento de la funcion numero_mayor"""
        if not hasattr(self.ejercicio4, "numero_mayor"):
            self.skipTest("La función numero_mayor no existe")

        self.assertEqual(self.ejercicio4.numero_mayor([1, 2, 3, 4, 5]), 5)
        self.assertEqual(self.ejercicio4.numero_mayor([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(self.ejercicio4.numero_mayor([0, 0, 0, 0]), 0)
        self.assertEqual(self.ejercicio4.numero_mayor([10, 20, 30, 40, 50]), 50)
