N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
    exit()


def get_xor(a, b):
    ans = bin(a ^ b)
    return int(ans, 2)


def get_or(nums):
    ans = bin(nums[0] | nums[1])
    ans = int(ans, 2)
    if len(nums) > 2:
        for i in range(2, len(nums)):
            ans = bin(ans | nums[i])
            ans = int(ans, 2)
    return ans


ans = 10 ** 6
for i in range(1, N):
    # print(A[:i], A[i:])
    if len(A[:i]) == 1:
        a = A[:i][0]
    else:
        a = get_or(A[:i])

    if len(A[i:]) == 1:
        b = A[i:][0]
    else:
        b = get_or(A[i:])

    c = get_xor(a, b)

    ans = min(ans, c)
print(ans)
