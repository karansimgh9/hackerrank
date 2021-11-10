
a=int(input())
b=list(map(int, input().split()))
c=max(b)
d=0
for i in range(a):
  if b[i]==c:
    d+=1
print(d)