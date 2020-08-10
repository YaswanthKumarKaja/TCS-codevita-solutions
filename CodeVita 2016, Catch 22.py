'''Catch 22
A robot is programmed to move forward F meters and backwards again, say B meters, in a straight line. The Robot covers 1 meter in T units of time. On Robot’s path there is a ditch at a distance FD from initial position in forward direction as well as a ditch at a distance BD from initial position in backward direction. This forward and backward movement is performed repeatedly by the Robot.

Your task is to calculate amount of time taken, before the Robot falls in either ditch, if at all it falls in a ditch.

Input Format
First line contains total number of test cases, denoted by N

Next N lines, contain a tuple containing 5 values delimited by space F B T FD BD, where

F denotes forward displacement in meters
B denotes backward displacement in meters
T denotes time taken to cover 1 meter
FD denotes distance from Robot’s starting position and the ditch in forward direction
BD denotes distance from Robot’s starting position and the ditch in backward direction
Output Format
For each test case print time taken by the Robot to fall in the ditch and also state which ditch he falls into. Print F for forward and B for backward. Both the outputs must be delimited by whitespace

OR

Print No Ditch if the Robot does not fall in either ditch

Constraints:
First move will always be in forward direction
1 <= N <= 100000
forward displacement > 0
backward displacement > 0
time > 0
distance of ditch in forward direction (FD) > 0
distance of ditch in backward direction (BD) > 0
All input values must be positive integers only
Sample Input / Output
Input

3
9 4 3 13 10
9 7 1 11 13
4 4 3 8 12

Output

63 F
25 F
No Ditch

Input

5
8 4 7 11 22
4 5 4 25 6
4 9 3 6 29
7 10 6 24 12
10 10 1 9 7

Output

133 F
216 B
231 B
408 B
9 F

'''
def fune(f,b,t,fd,bd):
    if f==b and fd>f:
        print("No Ditch")
        return "No Ditch"
    if f>=fd:
        print(fd*t,"F")
        return fd*t
    if b-f>=bd:
        print((2*f+bd)*t,"B")
        return (2*f+bd)*t
    if f-b>0:
        displacement=f-b
        distance=f+b
        lastbutone=fd-f
        restime=0
        if lastbutone%displacement==0:
            restime+=(lastbutone//displacement)*distance*t+f*t
            print(restime,"F")
            return restime
        else:
            restime+=(lastbutone//displacement)*distance*t+distance*t
            restdistance=fd-(lastbutone//displacement)*displacement-displacement
            restime+=restdistance*t
            print(restime,"F")
            return restime
    else:
        displacement=b-f
        distance=f+b
        bd+=f
        lastbutone=bd-b
        restime=f*t
        if lastbutone%displacement==0:
            restime+=(lastbutone//displacement)*distance*t+b*t
            print(restime,'B')
            return restime
        else:
            restime+=(lastbutone//displacement)*distance*t+distance*t
            restdistance=bd-(lastbutone//displacement)*displacement-displacement
            restime+=restdistance*t
            print(restime,"B")
            #print(displacement, distance,bd,lastbutone, restdistance,restime)
            return restime








T=int(input())
for T1 in range(T):
    f,b,t,fd,bd=input().split()
    f=int(f);b=int(b);t=int(t);fd=int(fd);bd=int(bd)
    fune(f, b, t, fd, bd)

