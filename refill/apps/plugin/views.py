# Create your views here.
from django.http import HttpResponse
import Image, ImageDraw

__root_image = Image.new("RGB", (1,1))
__sample_canvas = ImageDraw.Draw(__root_image)

def text_image(request, display_string):
    global __sample_canvas
    response = HttpResponse(mimetype="image/png")

    x, y = __sample_canvas.textsize(display_string)
    image = Image.new("RGB", (x+10, y))
    canvas = ImageDraw.Draw(image)
    canvas.text((5,0), display_string)

    image.rotate(90).save(response, "PNG")
    return response