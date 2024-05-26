from PIL import Image

from glitch_this import ImageGlitcher

"""
- Ejemplo más avanzado utilizando diferentes parámetros

"""

glitcher = ImageGlitcher()


img = Image.open("input/kanagawa.png")

print(img)

# Esta es la única línea de código que cambia, el resto son idénticas al script 1
# Puedes usar parámetros más avanzados para aplicar distintos ejemplos sobre la imagen
# Lista completa de parámetros: https://github.com/TotallyNotChase/glitch-this/wiki/Documentation:-The-glitch-this-library
# Puedes comentar/descomentar cada línea para ver los efectos de cada parámetro de manera individual
glitch_img = glitcher.glitch_image(
    img,                     # Imagen a modificar (inicializada antes)
    glitch_amount=8.0,         # Nivel de glitching entre 0.0 y 10.0 a aplicar (el creador de la librería dice que su favorito es el 2)
    color_offset=True,       # Modifica aleatoriamente el valor del RGB
    scan_lines=True,         # Líneas de televisión antigua
)


glitch_img.save("output/kanagawa_complex_glitch.png")
