'''Collecting Candies
Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to.

He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box. Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. Assume that there are infinite number of empty boxes available.

At a time he can pick up any two boxes for transferring and if both the boxes say contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. As he is to eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected.

Input Format
First line of input is number of test case T
Each test case is comprised of two inputs
First input of a test case is the number of boxes N
Second input is N integers delimited by whitespace denoting number of candies in each box
Output Format:
Print minimum time required, in seconds, for each of the test case. Print each output on a new line.

Constraints:
1 ≤T≤10
1 ≤N≤ 10000
1 ≤ [Candies in each box] ≤ 100009
Sample Input and Output
Input

1
4
1 2 3 4
Output

19
Explanation

4 boxes, each containing 1, 2, 3 and 4 candies respectively.

Adding 1 + 2 in a new box takes 3 seconds

Adding 3 + 3 in a new box takes 6 seconds

Adding 4 + 6 in a new box takes 10 seconds

Hence total time taken is 19 seconds. There could be other combinations also, but overall time does not go below 19 seconds.

Input

1
5
1 2 3 4 5
Output

33
Explanation

5 boxes, each containing 1, 2, 3, 4 and 5 candies respectively.

Adding 1 + 2 in a new box takes 3 seconds

Adding 3 + 3 in a new box takes 6 seconds

Adding 4 + 5 in a new box takes 9 seconds

Adding 6 + 9 in a new box takes 15 seconds

Hence total time taken is 33 seconds. There could be other combinations also, but overall time does not go below 33 seconds.

'''
import heapq

T = int(input())
for T1 in range(T):
    n = int(input())
    candies = list(map(int, input().split()))
    heapq.heapify(candies)
    sume = 0

    while len(candies) > 1:
        a = heapq.heappop(candies)
        b = heapq.heappop(candies)
        sume += a + b
        heapq.heappush(candies, a + b)
    print(sume)


