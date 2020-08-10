'''Number Game
Aman and Jasbir are very intelligent guys of their batch. Today they are playing a game “Game of Numbers”.

Description of game:

There are N numbers placed on a table.
Since two players are playing the game, they will make their moves alternatively.
In one move a player can perform the following operation.
A player will choose a number from the table and will replace that number with one of its divisor. For example, 6 can be replaced with 1, 2, or 3 (since these are the divisors of 6). Similarly, 12 can be replaced with 1, 2, 3, 4 or 6.
It is mandatory that the player has to replace the number.
A player cannot put back the same number on table.
As 1 does not have any divisor other than itself, a player cannot replace 1 with any other number. So soon a situation will arise when there will be only all 1s on the table. In that situation the player will not be able to make any move. The player who will not be able to make the move, loses.
Both the players are masters of this game. So they will play the game optimally.
Aman will make the first move of the game.
You will be given N integers that are on the table. You have to predict, who will win the game - Aman or Jasbir.

Input Format
First line contains information about the numbers present of the table, denoted by N
Second line contains N integers delimited by space - A1 A2 A3 A4 ...... AN

Output Format
Print the name of the player who will win the game in upper case i.e. AMAN or JASBIR.

Constraints:
1 <= N <= 100000
0 < Ai <= 10000

A player cannot replace more than 1 number in one move
Players move alternate and a player cannot pass or make no move.
A number cannot be replaced itself, i.e. 6 can be replaced with 1, 2 or 3 only , not with 6
Aman always makes the first move
Sample Input / Output
Input

1
6

Output

AMAN

Input

2
18 6

Output

AMAN

Input

4
24 45 45 24

Output

JASBIR'''


def isprime(n):
    if n == 1:
        return 0
    if n == 2 or n == 3 or n == 5:
        return 1
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return 0
    if n % 6 == 1 or n % 6 == 5:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 0
            elif i == int(n ** 0.5):
                return 1
    else:
        return 0


n = int(input())
a = list(map(int, input().split()))
prili = []
for i in range(2, max(a) + 1):
    if isprime(i) == 1:
        prili.append(i)
for i in range(n):
    temp = a[i]
    k = 0
    save = 0
    while (temp > 1):
        if temp % prili[k] == 0:
            save += 1
            temp //= prili[k]
        else:
            k += 1
    a[i] = save
res = a[0]
for i in range(1, len(a)):
    res ^= a[i]
if res == 0:
    print("JASBIR")
else:
    print("AMAN")
