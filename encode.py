import numpy as np
import re
import sys
from utils import char_to_ord, get_encoding_matrix, list_chunk


def encode(n, msg):
    """Encodes a given message into a matrix of encoded ordinals.

    Args:
        n (int): Size of the encoding matrix
        msg (str): Given message
    """
    validate_message(msg)
    ord_matrix = msg_to_ord_matrix(n, msg)
    A = get_encoding_matrix(n)
    print("Input message:", ord_matrix, "", sep="\n")
    encoded_message = np.matmul(ord_matrix, A)
    print("Encoded message:", encoded_message, "", sep="\n")


def msg_to_ord_matrix(n, msg):
    """Converts given message to matrix of ordinals.

    Args:
        n (int): Width of the ordinal matrix
        msg (str): Given message

    Returns:
        np.ndarray: Matrix of ordinals corresponding to `msg`
    """
    msg = msg.lower()
    num_list = [char_to_ord(c) for c in msg]
    chunks = list(list_chunk(num_list, n))
    return np.asarray(chunks, dtype=float).reshape(len(chunks), n)


def validate_message(msg):
    """Ensures that message contains only letters and spaces, panicking otherwise.

    Args:
        msg (str): Given message
    """
    ALPHABETIC_AND_SPACE_ONLY_REGEX = re.compile("^[a-zA-Z\s]*$")
    if not (ALPHABETIC_AND_SPACE_ONLY_REGEX.match(msg)):
        sys.exit(f"The given message may only contain letters and spaces.")
