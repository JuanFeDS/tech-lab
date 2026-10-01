import reflex as rx

def navbar() -> rx.Component:
    return(
        rx.hstack(
        rx.text(
            'JuanFe98',
            height='40px',
            width='100%',
            background='darkblue',
            color='white'
        ),
        position='sticky',
        width='100%',
        background='black',
        padding_x='16px',
        padding_y='8px',
        z_index='999',
    )
) 