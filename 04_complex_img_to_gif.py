from PIL import Image

from glitch_this import ImageGlitcher

"""
    - Ejemplo AVANZADO de como crear un gif a partir de una imagen
    - En este ejemplo se convierte una imagen a gif, pero cada frame del gif resultante tiene un nivel de glitch superior
        al anterior (i.e., la imagen se va deformando poco a poco).
"""

glitcher = ImageGlitcher()


img = Image.open("input/kanagawa.png")

print(img)


glitch_img = glitcher.glitch_image(
    img,
    glitch_amount=1.0,        # Nivel de glitch inicial, lo he bajado al mínimo para que se note el cambio
    color_offset=True,
    gif=True,
    glitch_change=0.1,       # Indica cuanto incrementa el nivel de glitching con cada frame, si vale 0.1 el segundo frame tendrá un glitch de 1.1, el tercero 1.2, etc.
                            #       También puede utilizarse un número negativo para que el valor se vaya decrementando.
    cycle=True,             # Si vale True, cuando el nivel de glitching aumente (gracias al parámetro glitch_change)
                            # hasta 10, se reiniciará a 0 para seguir aumentando.
    # frames=23,              # Número de frames por segundo (el valor por defecto es 23).
    step=2                     # Cada cuantos frames se incrementa el valor del glitching, el valor por defecto es 1.
)


DURATION = 2000          # He aumentado la duración para que se note mejor el incremento
LOOP = 0
glitch_img[0].save('output/kanagawa_complex_gif.gif',
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=DURATION,
                   loop=LOOP)
