import secrets
import string
import hashlib
import time
import multiprocessing


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
def main(n,shared_dict):
    start = time.time()
    while True:
        random_string = generate_random_string(n)
        hashValue = sm3_hash(random_string)[:n]
        if hashValue not in shared_dict:
            shared_dict[hashValue] = random_string
        else:
            print(f"find the {n*4} bit collision!")
            print("input1:",shared_dict[hashValue])
            print("input2:",random_string)
            print("collision hashValue:",hashValue)
            end = time.time()
            print("time used:", end - start, "s")
            print("-------------------")
            # exit_flag.value = 1
            break
if __name__=='__main__':
    print("please input the byte length of birthday attack of reduced SM3:",end=' ')
    n = int(input())
    # exit_flag = multiprocessing.Value('i', 0)

    manager = multiprocessing.Manager()
    shared_dict = manager.dict()

    # 创建多个进程
    processes = []
    num_processes = multiprocessing.cpu_count()
    for _ in range(num_processes):
        process = multiprocessing.Process(target=main, args=(n,shared_dict))
        process.start()
        processes.append(process)

    # 等待任意一个进程完成
    for process in processes:
        process.join()
