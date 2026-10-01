import reflex as rx

import plotly.express as px

df = px.data.gapminder().query('country == "Colombia"')

fig = px.line(
    df,
    x='year',
    y='lifeExp',
    title='Life expectaty in Colombia'
)

def line_chart() -> rx.Component:
    return(
        rx.plotly(data=fig)
    )