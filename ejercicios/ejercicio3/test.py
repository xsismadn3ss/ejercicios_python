import importlib
import unittest

ejercicio3 = importlib.import_module("ejercicio3.solucion")


class TestEjercicio3(unittest.TestCase):
    def test_es_par_fn_existance(self):
        """Validar que exista la función es_par"""
        self.assertTrue(hasattr(ejercicio3, "es_par"), "La función es_par no existe")

    def test_es_par_fn(self):
        '''Validar funcionamiento de la función es_par'''

        if not hasattr(ejercicio3, "es_par"):
            self.skipTest("La función es_par no existe")

        self.assertIsNotNone(ejercicio3.es_par(2), "La función es_par no debe retornar None")
        self.assertTrue(ejercicio3.es_par(2), "La función es_par no retorna True para un número par")
        self.assertFalse(ejercicio3.es_par(3), "La función es_par no retorna False para un número impar")