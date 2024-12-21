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
                src="/avatar.png",
                fallback="BR",
                size="7",
                radius="full",
                variant="solid",
                border="2px solid",
                border_color=Color.PRIMARY.value,
                _hover={"transform": "scale(1.5)"}
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
                        "/icons/github.svg",
                        constants.GITHUB_URL
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        constants.INSTAGRAM_URL
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        constants.LINKEDIN_URL
                    ),
                    margin_top=Size.X_SMALL.value,
                    spacing="4"
                ),
                spacing="0"
            ),
        ),
        rx.text(
            constants.PROFILE_DESCRIPTION,
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value,
        ),
        spacing="6"
    )
