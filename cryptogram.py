"""
cryptogram.py 
Created by Hadi Chaudhri, 11 May 2021
Literally created to solve my math homework 
"""

""" 
Program Outline


cryptogram.py [-e,-d] <n> <message>

'-e'/'--encode' flag -> encode
'-d'/'--decode' flag -> decode

n is the size of the matrix
message is the string to be encoded/decoded (space-delimited)

Program will then prompt for the n rows of the encryption matrix.

If -e specified, then program will print out encrypted row matrices.
If -d specified, then program will print out the original message.
"""

import numpy as np
import re
import sys


def decode(n, msg):
    print(msg)
    vectors = encoded_msg_to_vectors(n, msg)
    A = get_matrix(n)
    print(vectors)
    for vector in vectors:
        x = np.linalg.solve(np.transpose(A), vector)
        print(x)


def encode(n, msg):
    print(msg)
    vectors = decoded_msg_to_vectors(n, msg)
    print(vectors)
    A = get_matrix(n)
    for vector in vectors:
        b = vector * A
        print(b)


def validate_decoded_message(msg):
    ALPHABETIC_AND_SPACE_ONLY_REGEX = re.compile("^[a-zA-Z\s]*$")
    if ALPHABETIC_AND_SPACE_ONLY_REGEX.match(msg):
        sys.exit(f"The given message may only contain letters and spaces.")


def encoded_msg_to_vectors(n, msg):
    msg = msg.strip().split(" ")
    return [np.asarray(chunk, dtype=float) for chunk in msg_chunk(msg, n)]


def decoded_msg_to_vectors(n, msg):
    ALPHABETIC_AND_SPACE_ONLY_REGEX = re.compile("^[a-zA-Z\s]*$")
    if ALPHABETIC_AND_SPACE_ONLY_REGEX.match(msg):
        msg = msg.lower()
        num_list = [char_to_int(c) for c in msg]
        return [np.r_["r", chunk] for chunk in msg_chunk(num_list, n)]
    else:
        sys.exit(f"The given message may only contain letters and spaces.")


def msg_chunk(msg, n):
    for i in range(0, len(msg), n):
        sublist = msg[i : i + n]
        while len(sublist) != n:
            sublist += [0]
        yield sublist


def char_to_int(c):
    if c == " ":
        return 0
    else:
        return ord(c) - 96


def int_to_char(i):
    if i == 0:
        return " "
    else:
        return chr(i + 96)


def get_matrix(n):
    while True:
        entries = []
        for i in range(n):
            row = (
                input(
                    f"Please enter row {i+1} of the encoding matrix. (No brackets, spaces between numbers): "
                )
                .strip()
                .split(" ")
            )
            entries += row
        try:
            return np.asarray(entries, dtype=int).reshape(n, n)
        except Exception:
            print(
                f"Error: Given data cannot be made into a valid {n}x{n} matrix. Try again."
            )


def parse_args(args, task_dict):
    try:
        if len(args) < 3:
            raise IndexError
        flag, n, msg = args[0], args[1], " ".join(args[2:])
    except IndexError as err:
        sys.exit(
            f"Congratulations! You fucked up the number of needed arguments!\nHere's your consolation prize: {err}."
        )

    try:
        command = task_dict[FLAGS[flag]]
    except KeyError as err:
        sys.exit(
            f"You screwed up the command flag (-e|-d|--encode|--decode) by writing this instead: {err}."
        )

    try:
        n = int(n)
    except ValueError:
        sys.exit("Given matrix size is not an integer!")

    return command, n, msg


if __name__ == "__main__":
    FLAGS = {
        "-e": "encode",
        "--encode": "encode",
        "-d": "decode",
        "--decode": "decode",
    }
    TASK_DICT = {"encode": encode, "decode": decode}

    command, n, msg = parse_args(sys.argv[1:], TASK_DICT)
    try:
        command(n, msg)
    except Exception as err:
        sys.exit(f"Error: {err}")
