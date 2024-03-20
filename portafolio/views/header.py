import reflex as rx
from portafolio.data import Data
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.styles.styles import Size

def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src = data.avatar,
            size=Size.BIG.value
        ),
        rx.vstack(
            heading(data.name, h1 = True),
            heading(data.title),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"                 
            ),
            media(),
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value,  
    )