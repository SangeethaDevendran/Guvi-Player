cha,che=map(str,input().split())
if(len(cha)!=len(che)):
    print("no")
else:
  r=[cha.count(i) for i in cha]
  t=[che.count(i) for i in che]
if(r==t):
    print("yes")
else:
    print("no")
