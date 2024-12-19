import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links
from link_bio.styles.styles import Size
import link_bio.styles.styles as styles
import link_bio.constants as constants


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding_x=Size.MEDIUM.value,
            )
        ),
        footer(),
    )


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)
app.add_page(
    index,
    title=constants.PAGE_TITLE,
    description=constants.PAGE_DESCRIPTION,
    image="favicon.ico"
)
