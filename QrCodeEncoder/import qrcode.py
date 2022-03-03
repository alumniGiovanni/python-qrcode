import qrcode

img = qrcode.make("www.github.com/alumniGiovanni")
img.save("gitQR.png")