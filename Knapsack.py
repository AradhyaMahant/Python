def knapSack(capacity, wt, profit, n):
    if(n==0 or capacity==0):
        return 0
    if (wt[n-1] > capacity):
        return knapSack(capacity, wt, profit, n-1)
 
    else:
        return max(
            profit[n-1] + knapSack(
                capacity-wt[n-1], wt, profit, n-1),
            knapSack(capacity, wt, profit, n-1))
 

print('enter profits')
profit=list(map(int,input().split(' ')))
print('enter weights')
wt=list(map(int,input().split(' ')))
capacity= int(input("enter the max capacity"))
n = len(wt)
print(knapSack(capacity, wt, profit, n))