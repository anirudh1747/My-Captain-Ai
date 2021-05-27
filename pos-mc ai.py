a=input()
g=a[1:-1]
q=g.split(",")
for i in q:
    if int(i)>=0:
        print(i,end=",")
