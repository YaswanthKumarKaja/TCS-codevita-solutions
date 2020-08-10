'''Min Product Array
The task is to find the minimum sum of Products of two arrays of the same size, given that k modifications are allowed on the first array. In each modification, one array element of the first array can either be increased or decreased by 2.

Note- the product sum is Summation (A[i]*B[i]) for all i from 1 to n where n is the size of both arrays

Input Format:
First line contains T, the number of test cases, Following T lines contain:
First line of the input contains n and k delimited by whitespace
Second line contains the Array A (modifiable array) with its values delimited by spaces
Third line contains the Array B (non-modifiable array) with its values delimited by spaces
Output Format:
Output the minimum sum of products of the two arrays

Constraints:
1 ≤ N ≤ 10^5
0 ≤ |A[i]|, |B[i]| ≤ 10^5
0 ≤ K ≤ 10^9
Sample Input & Output
Input:

1
3 5
1 2 -3
-2 3 -5
Output:

-31
Explanation

Here total numbers are 3 and total modifications allowed are 5. So we modified A[2], which is -3 and increased it by 10 (as 5 modifications are allowed). Now final sum will be

(1 * -2) + (2 * 3) + (7 * -5)
-2 + 6 - 35
-31
-31 is our final answer.

Input:

1
5 3
2 3 4 5 4
3 4 2 3 2
Output:

25
Explanation

Here total numbers are 5 and total modifications allowed are 3. So we modified A[1], which is 3 and decreased it by 6 (as 3 modifications are allowed).
Now final sum will be

(2 * 3) + (-3 * 4) + (4 * 2) + (5 * 3) + (4 * 2)
6 - 12 + 8 + 15 + 8
25
25 is our final answer.
'''
T=int(input())
for T1 in range(T):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    sume=0
    for i in range(n):
        sume+=A[i]*B[i]
    minsume=sume
    for i in range(n):
        temp=min(((A[i]+(2*k))*B[i]),((A[i]-(2*k))*B[i]))
        tempsume=sume-(A[i]*B[i])+temp
        if tempsume<minsume:
            minsume=tempsume
    print(minsume)


