import reflex as rx
from portafolio import data
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.about import about
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack
from portafolio.views.extra import extra

DATA = data.data 
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            #rx.theme_panel(),
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formación", DATA.training),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing = Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme = rx.theme(
        appearance="dark",
        accentColor="cyan",
        radius="full"
    )
    
)
app.add_page(index)
