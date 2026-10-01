import reflex as rx

def header() -> rx.Component:
    return (
        rx.vstack(
            rx.avatar(name='JuanFe', size='xl'),
            rx.text('@JuanFe98'),
            rx.text('BIENVENID@S'),
            rx.text('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit neque id enim vehicula iaculis. Integer laoreet a lacus sit amet feugiat. Nunc gravida erat varius erat fringilla elementum. Aliquam ultrices, sem in blandit blandit, purus ex luctus nulla, eget ullamcorper neque quam placerat nisl. Curabitur tempus mattis eros''')
        )
    )