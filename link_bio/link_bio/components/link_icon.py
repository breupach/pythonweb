import reflex as rx
from link_bio.styles.styles import Size


def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value
        ),
        href=url,
        is_external=True
    )
