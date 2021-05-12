import numpy as np
import sys


def list_chunk(l, n):
    """Breaks up a list into chunks of size n

    Args:
        l (ListLike|String): List to be broken up
        n (int): Size of each chunk

    Yields:
        List: Next chunk of size n
    """
    for i in range(0, len(l), n):
        sublist = l[i : i + n]
        while len(sublist) != n:
            sublist += [0]
        yield sublist


def char_to_ord(c):
    """Converts character to ordinal number

    Note:
        In this case ordinals are used to refer to the position of a letter
        in the alphabet, with space as 0, "A" as 1, and "Z" as 26.

    Args:
        c (string): Character to convert

    Returns:
        int: Ordinal number of character
    """
    if c == " ":
        return 0
    else:
        return ord(c) - 96


def ord_to_char(ord):
    """Converts ordinal number to character

    Note:
        See `char_to_int` for information on
        number scheme for ordinal numbers.

    Args:
        ord (int): Ordinal number to convert

    Returns:
        str: Character associated with ordinal number.
    """
    if ord == 0:
        return " "
    else:
        return chr(ord + 96)


def get_encoding_matrix(n):
    """Prompts user for information about the encoding matrix.

    Args:
        n (int): Size of the desired encoding matrix

    Returns:
        np.ndarray: The matrix specified by user input.
    """
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
            A = np.asarray(entries, dtype=int).reshape(n, n)
            # Force user to input new matrix if A is singular (rank != n)
            if np.linalg.matrix_rank(A) != n:
                raise np.linalg.LinAlgError
            return A
        except np.linalg.LinAlgError:
            print("Error: Singular matrix. Try again.")
        except ValueError:
            print(
                f"Error: Given data cannot be made into a valid {n}x{n} matrix. Try again."
            )
        finally:
            print("-" * 30)


def parse_args(args, task_dict, flags_dict):
    """Parses argument from command line input.

    Args:
        args (List[str]): List of arguments from command line input.
        task_dict (Dict): Dictionary mapping tasks to python functions.
        flags_dict (Dict): Dictionary mapping command line flags to tasks.

    Raises:
        IndexError: [description]

    Returns:
        3-element tuple containing

            - command (Function): Function specified by command flag.
            - n (int): Size of the encoding matrix.
            - msg (str): The given message (encoded or decoded)
    """
    try:
        if len(args) < 3:
            raise IndexError
        flag, n, msg = args[0], args[1], " ".join(args[2:])
    except IndexError as err:
        sys.exit(
            f"Congratulations! You messed up the number of needed arguments!\nHere's your consolation prize: {err}."
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
