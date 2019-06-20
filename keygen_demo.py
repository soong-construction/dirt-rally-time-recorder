from encodings.base64_codec import base64

from cryptography.hazmat.backends import default_backend as crypto_default_backend
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa

UTF_8 = 'utf-8'
key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=512
)
private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption())
public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH,
    crypto_serialization.PublicFormat.OpenSSH
)

# TODO #6 Recreate prefix on client
fix_prefix = 'ssh-rsa AAAAB3NzaC1y'

pub_key_canon = public_key.decode(UTF_8)
pub_key_b64 = pub_key_canon.replace(fix_prefix, '')
print('b64 ' + pub_key_b64)

pub_key_bin = base64.b64decode(bytes(pub_key_b64, UTF_8))
pub_key_b32 = base64.b32encode(pub_key_bin).decode(UTF_8)
print('b32 ' + pub_key_b32)

pub_key_b32_url = pub_key_b32.replace("=", "%3D")
print('b32url ' + pub_key_b32_url);
