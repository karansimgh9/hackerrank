n= int(input())
g=[]
for i in range(n):
  j=int(input())
  g.append(j)
def grade(l):
  for i in range(len(l)):
    if l[i]>37:
      if (l[i]%5)!=0:
        if(5-l[i]%5)<3:
          l[i]+=5-(l[i]%5)
  return ('\n'.join(map(str, l)))

print(grade(g))
