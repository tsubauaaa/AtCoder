if __name__ == "__main__":
    s = input()
    t = input()

    for i, e in enumerate(t):
        compare_t = t[0:len (t) - i]
        if compare_t in s:
            print(f'{s}, {compare_t}')

    #         print(i+len(t) - len(t))
            break
    # print(len(t))
