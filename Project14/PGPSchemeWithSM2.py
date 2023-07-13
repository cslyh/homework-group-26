from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ec
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

# 生成PGP密钥对
def generate_pgp_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=3072
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_key

# 加密
def pgp_encrypt(message, public_key):
    recipient_key = serialization.load_pem_public_key(public_key)

    cipher_text = recipient_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher_text

# 解密
def pgp_decrypt(cipher_text, private_key):
    private_key = serialization.load_pem_private_key(private_key, password=None)

    message = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return message

# 生成SM2密钥对
def generate_sm2_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_key

# 签名
def sm2_sign(message, private_key):
    private_key = serialization.load_pem_private_key(private_key, password=None)

    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

# 验签
def sm2_verify(message, signature, public_key):
    public_key = serialization.load_pem_public_key(public_key)

    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False


message = b"Implement a PGP scheme with SM2"

# 生成PGP密钥对
pgp_private_key, pgp_public_key = generate_pgp_key_pair()

# 加密
ciphertext = pgp_encrypt(message, pgp_public_key)



# 生成SM2密钥对
sm2_private_key, sm2_public_key = generate_sm2_key_pair()

# 签名
signature = sm2_sign(message, sm2_private_key)

# 验签
is_valid = sm2_verify(message, signature, sm2_public_key)

print("message:", message)
print("ciphertext:",ciphertext)
print("signature:",signature)
print("Signature is valid:", is_valid)