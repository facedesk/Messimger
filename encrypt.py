from PIL import Image
import numpy 

def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""

    image = Image.open(image_path, 'r')
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == 'RGB':
        channels = 3
    elif image.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    #pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values


images = get_image("green.jpg")
for image in images:
	print image