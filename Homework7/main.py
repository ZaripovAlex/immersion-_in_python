from tsk7.FileGenerator import file_generator
from tsk7.Task2 import rename

if __name__ == '__main__':
    file_generator(directory="test", count= 40)
    rename(wanted_name="qaz")