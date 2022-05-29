from asyncio import streams
import imp
from multiprocessing import context
from turtle import title

import os
from django.core.files import File
# Create your views here.
from django.shortcuts import render
#from numpy import tile
import qrcode
import qrcode.image.svg

from io import BytesIO

from Qrcode.models import GenarateCode, QRcodesForDishes
from .forms import QrCodeForm1


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
    new_data = QRcodesForDishes(title=title, img=context)
    new_data.save()


'''
    data = {'title': title,
            'outlet': outlet,
            'img': context,

            }

    form = QrCodeForm1(data)
    if form.is_valid:
        form_data = form.save(commit=False)
        form_data.save()
    print(form)
'''
# print(img)


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
    print(img)
    data = QRcodesForDishes(title=title, img=img)
    # data.save()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("Qrcode/qrcodes/" + title + ".jpg")

    with open(img, 'rb') as qr_img:
        print(qr_img)
        #new_qr_code, created = QRcodesForDishes.objects.get_or_create(title=title, outlet=outlet, is_active=True, defaults={"user":get_user_profile, "qr_code":hex_code, "qr_code_img":File(qr_img), "upcoming_show":get_upcoming_show})
        # if not created:
        #     pass


def code2(request, url, title, outlet):

    method = "basic"

    data = url

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
    stream = BytesIO()
    img.save(stream)
    image = stream.getvalue().decode()

    data = QRcodesForDishes(title=title, outlet=outlet, img=image)
    data.save()
    # Save svg file somewhere
   #
