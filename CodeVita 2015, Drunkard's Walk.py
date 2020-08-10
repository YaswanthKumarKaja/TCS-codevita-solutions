'''Drunkard’s Walk
In state of inebriation, a drunkard sets out to walk home, afoot. As is common knowledge, a drunkard struggles to find balance and ends up taking random steps. Not surprisingly these are steps in both forward as well as backward direction. Funnily enough, these are also repeated movements. Now, it so happens that on this drunkard’s path, there are two banana skins - one in forward direction and one in backward direction. There is a real danger that the drunkard’s downfall may be accelerated if he accidentally slips over either of those banana skins.

Your task is to find out if he will slip over the banana skin on forward path or banana skin on backward path and in how much time. It is also possible that by his good fortune he might not step over either banana skins. Write a program to calculate the outcome.

Input Format
First line contains total number of test cases, denoted by N
Next N lines, contain a tuple containing 6 values delimited by space
D FM BM T FBS BBS, where

D denotes direction, either F (Forward) or B (Backward)
FM denotes the magnitude of forward movement in meters
BM denotes the magnitude of backward movement in meters
T denotes time taken to cover 1 meter
FBS denotes distance from Drunkards’ starting position and the banana skin in forward direction
BBS denotes distance from Drunkards’ starting position and the banana skin in backward direction
Output Format
For each test case, print time taken by the Drunkard to slip over the forward or backward banana skin. Print F if he slips over forward banana skin and B if he slips over the backward banana skin. Both the outputs must be delimited by whitespace

OR

Print Hurray if the Drunkard is lucky to not slip over either banana skin

Constraints
1 <= N <= 100
forward movement (FM) > 0
backward movement (BM) > 0
time (T) > 0
Distance to banana skin in forward direction (FBS) > 0
Distance to banana skin in backward direction (BBS) > 0
All input values must be integer only
Sample Input / Output
Input

6
B 14 12 7 25 4
B 11 4 6 10 17
F 2 3 9 12 15
F 1 12 3 22 28
B 8 8 5 9 18
F 8 8 5 7 9

Output

28 B
156 F
675 B
102 B
Hurray
35 F'''
T = int(input())
for T1 in range(T):
    d, f, b, t, fbs, bbs = input().split()
    f = int(f);
    b = int(b);
    t = int(t);
    fbs = int(fbs);
    bbs = int(bbs)
    if d.upper() == "F" and f < fbs and f == b:
        print("Hurray")
    elif d.upper() == "B" and b < bbs and f == b:
        print("Hurray")
    elif d.upper() == "F" and f > fbs:
        print(fbs * t, "F")
    elif d.upper() == "B" and b > bbs:
        print(bbs * t, "B")
    elif d.upper() == "F" and b - f > bbs:
        print((2 * f + bbs) * t, "B")
    elif d.upper() == "B" and f - b > fbs:
        print((2 * b + fbs) * t, "F")
    elif f - b > 0:
        time = 0
        if d.upper() == "B":
            time += b * t
            fbs += b
        displacemnt = f - b
        distance = f + b
        tobemod = fbs - f
        if tobemod % displacemnt == 0:
            time += (tobemod // displacemnt) * distance * t + f * t
            print(time, "F")
        else:
            time += (tobemod // displacemnt) * distance * t + distance * t
            finaldistance = fbs - (tobemod // displacemnt) * displacemnt - displacemnt
            time += finaldistance * t
            print(time, "F")
    elif b - f > 0:
        time = 0
        if d.upper() == "F":
            bbs += f
            time += f * t
        displacemnt = b - f
        distance = b + f
        tobemod = bbs - b
        if tobemod % displacemnt == 0:
            time += (tobemod // displacemnt) * distance * t + b * t
            print(time, "B")
        else:
            time += (tobemod // displacemnt) * distance * t + distance * t
            finaldistance = bbs - (tobemod // displacemnt) * displacemnt - displacemnt
            time += finaldistance * t
            print(time, "B")



