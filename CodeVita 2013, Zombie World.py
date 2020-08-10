'''Zombie World
One day Bob is playing Zombie World video game. In Zombie World game each round will contain N zombie’s and each zombie’s energy is Zi (where 1 <= i <= N).

Bob will start the round with B energy. In order to move to the next level Bob need to kill all the N zombie’s but Bob can select any one among N Zombies. If energy of Bob (B) is less than Zombie energy (Zi) then Bob will die and lose the round else Bob will won, during the fighting with zombie, Bob will lose his energy by ( Zi % 2 ) + ( Zi / 2 ). At any point of game Bob will play optimally. Now your task is to find out whether Bob can reach to the next level or not.

Input Format
First line will contains B and N, separated by space, where B is the energy of Bob and N is the number of Zombie. Next line will contain N spaced integers each will represent the energy of zombie.

Line 1: B N, where B is the energy of Bob and N is the number of Zombie
Line 2: Zi, where Zi is a list containing energy of zombies separated by space

Constraints
1 <= N  <= 10^4
1 <= B  <= 10^9
1 <= Zi <= 10^5
Note: for this problem all the divisions are integer divisions.

Output Format:
Print YES or NO depending upon whether Bob can reach the next level or not.

For Valid Input,print

YES Or NO

For Invalid Input,print

Invalid Input

Sample Input / Output
Input

35 3

5 9 6
Output

YES
Input

456 68

a
Output

Invalid Input
Input

4 4

1 3 2 4
Output

NO'''
try:
    b,n=input().split()
    b=int(b);n=int(n)
    a=list(map(int,input().split()))
    a.sort()
    sume=0
    for i in a:
        sume+=(i%2)+(i/2)
    if b>sume:
        print("YES")
    else:
        print("NO")
except:
    print("Invalid Input")
