import reflex as rx
from portafolio.views.header import header
from portafolio.styles.styles import MAX_WIDTH

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            max_width=MAX_WIDTH
        )
    )


app = rx.App()
app.add_page(index)
