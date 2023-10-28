n=int(input())
dp=[0]*(n+1)
for i in range(1,n+1):
    for j in range(i,n+1,i):
        if i*i!=j:
            dp[j]+=1
ans=0
for i in range(1,n):
    ans+=dp[n-i]-2*(n%i==0 and i*i+i!=n)
print(ans)