import reflex as rx
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.about import about
from portafolio.styles.styles import MAX_WIDTH, EmSize, Size

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            footer(),
            spacing = Size.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH
        )
    )


app = rx.App()
app.add_page(index)
