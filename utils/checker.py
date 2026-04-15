"""
## Checker
Modulo para ejecutar test de un ejercicio.

Este modulo tiene un pequeño script para consultar el numero ejercicio y realizar
el test usando unittest.
"""
from types import ModuleType
import sys
import os
import importlib.util
import unittest
import colorama

# funcion lambda para colores
print_red = lambda text: print(f"{colorama.Fore.RED}{text}{colorama.Style.RESET_ALL}")
print_yellow = lambda text: print(
    f"{colorama.Fore.YELLOW}{text}{colorama.Style.RESET_ALL}"
)
print_green = lambda text: print(
    f"{colorama.Fore.GREEN}{text}{colorama.Style.RESET_ALL}"
)


def ask_number(prompt="Ingresa el número de ejercicio: ") -> int:
    """Pedir número

    Args:
        prompt (str, optional): mensaje para el usuario. Defaults to "Ingresa el número de ejercicio: ".

    Returns:
        int: número ingresado
    """
    while True:
        s = input(prompt).strip()

        if not s:
            print_red("NO se ha ingresado nada, intenta de nuevo.")
            continue
        if not s.isdigit():
            print_red("No se ha ingresado un número, intenta de nuevo.")
            continue

        # Validar que el número sea positivo
        n = int(s)
        if n <= 0:
            print_red("El número debe ser positivo, intenta de nuevo.")
            continue

        return n


def load_test_file(n: int) -> ModuleType | None:
    """Cargar archivo de test

    Args:
        n (int): numero de ejercicio

    Returns:
        ModuleType | None: archivo de test o None si el archivo no existe
    """
    repo_root = os.path.dirname(os.path.dirname(__file__))
    base = os.path.join(repo_root, "ejercicios", f"ejercicio{n}")
    test_path = os.path.join(base, "test.py")

    ejercicios_dir = os.path.join(repo_root, "ejercicios")

    if ejercicios_dir not in sys.path:
        sys.path.insert(0, ejercicios_dir)

    if not os.path.isdir(base) or not os.path.exists(test_path):
        print_red("Error: Archivo de test no encontrado para el ejercicio seleccionado")
        return None

    spec = importlib.util.spec_from_file_location(f"ejercicio{n}.test", test_path)
    if spec is None:
        print_red("Error: No se pudo cargar el módulo de test")
        return None

    mod = importlib.util.module_from_spec(spec=spec)

    try:
        spec.loader.exec_module(mod)  # type: ignore
    except Exception as e:
        print_red(f"Error al ejecutar el módulo de test: {e}")
        return None

    return mod


def run_test(testModule: ModuleType):
    """Correr test

    Args:
        testModule (ModuleType): modulo del test

    Returns:
        int: resultado de la ejecución del test, 0 si es correcto, 1 si no lo es
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(testModule)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print_green("------------------------------------------------------")

    if result.wasSuccessful():
        print_green("El ejercicio está correcto")
        return 0
    else:
        print_yellow("El ejercicio no está correcto, revisa los errores anteriores")
        return 1


def check_exercise():
    """Función principal para ejecutar el checker."""
    n = ask_number()
    test_file = load_test_file(n)
    print_green("------------------------------------------------------")
    if test_file is not None:
        code = run_test(test_file)
        sys.exit(code)
