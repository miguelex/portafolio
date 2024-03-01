import reflex as rx
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.styles.styles import MAX_WIDTH, EmSize

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.divider(),
            header(),
            footer(),
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH
        )
    )


app = rx.App()
app.add_page(index)
