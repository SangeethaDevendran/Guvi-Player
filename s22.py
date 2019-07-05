saa,haa=map(int,input().split())
caa=list(map(int,input().split()))
for i in range(0,saa):
  caa=[caa[-1]] + caa[:-1]
print(*caa,end=' ')
