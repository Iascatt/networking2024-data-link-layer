from random import choices, randint
from hamming.coding import N, check_input

ERROR_PROBABILITY = 0.08
FRAME_LOSS_PROBABILITY = 0.02

def lose_frame(prob=FRAME_LOSS_PROBABILITY):
    return choices(
        population=[False, True], 
        weights=[1 - prob, prob],
        k=1)[0]

def get_error_vector(prob=ERROR_PROBABILITY, length=N):
    is_corrupted = choices(
        population=[False, True], 
        weights=[1 - prob, prob],
        k=1)[0]
    
    error_vector_bits = [0 for _ in range(length)]
    if not is_corrupted:
        return ''.join([str(i) for i in error_vector_bits])
    error_bit_index = randint(0, length - 1)
    error_vector_bits[error_bit_index] ^= 1
    return ''.join([str(i) for i in error_vector_bits])

def insert_error(inf_v, error_v=get_error_vector(), length=N):
    check_input(inf_v, length)
    check_input(error_v, length)

    return ''.join([str(int(inf_v[i]) ^ int(error_v[i]))
          for i in range(length)])