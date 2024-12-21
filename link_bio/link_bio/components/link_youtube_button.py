import reflex as rx
from link_bio.styles.styles import Size, button_body_style, button_title_style
from link_bio.components.link_button import link_button
import link_bio.youtubeUtils as youtubeUtils


def link_youtube_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:

    title, description = youtubeUtils.getTitleAndDescription(url)

    if description and len(description) > 100:
        description = description[:100] + "..."

    return link_button(title, description, image, url, is_external)
