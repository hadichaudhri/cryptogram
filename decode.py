import numpy as np
import re
import sys
from utils import get_encoding_matrix, ord_to_char, list_chunk


def decode(n, msg):
    """Decodes a given encoded string into the original message

    Args:
        n (int): Size of the encoding matrix
        msg (str): Space-delimited string of encoded ordinals
    """
    validate_encoded_message(msg)
    encoded_ords = encoded_ords_to_matrix(n, msg)
    A = get_encoding_matrix(n)
    print(f"Input message:", encoded_ords, sep="\n")
    # Transpose yA=b to get A^t*y^t=b^t, which can be solved using numpy
    decoded_ords = np.linalg.solve(np.transpose(A), np.transpose(encoded_ords))
    decoded_msg = decoded_ord_matrix_to_msg(decoded_ords)
    print(f"Decoded Message: {decoded_msg}")


def decoded_ord_matrix_to_msg(matrix):
    """Converts a matrix of ordinals into the original message.

    Args:
        matrix (np.ndarray): Matrix of decoded ordinals

    Returns:
        str: Message corresponding to the matrix of orbitals
    """
    decoded_msg = (
        "".join([ord_to_char(round(i)) for i in matrix.flatten(order="F")])
        .upper()
        .strip()
    )
    return decoded_msg


def encoded_ords_to_matrix(n, ords):
    """Converts a list of encoded ordinals into a matrix of encoded ordinals.

    Args:
        n (int): Width of the encoded ordinal matrix
        ords (str): Space-delimited string of encoded ordinals

    Returns:
        np.ndarray: Matrix of encoded ordinals corresponding to `ords`.
    """
    ords = ords.strip().split(" ")
    chunks = list(list_chunk(ords, n))
    return np.asarray(chunks, dtype=float).reshape(len(chunks), n)


def validate_encoded_message(msg):
    """Ensures that the encoded message only contains numbers and spaces

    Args:
        msg (str): Space-delimited string of encoded orbitals
    """
    NUMERIC_AND_SPACE_ONLY_REGEX = re.compile("^[0-9\s]*$")
    if not (NUMERIC_AND_SPACE_ONLY_REGEX.match(msg)):
        sys.exit(f"The encoded message may only contain numbers and spaces.")
