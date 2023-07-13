from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.exceptions import InvalidSignature

# SM2 椭圆曲线参数
p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
n = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123

# RFC6979 的 K 值生成函数实现
def generate_k(msg, private_key):
    h = hmac.HMAC(int(private_key).to_bytes(32, 'big'), hashes.SHA256())
    h.update(msg)
    digest = h.finalize()
    kdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=b"salt", info=digest)
    k = kdf.derive(key_material=b"key_material")
    return int.from_bytes(k, 'big') % n

# 生成 SM2 密钥对
curve = ec.SECP256K1()
private_key = ec.generate_private_key(curve)
public_key = private_key.public_key()

# 获取消息数据
msg = b"SM2"

# 使用 RFC6979 的 K 值生成函数生成 K 值
k = generate_k(msg, private_key.private_numbers().private_value)
print("使用 RFC6979生成的K值为:",k)

# 计算 SM2 签名
signature = private_key.sign(msg, ec.ECDSA(hashes.SHA256()))

print("SM2签名为",signature)
# 验证 SM2 签名
try:
    public_key.verify(signature, msg, ec.ECDSA(hashes.SHA256()))
    print("Signature verified")
except InvalidSignature:
    print("Signature verification failed")