import reflex as rx
import link_bio.utils as utils
from link_bio.routes import Route
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.styles.styles import Size
import link_bio.styles.styles as styles


@rx.page(
    route=Route.COURSES.value,
    title=utils.COURSES_PAGE_TITLE,
    description=utils.COURSES_PAGE_DESCRIPTION,
    image=utils.PREVIEW,
)
def courses() -> rx.Component:

    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                courses_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding_x=Size.MEDIUM.value,
            )
        ),
        footer(),
    )
