import imp
from multiprocessing import context
from turtle import title


# Create your views here.
from django.shortcuts import render
import qrcode
import qrcode.image.svg

from io import BytesIO

from Qrcode.models import GenarateCode, QRcodesForDishes
from .forms import QrCodeForm


def index1(request):

    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text", ""),
                          image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "Qrcode/index1.html", context=context)


def code(request, url, title, outlet):
    #print(url, outlet)
    context = {}
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(request.POST.get(url, ""),
                      image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)
    context["svg"] = stream.getvalue().decode()
    data = QRcodesForDishes(title=title, img=context)
    data.save()
    print(img)


def code1(request, url, title):

   # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # The data that you want to store
    data = url

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()
    #img = "Qrcode/qrcodes/" + title + ".jpg"
    #data = QRcodesForDishes(title=title, img=img)
    # data.save()
    print(img)
    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("Qrcode/qrcodes/" + title + ".jpg")


def code2(request, url, title):
    method = "basic"

    data = "Some text that you want to store in the qrcode"

    if method == 'basic':
        # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
    elif method == 'path':
        # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage

    # Set data to qrcode
    img = qrcode.make(data, image_factory=factory)

    # Save svg file somewhere
    img.save("qrcode.svg")
