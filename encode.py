import numpy as np
import re
import sys
from utils import char_to_int, get_matrix, msg_chunk


def encode(n, msg):
    validate_message(msg)
    vectors = msg_to_vectors(n, msg)
    A = get_matrix(n)
    for vector in vectors:
        b = vector * A
        print(b)


def validate_message(msg):
    ALPHABETIC_AND_SPACE_ONLY_REGEX = re.compile("^[a-zA-Z\s]*$")
    if not (ALPHABETIC_AND_SPACE_ONLY_REGEX.match(msg)):
        sys.exit(f"The given message may only contain letters and spaces.")


def msg_to_vectors(n, msg):
    msg = msg.lower()
    num_list = [char_to_int(c) for c in msg]
    return [np.r_["r", chunk] for chunk in msg_chunk(num_list, n)]
