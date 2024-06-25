# PYTHON ASSESSMENT CLARCAT


## Python Assessment Project
Este proyecto contiene varias funciones y clases en Python para resolver problemas técnicos. Incluye pruebas unitarias para verificar la funcionalidad.
Se ha agregado recientemente un script en python para hacer peticiones a una url.

## Requisitos Previos

- Python 3.6 o superior recomendado 3.12.0
- pip (gestor de paquetes de Python)

## Instalación

   ```sh
   git clone https://github.com/JoseBlancoSiles/python_assessment_clarcat.git
   cd python_assessment_clarcat

    python -m venv venv # Recomendable crear entorno virtual por tema dependencias
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

    pip install -r requirements.txt

    pytest # Para lanzar los tests, recomendable desde el directorio principal
   ```

   Para probar el [Script de peticiones del ejercicio 11](./request.py) lanzar desde el directorio principal del proyecto:
   ```sh
    python request.py
   ```