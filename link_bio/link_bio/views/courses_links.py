import reflex as rx
from link_bio.components.link_youtube_button import link_youtube_button
from link_bio.components.title import title
import link_bio.constants as constants
from link_bio.routes import Route


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos realizados"),
        link_youtube_button(
            constants.COURSES_TITLE_PYTHON_WEB,
            constants.COURSES_DESCRIPTION_PYTHON_WEB,
            "/icons/youtube.svg",
            constants.COURSES_MOUREDEV_PYTHON_WEB_URL
        ),
        width="100%",
        spacing="2"
    )
