if __name__ == "__main__":
    a, b = map(int, input().split())

    print('Even' if a*b%2==0 else 'Odd')