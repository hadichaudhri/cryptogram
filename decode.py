import numpy as np
from utils import char_to_int, get_matrix, msg_chunk


def decode(n, msg):
    print(msg)
    vectors = msg_to_vectors(n, msg)
    A = get_matrix(n)
    print(vectors)
    for vector in vectors:
        x = np.linalg.solve(np.transpose(A), vector)
        print(x)


def msg_to_vectors(n, msg):
    msg = msg.strip().split(" ")
    return [np.asarray(chunk, dtype=float) for chunk in msg_chunk(msg, n)]
