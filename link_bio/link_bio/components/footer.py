import reflex as rx
import datetime
from link_bio.styles.styles import Size
import link_bio.constants as constants
from link_bio.styles.colors import TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            height=Size.VERY_BIG.value,
        ),
        rx.link(
            f"texto de link - {datetime.date.today().year}",
            href=constants.GOOGLE_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "texto footer texto footer texto footer texto footer texto footer ",
            font_size=Size.MEDIUM.value,
            margin_bottom=Size.BIG.value,
        ),
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value,
        spacing="0",
        align="center"
    )
