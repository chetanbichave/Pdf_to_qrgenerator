import qrcode
from PIL import Image

data = "https://bit.ly/3T3a1gD"

Logo1 = "Logo1.png"
Logo2 = "Logo2.png"
Logo3 = "Logo3.png"
Logo4 = "Logo4.png"

logo = Image.open(Logo1)
basewidth = 90

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

QRcode.add_data(data)


QRcode.make(fit=True)

img = QRcode.make_image(
    fill_color="Blue", back_color="white").convert('RGB')

# set size of QR code
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)

# save the QR code generated
img.save('MyResume.png')

print('QR code generated!')

