import re

S = input()
ans = "WA"
if (
    S[0] == "A"
    and S[2:-1].count("C") == 1
    and re.match(r"^[a-z]+$", S.replace("A", "").replace("C", ""))
):
    ans = "AC"

print(ans)
