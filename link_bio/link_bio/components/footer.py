import reflex as rx
import datetime
from link_bio.styles.styles import Size
import link_bio.constants as constants
from link_bio.styles.colors import TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Creado con 💻 y ☕ por Brian Reupach.",
            font_size=Size.MEDIUM.value,
            margin_bottom=Size.BIG.value,
        ),
        padding_bottom=Size.X_SMALL.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value,
        spacing="0",
        align="center",
        position="absolute",
        bottom="0px",
        width="100%"
    )
