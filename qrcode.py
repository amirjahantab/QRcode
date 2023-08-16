import os
import qrcode

link = str(input("enter your linck: "))

img = qrcode.make(link)

img.save("myQRCODE.png", "PNG")

os.system("open myQRCODE.png")
