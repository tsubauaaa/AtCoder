import re
if __name__ == "__main__":
    S = input()
    if re.match('^(dream|dreamer|erase|eraser)+$', S):
        print('YES')
    else:
        print('NO')

