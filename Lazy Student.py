'''There is a test of Algorithms. Teacher provides a question bank consisting of N questions and guarantees all the questions in the test will be from this question bank. Due to lack of time and his laziness, Codu could only practice M questions. There are T questions in a question paper selected randomly. Passing criteria is solving at least 1 of the T problems. Codu can't solve the question he didn't practice. What is the probability that Codu will pass the test?

Constraints
0 < K <= 10000
0 < N, T <= 1000
0 <= M <= 1000
M,T <= N
Input Format
First line contains single integer K denoting the number of test cases.
First line of each test case contains 3 integers separated by space denoting N, T, and M.
Output
For each test case, print a single integer.
If probability is p/q where p & q are co-prime, print  (p*mulInv(q)) modulo 1000000007, where mulInv(x) is multiplicative inverse of x under modulo 1000000007.
Example Input 1
1
4 2 1
Output
500000004
Explanation
The probability is 1/2. So output is 500000004

'''
import math

def mult(a,b,prime):
    ans = (a%prime * b%prime)%prime
    return ans

K = int(input())
max_n = 1000
prime = 10**9+7


### generating pascal's triangle
pascals = [[0 for i in range(max_n+1)] for j in range(max_n+1)] # 1-indexed
pascals[0][0] = 1

for i in range(1,len(pascals)):
    pascals[i][0] = 1
    for j in range(1,i+1):
        pascals[i][j] = (pascals[i-1][j-1] + pascals[i-1][j])%prime
    #print(pascals[i])



for case in range(K):
    N,T,M = list(map(int, input().split()))

    if N-M < T:
        print(1)
        continue
    if M == 0:
        print(0)
        continue

    denominator =  pascals[N][T]
    numerator = pascals[N-M][T]

    p = denominator-numerator
    q = denominator

    # reducing them
    common = math.gcd(p,q)
    p = p//common
    q = q//common

    q_inv = pow(q,prime-2,prime)
    ans = mult(p,q_inv,prime)

    print(ans)