from PIL import Image

from glitch_this import ImageGlitcher

"""
    - Ejemplo de como crear un gif a partir de una imagen
"""

glitcher = ImageGlitcher()


img = Image.open("input/kanagawa.png")

print(img)


glitch_img = glitcher.glitch_image(
    img,
    glitch_amount=8.0,
    color_offset=True,
    gif=True                # Hace que el resultado sea un gif, lo que hace este parámetro en realidad es indicar a la
                            # función que debe glitchear la imagen original varias veces en lugar de solo una,
                            # devolviendo un array de imágenes glitcheadas en lugar de solo una.
)


# Este código de guardado es ligeramente diferente al de los scripts anteriores, ya que recibe como entrada la primera
# imagen del array creado con la función anterior (glitch_img[0]) y la guarda contatenándole el resto de imágenes
# del array después (parámetro: append_images=glitch_img[1:])
# Puede tardar varios segundos en finalizar
DURATION = 200      # Duracion en centésimas de segundo
LOOP = 0            # 0 para bucle infinito
glitch_img[0].save('output/kanagawa_gif.gif',
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=DURATION,
                   loop=LOOP)
