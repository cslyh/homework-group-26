import hashlib
import struct

# 原始消息和原始摘要值
original_msg = b'Original message'
original_digest = hashlib.new('sm3', original_msg).digest()

# 构造填充消息
message_len = len(original_msg)
padding = b'\x80' + b'\x00' * ((64 - (message_len + 1 + 8) % 64) % 64)  # 利用填充规则进行长度扩展攻击
fake_length = (message_len + len(padding) + 8) * 8
fake_mag = original_msg + padding + struct.pack('>Q', fake_length)

# 计算伪造的摘要
forged_digest = hashlib.new('sm3', fake_mag).digest()

print("original_msg:",original_msg)
print("Original Digest:", original_digest.hex())
print("fake_mag:",fake_mag)
print("Forged Digest:", forged_digest.hex())