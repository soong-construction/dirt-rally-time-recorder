import pyqrcode
import keygen_demo

# Cf. https://www.qrcode.com/en/about/version.html
# Since terminal background is usually black/dark, data_module corresponds to spaces and the qrcode background is drawn
DATA_MODULE = '  '
BACKGROUND = u"\u2588"u"\u2588"

# TODO #6 Use base64 encoded public key? (33% overhead vs. 50% more efficient alphanumeric encoding)
def qr_ascii_code(data):
    qrcode = pyqrcode.create(data, 'L', 6, 'binary').text(quiet_zone=1)
    # TODO #6 Recreate prefix on client?
    fix_prefix = 'ssh-rsa AAAAB3NzaC1yc2E'
    
    qrcode_str = str(qrcode)
    qrcode_str = qrcode_str.replace(fix_prefix, '')
    return qrcode_str.replace('1', DATA_MODULE).replace('0', BACKGROUND)

qrcode = qr_ascii_code(keygen_demo.public_key)
print(str(qrcode))