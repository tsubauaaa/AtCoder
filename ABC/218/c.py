def rotate(mat):
    r_mat = []
    for i in range(N):
        row = []
        for j in range(N-1, 0, -1):
            row.append(mat[i][j])
        r_mat.append(row)
    return r_mat

def cut_width(mat):
    cw_mat = []
    for i in range(N):
        if len(set(mat[i])) == 1 and mat[i][0] == ".":
            continue
        cw_mat.append(S[i])
    return cw_mat


def cut_height(mat):
    ch_mat = []
    cuts = []
    for i in range(N):
        row = [r[i] for r in mat]
        if len(set(row)) == 1 and row[0] == ".":
            cuts.append(i)
    
    for i in range(len(mat)):
        g = []
        for j in range(N):
            if j in cuts:
                continue
            g.append(mat[i][j])
        ch_mat.append(g)
    return ch_mat


N=int(input())
S = []
for i in range(N):
    S.append(list(input()))
T = []
for i in range(N):
    T.append(list(input()))


cutw_S = cut_width(S)
cut_S = cut_height(cutw_S)
print(cut_S)

cutw_T = cut_width(T)
cut_T = cut_height(cutw_T)
print(cut_T)

