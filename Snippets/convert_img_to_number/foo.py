from PIL import Image
from io import BytesIO
import base64
from zlib import adler32

def convert_image(image):
    img = Image.open(image)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    image_string = adler32(img_str)
    img.close()
    return image_string

if __name__ == "__main__":
    print(convert_image("img.png"))

    #3765326702