from random import choices, randint
from hamming.coding import N, check_input
from numpy import random

ERROR_PROBABILITY = 0.08
FRAME_LOSS_PROBABILITY = 0.02

def lose_frame(prob=FRAME_LOSS_PROBABILITY):
    return choices(
        population=[False, True], 
        weights=[1 - prob, prob],
        k=1)[0]

# выбор ошибочного бита через нормальное распределение
def choose_error_bit_normal(min_val: int, max_val: int, m = 150, sd = 15):
    error_bit = min_val - 1

    while error_bit not in range(min_val, max_val + 1):
        error_bit = int(random.normal(loc=m, scale=sd, size=None))

    return error_bit


def get_error_vector(prob=ERROR_PROBABILITY, length=N):
    is_corrupted = choices(
        population=[False, True], 
        weights=[1 - prob, prob],
        k=1)[0]
    error_vector_bits = [0 for _ in range(length)]

    if not is_corrupted:
        return ''.join([str(i) for i in error_vector_bits])
    error_bit_index = choose_error_bit_normal(0, length - 1)

    error_vector_bits[error_bit_index] ^= 1
    return ''.join([str(i) for i in error_vector_bits])

def insert_error(inf_v, error_v, length=N):
    check_input(inf_v, length)
    check_input(error_v, length)

    return ''.join([str(int(inf_v[i]) ^ int(error_v[i]))
          for i in range(length)])

from matplotlib import pyplot as plt
# проверка нормального распределения ошибки
def visualize_error_bit_normal():
    plt.hist([choose_error_bit_normal(0, 960) for _ in range(1_000_000)], bins=100)
    plt.show()