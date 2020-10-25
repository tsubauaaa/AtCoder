N = int(input())
res = []
for i in range(N):
    S, P = map(str, input().split())
    res.append({"city": S, "score": int(P), "index": i})

res = sorted(res, key=lambda x: x["score"], reverse=True)
res = sorted(res, key=lambda x: x["city"])

for r in res:
    print(r["index"] + 1)
