import secrets
import string
import hashlib
import time


def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(secrets.choice(letters) for _ in range(length))
    return random_string


def sm3_hash(message):
    # 创建一个SM3哈希对象
    sm3 = hashlib.new('sm3')

    # 更新哈希对象的数据
    sm3.update(message.encode('utf-8'))

    # 计算哈希值
    hash_value = sm3.hexdigest()

    return hash_value
def main(n):
    output = {}
    random_string = generate_random_string(n)
    while True:
        hashValue = sm3_hash(random_string)
        if hashValue[:n] not in output:
            output[hashValue[:n]] = random_string
            random_string = hashValue
        else:
            print(f"find the {n*4} bit collision!")
            print("input1:",output[hashValue[:n]])
            print("input2:",random_string)
            print("collision hashValue:",hashValue[:n])
            break

if __name__=='__main__':
    print("please input the byte length of Rho method of reduced SM3:",end=' ')
    n = int(input())
    start = time.time()
    main(n)
    end = time.time()
    print("time used:",end-start,"s")

