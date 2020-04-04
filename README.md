# gcj-python3-template
My Python3 template for Google Code Jam

## Preview

### main.py

```python
# use `log(...)` to print data when debugging
def log(*argv): pass
log = print # when debug is over, remove this line to mute log

def read_str(): return input()
def read_int(): return int(input())
def read_str_list(): return input().strip().split(' ')
def read_int_list(): return list(map(int, input().strip().split(' ')))
def read_lines(n, read_func): return [read_func() for _ in range(n)]
def list_to_str(l, sep=' '): return sep.join(map(str, l))

def main():
    T = read_int()
    for case_idx in range(1, T + 1):
        ans = solve()
        print("Case #{}: {}".format(case_idx, ans))

def solve():
    # example for reading input
    N = read_int()
    S = read_str()
    R, C = read_int_list()
    M = read_lines(N, read_int_list)

    # solve the problem here
    ans = 0

    # example for printing something when debugging
    log(M)

    return ans

if __name__ == '__main__':
    main()
```

### main-interactive.py

```python
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
```