# ejercicios_python

Ejercicios de programación en Python.

## Estructura del proyecto

La organización del repositorio es la siguiente:

```bash
main.py # Archivo principal
README.md
requirements.txt # Listado de dependencias del proyecto
ejercicios/ # Carpeta de ejercicios
    __init__.py
    ...
utils/ #modulo de utilidades para el proyecto
    __init__.py
    checker.py # script para validar ejercicios
```
> **Nota**: en las subcarpetas dentro `ejercicios` cada carpeta tiene dos archivos: `solucion.py` y `test.py`. En `solucion.py` debes resolver el ejercicio para que se pueda hacer el test correctamente.

> Cuando se ejecuta un test, en la termina muestra el error y la razón por la cual el ejercicio no paso el test

## Requisitos

- Python 3.10 o superior
- pip

Es recomendable usar un entorno virtual para no alterar las dependencias del sistema.

## Crear y activar un entorno virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Windows (CMD):

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Instalar dependencias

Con el entorno activo, instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecutar los tests

Hay dos formas principales de validar los ejercicios:

- Usar el checker interactivo (recomendado):

	```bash
	python main.py
	```

	El script pedirá el número del ejercicio y ejecutará su `test.py` mostrando el resultado.

- Usar `unittest` directamente:

	- Ejecutar todos los tests:

		```bash
		python -m unittest discover -s ejercicios -p "test.py"
		```

	- Ejecutar el test de un ejercicio específico (ejemplo para `ejercicio2`):

		Opción A (más simple): cambiar al directorio `ejercicios` y ejecutar el test como módulo:

		```bash
		cd ejercicios
		python -m unittest ejercicio2.test
		```

		Opción B: exportar `PYTHONPATH` apuntando a la carpeta `ejercicios` y ejecutar el módulo desde la raíz:

		macOS / Linux:
		```bash
		PYTHONPATH=ejercicios python -m unittest ejercicio2.test
		```

		Windows (PowerShell):
		```powershell
		$env:PYTHONPATH = "ejercicios"
		python -m unittest ejercicio2.test
		```

		Windows (CMD):
		```cmd
		set PYTHONPATH=ejercicios
		python -m unittest ejercicio2.test
		```

## Notas

- El archivo `utils/checker.py` contiene la lógica usada por `main.py` para cargar y ejecutar el test de un ejercicio seleccionado.
- Los tests están escritos con `unittest` y usan import dinámico esperando que la carpeta `ejercicios` esté en `PYTHONPATH` (por eso las instrucciones previas funcionan).
- Si necesita ejecutar un test de forma automatizada desde otro entorno CI, asegúrese de activar el entorno virtual y de que `ejercicios` esté en `PYTHONPATH` o use `unittest discover` con `-s ejercicios`.
