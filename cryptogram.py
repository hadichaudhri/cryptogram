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

import sys
from decode import decode
from encode import encode
from utils import parse_args

if __name__ == "__main__":
    FLAGS = {
        "-e": "encode",
        "--encode": "encode",
        "-d": "decode",
        "--decode": "decode",
    }
    TASK_DICT = {"encode": encode, "decode": decode}

    command, n, msg = parse_args(sys.argv[1:], TASK_DICT, FLAGS)
    try:
        command(n, msg)
    except Exception as err:
        sys.exit(f"Error: ({type(err)}) {err}")
