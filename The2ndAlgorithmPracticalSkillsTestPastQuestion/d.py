# 文字列Tが文字列Sにマッチするかどうかを判定する関数
# マッチするときはTrueを、マッチしないときはFalseを返す
def is_match(T, S):

    # 文字列Sのi文字目から始まる部分が文字列Tとマッチするかどうか調べる
    for i in range(len(S)-len(T)+1):
        # 文字列Sのi文字目から始まる部分が
        # 文字列Tとマッチしているかどうかを保持する変数
        ok = True

        # 文字列Tのj文字列目と、文字列Sのi+j文字列目を見比べる
        for j in range(len(T)):
            # 文字列Tのj文字目が文字列Sのi+j文字目と異なっていて
            # かつ、文字列Tのj文字目が "." でもない場合、
            # 文字列Sのi文字目から始まる部分は文字列Tとマッチしない
            if S[i+j] != T[j] and T[j] != ".":
                ok = False

        # 文字列Sのi文字目から始まる部分が文字列Tとマッチしている場合
        # True を返す
        if ok:
            return True

    # 文字列Sの全ての部分について文字列Tとマッチしなかった場合、Falseを返す
    return False


S = input()
chars = "abcdefghijklmnopqrstuvwxyz."
ans = []
for i in range(len(chars)):
    if is_match(chars[i], S):
        ans.append(chars[i])

for i in range(len(chars)):
    for j in range(len(chars)):
        if is_match(chars[i]+chars[j], S):
            ans.append(chars[i]+chars[j])

for i in range(len(chars)):
    for j in range(len(chars)):
        for k in range(len(chars)):
            if is_match(chars[i]+chars[j]+chars[k], S):
                ans.append(chars[i]+chars[j]+chars[k])

print(len(ans))
