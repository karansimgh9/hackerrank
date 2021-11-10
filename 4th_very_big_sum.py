n =int(input(''))
s = 0
a = list(map(int, input().rstrip().split()))
for i in range(len(a)):
  s +=a[i]
print(s)
