import reflex as rx

from Reflex.components.navbar import navbar
from Reflex.views.header.header import header
from Reflex.views.links.links import links

from Reflex.views.charts.line_chart import line_chart

# Inicializamos una clase donde se almacenara el estado de la aplicación
class State(rx.State):
    pass

# Creamos el bloque donde se almacenarn nuestros componentes
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        line_chart()
    )

# Inicializamos nuestra aplicación
app = rx.App()

# Agregamos una página a nuestra aplicación
app.add_page(index)

# Compilamos nuestra aplicación
app.compile()