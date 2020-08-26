import ipdb
from memory_profiler import profile

@profile
def main():
    color_list = [*range(30, 37), *range(90, 91)]
    for color in color_list:
        print ('\033[%dm'%color, 'Hello!', '\033[0m', sep='')

main()
