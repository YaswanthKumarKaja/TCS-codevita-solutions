'''CodeVita 2015, Minimum Distance
Two riders A and B are travelling on a highway towards each other on two roads that intersect at right angle at speeds VA meters/second and VB meters/second. A is at a distance of ‘x’ meters and B is at a distance of ‘y’ meters from the intersection. Calculate the minimum distance between these two riders that is possible.

Approaching Intersection

Input Format:
First line of input will contain number k - the number of inputs.
The following k lines contain:
First line contains the distance of Rider A from intersection denoted by x
Second line contains the distance of Rider B from intersection denoted by y
Third line contains the Velocity of Rider A denoted by VA
Fourth line contains the Velocity of Rider B denoted by VB

Output Format:
Print the minimum distance between these two riders, if minimum distance is nonzero. If minimum distance is zero, print it as 0.0

Print upto 11 decimal places

Example:
Input:
k = 2

x = 100
y = 100
VA = 10
VB = 10

x = 500
y = 300
VA = 20
VB = 14
Output:
0.0
41.18252056395
'''
T=int(input())
for _ in range(T):
    da=int(input())
    db=int(input())
    va=int(input())
    vb=int(input())
    mindist=((da)**2+(db)**2)**0.5
    while(da>0 or db >0):
        da-=va
        db-=vb
        distance=((da)**2+(db)**2)**0.5
        mindist=min(distance,mindist)
    if mindist == 0:
        print("0.0")
    else:
        print("{:.11f}".format(mindist))
