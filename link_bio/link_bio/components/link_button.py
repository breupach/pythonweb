import reflex as rx
from link_bio.styles.styles import Size, button_body_style, button_title_style


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.center(
                    rx.image(
                        src=image,
                        width=Size.LARGE.value,
                        height=Size.LARGE.value,
                        margin=Size.MEDIUM.value,
                    ),
                    rx.vstack(
                        rx.text(title, style=button_title_style),
                        rx.text(body, style=button_body_style),
                        align_items="start",
                        margin=Size.ZERO.value,
                        spacing="0"
                    )
                ),
                width="100%",
            ),
            cursor="pointer",
        ),
        href=url,
        is_external=True,
        width="100%",
    )
