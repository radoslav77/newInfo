from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import qrcode
from qrcode.image.svg import SvgImage

from io import BytesIO


def index(request, url):
    context = {}
    if request.method == "POST":
        factory = SvgImage
        img = qrcode.make(request.POST.get("qr_text", ""),
                          image_factory=factory, box_size=20)  # qrcode.image.pil.PilImage files for createing qrcode
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "index.html", context=context)
