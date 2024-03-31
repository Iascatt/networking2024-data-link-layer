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
    error_bits = choices(
        population=[0, 1],
        weights=[1 - prob, prob],
        k=length)
    return ''.join([str(i) for i in error_bits])

def insert_error(inf_v, error_v=get_error_vector(), length=N):
    check_input(inf_v, length)
    check_input(error_v, length)

    return ''.join([str(int(inf_v[i]) ^ int(error_v[i]))
          for i in range(length)])