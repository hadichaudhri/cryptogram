import numpy as np
import sys


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


def parse_args(args, task_dict, flags_dict):
    try:
        if len(args) < 3:
            raise IndexError
        flag, n, msg = args[0], args[1], " ".join(args[2:])
    except IndexError as err:
        sys.exit(
            f"Congratulations! You fucked up the number of needed arguments!\nHere's your consolation prize: {err}."
        )

    try:
        command = task_dict[flags_dict[flag]]
    except KeyError as err:
        sys.exit(
            f"You screwed up the command flag (-e|-d|--encode|--decode) by writing this instead: {err}."
        )

    try:
        n = int(n)
    except ValueError:
        sys.exit("Given matrix size is not an integer!")

    return command, n, msg
