# 🧪 Tech Lab

Laboratorio donde pruebo tecnologías y librerías, con ejemplos que corren y referencias rápidas de cómo usarlas: lo que la documentación oficial a veces no deja claro.

Consolida varios repositorios de pruebas que tenía por separado. Cada uno conserva su historial de commits.

## Tecnologías

| Carpeta | Qué hay |
|---|---|
| [🎈 streamlit](./streamlit/) | 9 mini proyectos (hello world, Yahoo Finance, ML con Iris y pingüinos, multipágina, autenticación con y sin base de datos, interactividad y modularización) y una [plantilla](./streamlit/plantilla/) multipágina con login |
| [📊 dash](./dash/) | Hello Dash, apps multipágina y Dash con Bootstrap |
| [🌀 reflex](./reflex/) | App básica con navbar, header y gráfico de líneas |
| [🤖 pycaret](./pycaret/) | Primer contacto con AutoML |
| [🔗 ploomber](./ploomber/) | Pipeline de ejemplo (get, clean, plot) |
| [🧰 python-utils](./python-utils/) | Utilidades: envío de correos, formato de Excel, generación de PowerPoint, lectura de archivos, módulos de gráficos y EDA, y una guía para empaquetar módulos |

## Cómo agregar una tecnología

Cada carpeta debería tener:

- `README.md` con la referencia rápida: qué es, instalación, conceptos clave, snippets, errores comunes y enlaces
- Ejemplos mínimos que corran
- Su propio `requirements.txt` o `pyproject.toml`

## Notas

- Los `config.yaml` de autenticación de Streamlit son el ejemplo de la documentación de `streamlit-authenticator` (usuarios ficticios).
- Ploomber está prácticamente abandonado; queda como referencia histórica.
