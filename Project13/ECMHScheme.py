import hashlib
import random
from sympy import gcd, mod_inverse

# 椭圆曲线参数
a = -1
b = 1
p = 263
G = (2, 51)  # 基点


def hash_to_point(message):
    # 哈希消息
    hash_value = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    x = hash_value % p
    y_squared = (x ** 3 + a * x + b) % p
    y = pow(y_squared, (p + 1) // 4, p)
    if y % 2 != 0:
        return (x, y)
    else:
        return (x, p - y)


def add_points(point1, point2):
    if point1 == point2:
        return double_point(point1)

    if point1[0] == point2[0]:
        slope = (3 * pow(point1[0], 2) + a) * mod_inverse(2 * point1[1], p)
    else:
        slope = (point2[1] - point1[1]) * mod_inverse(point2[0] - point1[0], p)

    x = (pow(slope, 2) - point1[0] - point2[0]) % p
    y = (slope * (point1[0] - x) - point1[1]) % p

    return (x, y)


def double_point(point):
    slope = (3 * pow(point[0], 2) + a) * mod_inverse(2 * point[1], p)

    x = (pow(slope, 2) - 2 * point[0]) % p
    y = (slope * (point[0] - x) - point[1]) % p

    return (x, y)


# 测试
message = "Implement the above ECMH scheme"
print("message:",message)
hashed_point = hash_to_point(message)
print("Hashed Point:", hashed_point)


Q = hashed_point
for i in range(10):
    private_key = random.randint(1, p - 1)
    public_key = double_point(G)  # G为基点
    shared_key = double_point(Q)
    Q = add_points(public_key, shared_key)

print("added Point:", Q)