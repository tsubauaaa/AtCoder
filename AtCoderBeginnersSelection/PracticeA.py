

if __name__ == "__main__":
    i = [input() for i in range(3)]
    a = int(i[0])
    b = int(i[1].split(' ')[0])
    c = int(i[1].split(' ')[1])
    s = i[2]
    sum = a + b+ c

    print(f'{sum} {s}')