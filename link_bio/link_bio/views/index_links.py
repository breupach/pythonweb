import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as constants
from link_bio.routes import Route


def index_links() -> rx.Component:
    return rx.vstack(
        title("Proyectos de cursos"),
        link_button(
            constants.COURSES_TITLE_COURSES_BUTTON,
            constants.COURSES_DESCRIPTION_COURSES_BUTTON,
            "/icons/python.svg",
            Route.COURSES.value,
            is_external=False
        ),
        link_button(
            constants.COURSES_TITLE_PYTHON_WEB,
            constants.COURSES_DESCRIPTION_PYTHON_WEB,
            "/icons/python.svg",
            constants.GITHUB_PYTHON_WEB_URL
        ),
        width="100%",
        spacing="2"
    )
