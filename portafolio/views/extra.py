import reflex as rx 
from portafolio.components.heading import heading
from portafolio.styles.styles import Size
from portafolio.components.card_detail import card_detail

def extra() -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail()
                    for _ in range (0, 3)
                ],
                spacing=Size.DEFAULT.value,
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail()
                    for _ in range (0, 3)
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )