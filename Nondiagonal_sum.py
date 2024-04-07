
def nondiagonal_sum():
    list=[[1,2,3],[4,5,6],[7,8,9]]
    sum=0
    n=3
    for i in range(0,n):
        for j in range(0,n):
            if (i!=j)and (i+j)!=(n-1):
                sum=sum+list[i][j]
    print(sum)

nondiagonal_sum()
