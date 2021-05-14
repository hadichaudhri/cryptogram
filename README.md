# cryptogram
Python script to encode and decode cryptograms using encoding matrices.

## Requirements
- Python 3+

## Installation
1. Clone the repository using
```bash
> git clone https://github.com/hadichaudhri/cryptogram.git
```
2. Install python dependencies using
```bash
> pip install -r requirements.txt
```

## Usage
```bash
> cryptogram.py [-e|--encode|-d|--decode] <size of the encoding matrix> <message>
## The encoding matrix for all of these examples is [[1, 2], [3, 5]]
# To encode the message `COME HOME SOON` with a user-provided 2x2 encoding matrix
> cryptogram.py -e 2 COME HOME SOON
2 48 81 28 51 24 40 54 95 5 10 64 113 57 100
# To decode the message `2 48 81 28 51 24 40 54 95 5 10 64 113 57 100` with a user-provided 2x2 encoding matrix
> .\cryptogram.py -d 2 48 81 28 51 24 40 54 95 5 10 64 113 57 100
COME HOME SOON
```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
