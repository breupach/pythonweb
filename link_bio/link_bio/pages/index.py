import reflex as rx
import link_bio.utils as utils
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.styles.styles import Size
import link_bio.styles.styles as styles


@rx.page(
    title=utils.INDEX_PAGE_TITLE,
    description=utils.INDEX_PAGE_DESCRIPTION,
    image=utils.PREVIEW,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding_x=Size.MEDIUM.value,
            )
        ),
        footer(),
    )
