import reflex as rx
from link_bio.styles.styles import Size, navbar_title_style
from link_bio.styles.colors import TextColor, Color
from link_bio.routes import Route


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.link(
                rx.text(
                    "Breu",
                    as_="span",
                    color=Color.PRIMARY.value,
                ),
                rx.text(
                    "pach",
                    as_="span",
                    color=Color.SECONDARY.value
                ),
                style=navbar_title_style,
                href=Route.INDEX.value
            )
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
