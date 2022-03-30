def Alive(n,k):
    lst=[]
    for i in range(n):
        lst.append(i)
    c=k-1
    while(len(lst)>1):
        item=lst[(c)%len(lst)]
        inc=(c)%len(lst)
        lst.pop(inc)
        c+=k-1
        c=c%len(lst)
    return lst[0]

x=Alive(7,2)

print("The person whos is still alive =", x)
