import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as constants
from link_bio.pages.index import index
from link_bio.pages.courses import courses


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)
