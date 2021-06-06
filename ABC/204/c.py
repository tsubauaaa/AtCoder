def connected_components(graph):
    seen = set()

    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)


def print_gen(gen):
    return [list(x) for x in gen]


N, M = map(int, input().split())
f_graph = {i + 1: [] for i in range(N)}
b_graph = {i + 1: [] for i in range(N)}
for i in range(M):
    A, B = map(int, input().split())
    if A < B:
        f_graph[A].append(B)
    else:
        b_graph[A].append(B)

print(f_graph, b_graph)

print(connected_components(b_graph))

f_cons = [list(x) for x in connected_components(f_graph)]
b_cons = [list(x) for x in connected_components(b_graph)]
print(f_cons, b_cons)


f = 0
for f_con in f_cons:
    f += len(f_con) * (len(f_con) - 1) // 2

b = 0
is_turned = False
for b_con in b_cons:
    b += len(b_con) * (len(b_con) - 1) // 2
    if b_con == [1, N]:
        is_turned = True

if len(f_cons) == 1 and is_turned:
    print(N * N)
else:
    print(N + f + b)
