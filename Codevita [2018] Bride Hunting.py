'''Bride Hunting
Sam is an eligible bachelor. He decides to settle down in life and start a family. He goes bride hunting.

He wants to marry a girl who has at least one of the 8 qualities mentioned below:-

The girl should be rich
The girl should be an Engineer/Doctor
The girl should be beautiful
The girl should be of height 5.3"
The girl should be working in an MNC
The girl should be an extrovert
The girl should not have spectacles
The girl should be kind and honest
He is in search of a bride who has some or all of the 8 qualities mentioned above. On bride hunting, he may find more than one contenders to be his wife.

In that case, he wants to choose a girl whose house is closest to his house. Find a bride for Sam who has maximum qualities. If in case, there are more than one contenders who are at equal distance from Sam’'s house; then

print Polygamy not allowed

In case there is no suitable girl who fits the criteria then print No suitable girl found

Given a Matrix N*M, Sam’s house is at (1, 1). It is denoted by 1. In the same matrix, the location of a marriageable Girl is also denoted by 1. Hence 1 at location (1, 1) should not be considered as the location of a marriageable Girl’s location.
The qualities of that girl, as per Sam’'s criteria, have to be decoded from the number of non-zero neighbors (max 8-way) she has. Similar to the condition above, 1 at location (1, 1) should not be considered as the quality of a Girl. See Example section to get a better understanding.
Find Sam, a suitable Bride and print the row and column of the bride, and find out the number of qualities that the Bride possesses.
Distance is calculated in number of hops in any direction i.e. (Left, Right, Up, Down and Diagonal)
Constraints
2 <= N,M <= 10^2
Input Format
First Line contains the row (N) and column (M) of the houses.
Next N lines contain the data about girls and their qualities.

Output
It will contain the row and column of the bride, and the number of qualities that Bride possess separated by a colon (i.e. :).

Explanation
Input:

2 9
1 0 1 1 0 1 1 1 1
0 0 0 1 0 1 0 0 1
Output:

1:7:3
Explanation:

The girl and qualities are present at (1,3),(1,4),(1,6),(1,7),(1,8),(1,9),(2,4),(2,6),(2,9).
The girl present at (1,3) has 2 qualities (i.e. (1,4)and (2,4)).
The girl present at (1,4) has 2 qualities.
The Bride present at (1,6) has 2 qualities.
The Bride present at (1,7) has 3 qualities.
The Bride present at (1,8) has 3 qualities.
The Bride present at (1,9) has 2 qualities.
The Bride present at (2,4) has 2 qualities.
The Bride present at (2,6) has 2 qualities.
The Bride present at (2,9) has 2 qualities.
As we see, there are two contenders who have maximum qualities, one is at (1,7) and another at (1,8).
The girl who is closest to Sam’s house is at (1,7). Hence, she is the bride.
Hence, the output will be 1:7:3.

Input:

6 6
1 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 0
0 0 1 1 1 0
0 0 1 1 1 0
0 0 0 0 0 0
Output:

4:4:8
Explanation:

The bride and qualities are present at (3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)
The Bride present at (3,3) has 3 qualities (i.e. (3,4),(4,3) and (4,4)).
The Bride present at (3,4) has 5 qualities.
The Bride present at (3,5) has 3 qualities.
The Bride present at (4,3) has 5 qualities.
The Bride present at (4,4) has 8 qualities.
The Bride present at (4,5) has 5 qualities.
The Bride present at (5,3) has 3 qualities.
The Bride present at (5,4) has 5 qualities.
The Bride present at (5,5) has 3 qualities.
As we see, the girl present in (4,4) has maximum number of Qualities. Hence, she is the bride.

Hence, the output will be 4:4:8.

'''
'''def sumre(r,c,i,j,arr):
    s=0
    if 0<=i-1<=r-1 and 0<=j-1<=c-1:
        if arr[i-1][j-1]>0:
            s+=1
    if 0<=i-1<=r-1 and 0<=j<=c-1:
        if arr[i-1][j]>0:
            s+=1
    if 0<=i-1<=r-1 and 0<=j+1<=c-1:
        if arr[i-1][j+1]>0:
            s+=1
    if 0<=i<=r-1 and 0<=j-1<=c-1:
        if arr[i][j-1]>0:
            s+=1
    #if 0<=i<=r and 0<=j<=c:
        #s+=arr[i][j]
    if 0<=i<=r-1 and 0<=j+1<=c-1:
        if arr[i][j+1]>0:
            s+=1
    if 0<=i+1<=r-1 and 0<=j-1<=c-1:
        if arr[i+1][j-1]>0:
            s+=1
    if 0<=i+1<=r-1 and 0<=j<=c-1:
        if arr[i+1][j]>0:
            s+=1
    if 0<=i+1<=r-1 and 0<=j+1<=c-1:
        if arr[i+1][j+1]>0:
            s+=1
    arr[i][j]=s
    return arr,s





r,c=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(r)]
arr[0][0]=0
maxe=0
for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            arr,temax=sumre(r, c, i, j, arr)
            maxe=max(maxe,temax)
if maxe==0:
    print("No suitable girl found")
    exit()
dic={}
for i in range(r):
    for j in range(c):
        if arr[i][j]==maxe:
            t=(i+1,j+1)
            sum=max(i,j)
            if sum in dic:
                print("Polygamy not allowed")
                exit()
            else:
                dic[sum]=t


p=sorted(dic)
a,b=dic[p[0]]
print(a,":",b,":",maxe,sep="")
exit()
'''

def sumre(r,c,i,j,arr):
    s=0
    if 0<=i-1<=r-1 and 0<=j-1<=c-1:
        if arr[i-1][j-1]>0:
            s+=1
    if 0<=i-1<=r-1 and 0<=j<=c-1:
        if arr[i-1][j]>0:
            s+=1
    if 0<=i-1<=r-1 and 0<=j+1<=c-1:
        if arr[i-1][j+1]>0:
            s+=1
    if 0<=i<=r-1 and 0<=j-1<=c-1:
        if arr[i][j-1]>0:
            s+=1
    #if 0<=i<=r and 0<=j<=c:
        #s+=arr[i][j]
    if 0<=i<=r-1 and 0<=j+1<=c-1:
        if arr[i][j+1]>0:
            s+=1
    if 0<=i+1<=r-1 and 0<=j-1<=c-1:
        if arr[i+1][j-1]>0:
            s+=1
    if 0<=i+1<=r-1 and 0<=j<=c-1:
        if arr[i+1][j]>0:
            s+=1
    if 0<=i+1<=r-1 and 0<=j+1<=c-1:
        if arr[i+1][j+1]>0:
            s+=1
    arr[i][j]=s
    return arr,s





r,c=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(r)]
arr[0][0]=0
maxe=0
for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            arr,temax=sumre(r, c, i, j, arr)
            maxe=max(maxe,temax)
if maxe==0:
    print("No suitable girl found")
    exit()
dic1={}
dic2={}
for i in range(r):
    for j in range(c):
        if arr[i][j]==maxe:
            t=(i+1,j+1)
            sum=i+j
            dic1[sum] = t
            if sum in dic2:
                dic2[sum]+=1
            else:
                dic2[sum]=1



p=sorted(dic1)
if dic2[p[0]]>1:
    print("Polygamy not allowed")
else:
    a,b=dic1[p[0]]
    print(a,":",b,":",maxe,sep="")
    exit()
