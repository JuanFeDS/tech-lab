1. Crear un entorno virtual y activarlo
2. pip install wheel
3. Crear el archivo setup.py
4. Crear la carpeta que contendra nuestro modulo
    - Agregar el archivo __init__.py
    - Agregar los scripts que tengan nuestras funciones/clases
5. Compilar 
    -python setup.py sdist
    -python setup.py bdist_wheel
6. Enviar a github los archivos correspondientes
    - modulo
    - gitignore/readme/setup.py
    - *.egg-info
    - build/lib

