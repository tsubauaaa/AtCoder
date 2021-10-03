A,B = map(int,input().split())
 
for C in (1,2,3):
  if A*B*C % 2 != 0:
    print("Yes")
    exit()
    
print("No")