# Код Хемминга [7, 4]
N = 7
K = 4

def is_bit_vector(vector):
    try:
        int(vector, 2)
    except:
        return False
    finally:
        return True

def is_power_of_two(num):
    return num & (num - 1) == 0

def is_bit_1(num, index):
    return num & (2 ** index) == 2 ** index

def check_input(vector, length):
    if not is_bit_vector(vector):
        raise Exception("not bit vector")

    if len(vector) != length:
        raise Exception(f"vector length is not {length}")
    

def hamming_encode(inf_v, n=N, k=K): 
    check_input(inf_v, k)
    
    inf_bits = list(inf_v) # входной вектор
    check_bits = [0 for _ in range(n - k)] # проверочные биты
    res_bits = list() # выходной вектор
    # сначала распределим инф. биты
    for i in range(1, n + 1):
        if not is_power_of_two(i): # если не является степенью двойки, то вставляем инф. бит
            bit = inf_bits.pop()
            res_bits.append(bit)
            # и изменим проверочные биты 
            for j in range(n - k):
                if is_bit_1(i, j):
                    check_bits[j] ^= int(bit)
        else: # пока поставим на место проверочных битов нули
            res_bits.append("0")
    # затем расставим полученные проверочные биты
    for i in range(n - k):
        res_bits[2 ** i - 1] = str(check_bits[i])

    res_bits.reverse()

    return ''.join(res_bits)


def hamming_find_error(recieved_v, n=N, k=K):
    check_input(recieved_v, n)

    # вектор ошибки
    e_bits = [0 for _ in range(n - k)]
    recieved_bits = list(reversed(recieved_v))
    for i in range(1, n + 1):
        for j in range(n - k):
            if is_bit_1(i, j):
                e_bits[j] ^= int(recieved_bits[i - 1])
    e_bits.reverse()
    return ''.join([str(i) for i in e_bits])


def hamming_decode(recieved_v, n=N, k=K):
    error = hamming_find_error(recieved_v, n=n, k=k)

    error_index = int(error, 2)

    recieved_bits = list(reversed(recieved_v))
    if error_index:
        recieved_bits[error_index - 1] = int(recieved_bits[error_index - 1]) ^ 1 # инвертируем бит

    inf_bits = []

    for i in range(1, n + 1):
        if not is_power_of_two(i):
            inf_bits.append(str(recieved_bits[i - 1]))

    inf_bits.reverse()
    return ''.join(inf_bits)       


def code_segment(segment, n=N, k=K):
    vectors = [segment[(i - k):i] for i in range(k, len(segment) + 1, k)]
    encoded_vectors = [hamming_encode(v) for v in vectors]
    return ''.join(encoded_vectors)

def decode_segment(segment, n=N, k=K):
    vectors = [segment[(i - n):i] for i in range(n, len(segment) + 1, n)]
    encoded_vectors = [hamming_decode(v) for v in vectors]
    return ''.join(encoded_vectors)