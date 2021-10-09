K=int(input())

evens = 0
for i in range(1, K+1):
    if i % 2 == 0:
        evens += 1

print(evens*(K-evens))
    
