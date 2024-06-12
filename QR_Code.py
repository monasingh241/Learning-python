# import qrcode as qr
# img=qr.make("ullu banaya bada maza aaya")
# # img=qr.make("https://www.youtube.com/watch?v=k3g_WjLCsXM")
# img.save("Sajni_re_song.png")

import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.instagram.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="blue")
img.save("insta_gr.png")