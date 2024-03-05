from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.styles.styles import Size
import reflex as rx

def info(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        info_detail(),
        spacing = Size.DEFAULT.value
    )