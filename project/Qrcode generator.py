#import pyqrcode from pyqrcode import Qrcode.
import pyqrcode
from pyqrcode import QRCode
#string which represents the Qr code
link= 'https://www.youtube.com/@sc0utOP'
#generate Qrcode
url = pyqrcode.create(link)
# create and save the Qr file '
url.svg('scoutQR.svg',scale=8)

