from PIL import Image

from glitch_this import ImageGlitcher

"""
- Para instalar la librería tienes que ejecutar el siguiente comando:
    pip install glitch-this

- Repositorio oficial: https://github.com/TotallyNotChase/glitch-this?tab=readme-ov-file

- Documentación: https://github.com/TotallyNotChase/glitch-this/wiki/Documentation:-The-glitch-this-library

- Videotutorial muy simple: https://www.youtube.com/watch?v=knW6Zhhmpqg&ab_channel=LeslieWubbel

"""

# Instancia la clase de la librería que hace el proceso de glitching
glitcher = ImageGlitcher()


# Carga la imagen original en memoria utilizando la ruta completa o relativa (carpeta "input")
img = Image.open("input/kanagawa.png")

# Imprimir algunos detalles de la imagen
print(img)

# Creamos la imagen glitcheada (variable glitch_img) aplicando la función glitch_image llamando al objeto glitcher
# que hemos instanciado antes
# IMPORTANTE: Es aleatorio, cada ejecución con los mismos parámetros genera resultados diferentes, guarda un
#               resultado con otro nombre si te gusta
glitch_img = glitcher.glitch_image(
    img,                # Imagen a modificar (inicializada antes)
    glitch_amount=8.0       # Nivel de glitching entre 1.0 y 10.0 a aplicar (el creador de la librería dice que su favorito es el 2)
)

# Guardamos la imagen resultante en la carpeta output
glitch_img.save("output/kanagawa_basic_glitch.png")
