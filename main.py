
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
