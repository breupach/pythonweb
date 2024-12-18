import reflex as rx
from link_bio.styles.styles import Size
from link_bio.components.info_text import info_text
from link_bio.components.link_icon import link_icon
import link_bio.constants as constants
from link_bio.styles.colors import TextColor, Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="favicon.ico",
                fallback="BR",
                size="5",
                radius="full",
                variant="solid",
                border="4px solid",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading(
                    "Brian Reupach",
                    size="7"
                ),
                rx.text(
                    "@breupach",
                    size="2",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/twitch.svg",
                        constants.GOOGLE_URL
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        constants.GOOGLE_URL
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        constants.GOOGLE_URL
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        constants.GOOGLE_URL
                    ),
                    margin_top=Size.X_SMALL.value,
                    spacing="4"
                ),
                spacing="0"
            ),
        ),
        rx.flex(
            info_text("+5", "años de experiencia"),
            rx.spacer(),
            info_text("+5", "años de experiencia"),
            rx.spacer(),
            info_text("+5", "años de experiencia"),
            width="100%"
        ),
        rx.text(
            "Poner algo relacionado a experiencia de trabajo y que va a ser un portafolio para subir las aplicaciones que se realicen.",
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value,
        ),
        spacing="6"
    )
