from portafolio.components.heading import heading
import reflex as rx


def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text(description)
    )