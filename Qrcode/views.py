import imp
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import qrcode
import qrcode.image.svg

from io import BytesIO
from .forms import *


def code(request):
    print(123)
    form1 = GenarateCode()
    context = {}
    if request.method == "POST":
        url = request.POST['name']
        print(url)
        #factory = SvgImage
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(request.POST.get("qr_text", ""),
                          image_factory=factory, box_size=20)  # qrcode.image.pil.PilImage files for createing qrcode
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    print(form1)
    return render(request, "Qrcode/code.html", {'context': context})
