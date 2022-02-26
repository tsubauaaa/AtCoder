def check_yoko(h, w):
    if not (w + 5 <= N - 1):
        return False

    if (
        list(
            masus[h][w]
            + masus[h][w + 1]
            + masus[h][w + 2]
            + masus[h][w + 3]
            + masus[h][w + 4]
            + masus[h][w + 5]
        ).count("#")
        >= 4
    ):
        return True
    else:
        return False


def check_tate(h, w):
    if not (h + 5 <= N - 1):
        return False
    if (
        list(
            masus[h][w]
            + masus[h + 1][w]
            + masus[h + 2][w]
            + masus[h + 3][w]
            + masus[h + 4][w]
            + masus[h + 5][w]
        ).count("#")
        >= 4
    ):
        return True
    else:
        return False


def check_naname(h, w):
    if not (h + 5 <= N - 1 and w + 5 <= N - 1):
        return False

    if (
        list(
            masus[h][w]
            + masus[h + 1][w + 1]
            + masus[h + 2][w + 2]
            + masus[h + 3][w + 3]
            + masus[h + 4][w + 4]
            + masus[h + 5][w + 5]
        ).count("#")
        >= 4
    ):
        return True
    else:
        return False


def check_naname_reverse(h, w):
    if not (h + 5 <= N - 1 and w >= 5):
        return False
    if (
        list(
            masus[h][w]
            + masus[h + 1][w - 1]
            + masus[h + 2][w - 2]
            + masus[h + 3][w - 3]
            + masus[h + 4][w - 4]
            + masus[h + 5][w - 5]
        ).count("#")
        >= 4
    ):
        return True
    else:
        return False


N = int(input())
masus = []
for i in range(N):
    S = list(input())
    masus.append(S)

for i in range(N):
    for j in range(N):
        if (
            check_yoko(i, j)
            or check_tate(i, j)
            or check_naname(i, j)
            or check_naname_reverse(i, j)
        ):
            print("Yes")
            exit()
print("No")
