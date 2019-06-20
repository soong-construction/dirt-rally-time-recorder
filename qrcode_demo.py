import pyqrcode
import keygen_demo

# Cf. https://www.qrcode.com/en/about/version.html
# Since terminal background is usually black/dark, data_module corresponds to spaces and the qrcode background is drawn
DATA_MODULE = '  '
BACKGROUND = u"\u2588"u"\u2588"

def qr_ascii_code(data):
    qrcode = pyqrcode.create(data, 'L', 6, 'alphanumeric').text(quiet_zone=1)
    
    qrcode_str = str(qrcode)
    return qrcode_str.replace('1', DATA_MODULE).replace('0', BACKGROUND)

uri = 'DRTR://USER1234567890/V1/' + keygen_demo.pub_key_b32_url

print('uri ' + uri)

qrcode = qr_ascii_code(uri)

print(str(qrcode))

# Encode URI as such: <scheme>://<userid>/<version>/<pub_key_b32_url>, e.g. DRTR://USER1234567890/V1/ONQQAAAAAMAQAAIAAAAECAEXJF5HMFCN6RX7IESTBJG4R3OTX6B2YP6HCDEDMXDVMDETHCKMFCO2URWS546TRSYHL6RIQ3XVTDH2GCOTVIFN7JWCDB6TTQUXERJX2%3D%3D%3D
# max length: <scheme>:// = 7, <userid>/ = 19, <version>/ = 4, <pub_key_b32_url> = 153: 183
# allows QRCode in version 6
# TODO #6 Truncate userid by selecting 18-suffix 
