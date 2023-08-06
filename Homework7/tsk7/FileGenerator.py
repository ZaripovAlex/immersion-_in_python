from os import getcwd, listdir, mkdir
from random import randint

ASCII_MIN = 98
ASCII_MAX = 122
MIN_BYTE = 256
MAX_BYTE = 4096

__all__ =["name_generator", "file_generator"]
def name_generator(min_len: int = 4, max_len: int = 12):
    res = ''
    for _ in range(min_len, max_len):
        res += chr(randint(ASCII_MIN, ASCII_MAX))
    # print (res)
    return res.capitalize()


def file_generator(directory: str, count: int = 20):
    ext = '.txt'
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'
    for _ in range(count):
        with open(directory + name_generator() + ext, "wb") as f:
            data = bytes(randint(0, 255) for _ in range(MIN_BYTE, MAX_BYTE))
            f.write(data)


if __name__ == '__main__':
    file_generator(directory= "test", count=40)