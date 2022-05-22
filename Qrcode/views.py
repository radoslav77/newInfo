import imp
from turtle import title
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import qrcode
import qrcode.image.svg

from io import BytesIO

from Qrcode.models import GenarateCode
from .forms import QrCodeForm


def code1(request, url):
    print(123, url)
    form1 = QrCodeForm()
    context = {}
    if request.method == "POST":
        #url = request.POST['name']
        # print(url)
        #factory = SvgImage
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(request.POST.get("qr_text", ""),
                          image_factory=factory, box_size=20)  # qrcode.image.pil.PilImage files for createing qrcode
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    # print(form1)
    return render(request, "Qrcode/code.html", {
        'context': context,
        'form': form1

    })


def code(request, url, title, outlet):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    stream = BytesIO()

    img.save(stream)
    out = []
    for i in outlet:

        data = GenarateCode(title=title, outlet=i, img=img)
        data.save()
        print(data)
    '''return render(request, "Qrcode/code.html", {
        'img': img
    })'''
