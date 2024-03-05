from portafolio.components.heading import heading
import reflex as rx


def about() -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text("Descripción")
    )