import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size
import link_bio.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title("Titulo 1"),
        link_button(
            "click1 prue",
            "body del boton",
            "icons/twitch.svg",
            constants.GOOGLE_URL),
        link_button(
            "click2 prueba",
            "body del boton body del boton body del boton body del boton body del boton ",
            "icons/twitch.svg",
            constants.GOOGLE_URL),
        link_button(
            "click3 tenxto mas largo",
            "body del boton",
            "icons/twitch.svg",
            constants.GOOGLE_URL),
        link_button(
            "click4",
            "body del boton",
            "icons/twitch.svg",
            constants.GOOGLE_URL),
        width="100%",
        spacing="2"
    )
