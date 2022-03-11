def BinSrch(List,x):
    Low = 0
    High = len(List)-1
    F=False
    while Low <= High and not F:
        mid= High//2
        if x == List[mid]:
            F=True
        elif x > List[mid]:
            Low= mid+1
        else:
            High = mid -1
    if F==True:
        print("key element is present")
    else:
        print("not present")


List=[2,56,23,7,8,9,11]
List.sort()
x=int(input("enter the element to be found"))
BinSrch(List,x)