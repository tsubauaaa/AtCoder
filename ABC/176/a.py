import math
if __name__ == "__main__":
    N, X, T = [int(i) for i in input().split()]
    set_num = math.ceil(N / X)
    print(set_num * T)
    