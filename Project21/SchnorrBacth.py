import os
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend

def schnorr_batch_sign(private_keys, messages):
    curve = ec.SECP256K1()  # 使用secp256k1曲线
    backend = default_backend()
    sign_keys = [ec.derive_private_key(int.from_bytes(private_key, byteorder='big'), curve, backend) for private_key in private_keys]
    public_keys = [key.public_key() for key in sign_keys]
    aggregated_challenge = b""
    for i in range(len(messages)):
        hash_message = hashlib.sha256(messages[i].encode()).digest()
        aggregated_challenge += hash_message
    hashed_challenge = hashlib.sha256(aggregated_challenge).digest()
    # 进行批量签名
    signatures = []
    for i in range(len(private_keys)):
        signature_der = sign_keys[i].sign(data=hashed_challenge, signature_algorithm=ec.ECDSA(SHA256()))
        signatures.append(signature_der)

    return public_keys, signatures


private_key1 = os.urandom(32)
private_key2 = os.urandom(32)
message1 = "Project21"
message2 = "Schnorr Bacth"
private_keys = [private_key1, private_key2]
messages = [message1, message2]
print("message:",messages)
public_keys, signatures = schnorr_batch_sign(private_keys, messages)

for public_key in public_keys:
    serialized_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


print("\nSignatures:")
for signature in signatures:
    print(signature.hex())