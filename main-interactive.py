# Usage: python interactive_runner.py python local_testing_tool.py 0 -- python3 main-interactive.py

import sys

log_file = open('log.txt', 'w+')

def log_to_file(data):
    log_file.write(str(data) + '\n')

def read_str(): return input()
def read_int(): return int(input())
def read_str_list(): return input().strip().split(' ')
def read_int_list(): return list(map(int, input().strip().split(' ')))
def read_lines(n, read_func): return [read_func() for _ in range(n)]
def list_to_str(l, sep=' '): return sep.join(map(str, l))

def query(q, read_func):
    print(q)
    sys.stdout.flush()
    return read_func()

def main():
    T, N = read_int_list()
    for _ in range(T):
        ans = solve(N)
        verdict = query(ans, read_str)
        # if is wrong answer, exit
        if verdict == '-1': # may need to change this
            sys.exit()

def solve(N):
    # solve the problem here
    ans = 0

    # example for querying something
    query_data = 1
    response = query(query_data, read_int)

    # example for writing something to a file when debugging
    log_to_file("query {} get {}".format(query_data, response))

    return ans

if __name__ == '__main__':
    main()
