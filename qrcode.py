import os
import qrcode

link = str(input("enter your link: "))

img = qrcode.make(link)

img.save("myQRCODE.png", "PNG")

os.system("open myQRCODE.png")
