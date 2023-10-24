import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://instagram.com/matitanam___?igshid=YTQwZjQ0NmI0OA==" #link qrcode

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white") #setting warna
img.save("link.png")