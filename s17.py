cha=list(input())
for i in range(0,len(cha),2):
    cha[i],cha[i+1]=cha[i+1],cha[i]
sha=''.join(cha)
print(sha)
