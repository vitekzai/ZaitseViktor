import hashlib
import time
import threading
import multiprocessing

alphabet = "abcdefghijklmnopqrstuvwxyz"

def gen_pass(index):
    password = ""
    for i in range(5):
        password += alphabet[index % len(alphabet)]
        index = index // len(alphabet)
    return password[::-1]

def sha256_selection(index, hashes, start, end):
    for i in range(start, end):
        password = gen_pass(i)
        hash = hashlib.sha256(password.encode()).hexdigest()
        for h in hashes:
            if hash != h:
                continue
            print("Хэш {} найден пароль: {}. Поток {}.".format(hash, password, index))

def sha256():
    hashes = ["1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad",
              "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b",
              "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"]
    P = 26**5
    cpu = multiprocessing.cpu_count()
    print ("Количество ядер на вашем компьютере: {}".format(cpu))
    #threads
    while True:
        n_threads = int(input("Количество потоков для SHA256: "))
        if n_threads > 0:
            break
        else:
            print("Введите положительное число!")
    start_time = time.perf_counter()
    per_thread = P // n_threads
    lost_p = P - 5 * per_thread

    threads = []
    start = 0
    for i in range(n_threads):
        if i == n_threads:
            end = start + per_thread + lost_p
        else:
            end = start + per_thread
        thr = threading.Thread(target=sha256_selection, args=(i, hashes, start, end))
        threads.append(thr)
        thr.start()
        start = end
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Время выполнения: {}.".format(elapsed_time))
    #multiprocessing
    while True:
        n_proc = int(input("Количество процессов для SHA256 в диапазоне от 1 до {}: ".format(cpu)))
        if n_proc > 0 and n_proc <= cpu:
            break
        else:
            print("Число должно быть положительным и не превышать количество ядер процессора!")
    start_time = time.perf_counter()
    per_proc = P // n_proc
    lost_p = P - 5 * per_proc

    threads = []
    start = 0
    for i in range(n_proc):
        if i == n_proc:
            end = start + per_proc + lost_p
        else:
            end = start + per_proc
        proc = multiprocessing.Process(target=sha256_selection, args=(i, hashes, start, end))
        threads.append(proc)
        proc.start()
        start = end
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Время выполнения: {}.".format(elapsed_time))

def md5_selection(index, hashes, start, end):
    for i in range(start, end):
        password = gen_pass(i)
        hash = hashlib.md5(password.encode()).hexdigest()
        for h in hashes:
            if hash != h:
                continue
            print("Хэш {} найден пароль: {}. Поток {}.".format(hash, password, index))

def md5():
    hashes = ["81d45c9cf678fbaa8d64a6f29a6f97e3",
              "1f3870be274f6c49b3e31a0c6728957f",
              "d9308f32f8c6cf370ca5aaaeafc0d49b"]
    P = 26**5
    cpu = multiprocessing.cpu_count()
    print ("Количество ядер на вашем компьютере: {}".format(cpu))
    #threads
    while True:
        n_threads = int(input("Количество потоков для MD5: "))
        if n_threads > 0:
            break
        else:
            print("Введите положительное число!")
    start_time = time.perf_counter()
    per_thread = P // n_threads
    lost_p = P - 5 * per_thread

    threads = []
    start = 0
    for i in range(n_threads):
        if i == n_threads:
            end = start + per_thread + lost_p
        else:
            end = start + per_thread
        thr = threading.Thread(target=md5_selection, args=(i, hashes, start, end))
        threads.append(thr)
        thr.start()
        start = end
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Время выполнения: {}.".format(elapsed_time))
    #multiprocessing
    while True:
        n_proc = int(input("Количество процессов для MD5 в диапазоне от 1 до {}: ".format(cpu)))
        if n_proc > 0 and n_proc <= cpu:
            break
        else:
            print("Число должно быть положительным и не превышать количество ядер процессора!")
    start_time = time.perf_counter()
    per_proc = P // n_proc
    lost_p = P - 5 * per_proc

    threads = []
    start = 0
    for i in range(n_proc):
        if i == n_proc:
            end = start + per_proc + lost_p
        else:
            end = start + per_proc
        proc = multiprocessing.Process(target=md5_selection, args=(i, hashes, start, end))
        threads.append(proc)
        proc.start()
        start = end
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Время выполнения: {}.".format(elapsed_time))

if __name__ == '__main__':
    sha256()
    md5()
