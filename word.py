import qrcode

img = qrcode.make ("Hello world") 

img.save("mycode.png")
