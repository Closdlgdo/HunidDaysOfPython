import sys  # To access the command line arguments.

from PIL import Image  # Pillow library to treat the files as images

images = []  # we want to accumulate the images in a list.

for arg in sys.argv[1:]:  # we want to iterate over the command line arguments.
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "2sec.gif", format="GIF", save_all=True, append_images=images[1:], duration=200, loop=0)
# We want to save the first image, but we are asking the library to append the other image as well.
