'''
Simple Chessboard
Write a program that prints a simple chessboard.

Input format:
The first line contains the number of inputs T.
The lines after that contain a different values for size of the chessboard
Output format:
Print a chessboard of dimensions size * size. Print a Print W for white spaces and B for black spaces.

Input:
2
3
5

Output:
WBW
BWB
WBW
WBWBW
BWBWB
WBWBW
BWBWB
WBWBW
'''
T=int(input())
for T1 in range(T):
    n=int(input())
    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                print("W",end="")
            else:
                print("B",end="")
        print("")