arr=[]
n=int(input("enter the no. of elemnts in a list"))
     
for a in range(n): 
    l=int(input())
    arr.append(l)
     
found = False

x=int(input("enter the value to be found")) 
      
for i in range(len(arr)):
    if x == arr[i]:
        found = True
        print("element is present and is =", x )
        break

if not found:
  print("no found")
