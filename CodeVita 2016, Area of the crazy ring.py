'''Area of the Crazy Ring
Scientists have found a strange substance having strange properties. There is one triangular substance called Strange Triangle which has a property that if it is placed inside a circle, then it contracts/shrinks the circle until all the corners of the triangle are touching the circle. There is another circular substance called Strange Circle, which when placed inside any polygon, expands such that it becomes the largest possible circle which can fit inside the polygon such that it touches every side of the polygon.

Now researchers did a strange experiment. They placed a Strange Triangle inside a normal circle and then placed a Strange Circle inside this Strange Triangle. Thus the ring formed by the two circles, the normal outer circle and the inner strange circle is named Crazy Ring. You are provided with the coordinates of the Strange Triangle on coordinate plane and you have to calculate the area of the Crazy Ring formed by the structure, Print “Not Possible” if the ring is not possible to form.

Input Format:
The first line contains k, the number of inputs. The following k lines contain:

First line contains two space delimited numbers N1 M1 (N1 and M1 can also be negative)
Second line contains two space delimited numbers N2 M2 (N2 and M2 can also be negative)
Third line contains two space delimited numbers N3 M3 (N3 and M3 can also be negative)
Where, (N1, M1) , (N2, M2) and (N3, M3) are x and y coordinates of three points representing the Strange Triangle

Output Format:
Output the area of the crazy ring up to 2 decimal places however calculations are to be performed up to a precision of 11 decimal places

OR

Print “Not Possible” if it is not possible to form the ring

Sample Input and Output
Input 1:

3
5 5
5 20
20 5
Output:

292.79
Input 2:

3
5 5
5 5
5 5
Output:

Not Possible
Input 3:

3
5 8
4 3
2 4.34534554521
Output:

17.91
'''
import math

test = int(input())


def distance(x1, x2, y1, y2):
    res = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return res


def incircle(s, a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        return -1
    else:
        area = ((s - a) * (s - b) * (s - c) / s) ** 0.5
        r1 = area

        return r1


def cirum(s, a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        return -1
    else:
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        r0 = (a * b * c) / (4 * area)
        return r0


def solve(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    if (area > 0):
        circircle = (a * b * c) / (4 * area)
    else:
        circircle = 0

    if (s > 0):
        incircle = (((s - a) * (s - b) * (s - c)) / s) ** 0.5
    else:
        incircle = 0
    outarea = (math.pi) * ((circircle) ** 2)
    inarea = (math.pi) * ((incircle) ** 2)
    return outarea - inarea


if (test > 4):
    for i in range(test // 3):
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
        x3, y3 = map(float, input().split())
        a = distance(x1, x2, y1, y2)
        b = distance(x2, x3, y2, y3)
        c = distance(x3, x1, y3, y1)
        if (a < 0 or b < 0 or c < 0):
            print("Not Possible")
        else:
            '''s=a+b+c/2
            r1=incircle(s,a,b,c)
            r0=cirum(s,a,b,c)
            area1=0
            area2=0
            if(r1>0 or r0>0):
                area1=(math.pi)*r1*r1
                area2=(math.pi)*r0*r0
            if(abs(area1-area2)==0.0):
                print("Not possible")
            else:
                print(format(abs(area2-area1),".2f"))'''
            if (solve(a, b, c) > 0.0):
                print(format(solve(a, b, c), ".2f"))
            else:
                print("Not Possible")
        for i in range(test % 3):
            x1, y1 = map(float, input().split())
        if (test % 3 != 0):
            print("Not Possible")



else:
    print("Not Possible")