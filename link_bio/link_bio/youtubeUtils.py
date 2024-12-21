from yt_dlp import YoutubeDL


def getTitleAndDescription(url):
    try:
        # Configuración de yt-dlp
        ydl_opts = {
            'quiet': True,
            'skip_download': True,  # No descargar el video
        }
        with YoutubeDL(ydl_opts) as ydl:
            # Extraer información del video
            info = ydl.extract_info(url, download=False)
            titulo = info.get('title', 'Título no disponible')
            descripcion = info.get('description', 'Descripción no disponible')
            return titulo, descripcion
    except Exception as e:
        return None, f"Error: {e}"
