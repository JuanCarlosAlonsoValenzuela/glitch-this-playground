from PIL import Image

from glitch_this import ImageGlitcher

"""
    - Ejemplo de como aplicar glitching a un gif, es bastante parecido a las imágenes
"""

glitcher = ImageGlitcher()


img = Image.open("input/example_gif.gif")

print(img)

# Mismos parámetros que con las imágenes (Script 02)
# También puede usarse glitching incremental como en el script 4
# En lugar de un objeto devuelve 3:
# glitch_img: Array de imágenes que componen el gif glitcheado
# src_gif_duration: Duración en centésimas de segundos del gif resultante
# src_gif_frames: Número de frames del gif original
glitch_img, src_gif_duration, src_gif_frames = glitcher.glitch_gif(
    img,
    glitch_amount=8.0,
    color_offset=True,
    scan_lines=True
)


# Se guarda exactamente igual que los gifs de los scripts 03 y 04
DURATION = 200
LOOP = 0
glitch_img[0].save('output/gif_to_glitched_gif.gif',
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=DURATION,
                   loop=LOOP)
