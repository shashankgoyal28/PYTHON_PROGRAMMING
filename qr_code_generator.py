import qrcode
import image
qr = qrcode.QRcode(
    version=15,
    box_size=10,
    border=5
)
deta = "https://www.linkedin.com/in/shashankgoyal28/"
qr.add_data(data)
qr.make(fit=true)
img = qr_make_image(fill="black", back_color="white")
img.save("test.png")
