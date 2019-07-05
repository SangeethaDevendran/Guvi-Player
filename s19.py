cha,cho=map(int,input().split())
saa=[]
for p in range(cha+1,cho+1):
  if p>1:
    for f in range(2,p):
      if(p%f==0):
        break
    else:
      saa.append(f)
print(len(saa)+1)
