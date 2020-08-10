'''Game of Marbles
Darrell and Sally are two best friends. They had a large collection of marbles. They devised a game with it to play in their free time which will also help them to improve their math. One of them will have to select a certain number of marbles and give a hint to find the number. The other will have to guess the first number that matches the given criteria and vice versa.

Your task is to act as a judge for this game. When the player finds the answer, you will have to verify the answer. If answer is right, add 10 points to that player. If the player passes the question, you will have to give the right answer (no change in points in this case). You should also announce the winner at the end of the game.

Hint to find the number:

When the marbles are put into a group of x1, x2, x3,…(where x1, x2, x3 can be any number from 1 to 100), it falls into a perfect group.(No marble is left without a group).

Example: When Darrell says the number falls into a perfect set when she groups them into sets of 3 and 5, the answer could be 15 or 30 and so on. Since the first number that matches the criteria is 15, 15 will be the answer.

Explanation: when 15 marbles is put into groups of 3, We will get 5 sets of 3 marbles each and when it is put into groups of 5, we will get 3 sets of 5 marbles each. For 16 marbles, we will get 5 sets of 3 marbles each and one marble will be left without a proper group. So 16 cannot be the answer.

game_of_marbles

Input Format
The input will contain:

Number of input lines N adhering to the following specification

Lines will be of two types either a Question Posing line or Answer Giving line
Question posing line has to appear before any answer giving line
Question Posing line starts with Player Name and Answer Giving line starts with A
Second line will be a Question posing line whose format is where Perfect Sets are depicted in the format <X1,X2,...Xn> where 2<= n <=7 and 1<=Xn<=100

Third line must be an Answer Giving line which is the answer to the preceding Question Posing line. The format of the Answer Giving line is as follows:

answer above can only be an integer number OR it will be a constant string PASS
An integer number represents the value of the answer given by the Player
If the Player does not know the answer she will PASS the question
Fourth line onwards, if they exist, will be alternating series of Question Posing and Answer Giving lines in case of Valid inputs

In case of any Invalid Question Posing line, requisite output must be printed for all previous Valid Question posing line(s).

Processing should stop at Invalid input line after printing required message in output. See output specifications and sample test cases to understand points 5) and 6) better

Output Format
First line of output must reiterate the question in the following format < Player Name >'s question is : X1,X2,X3...,Xn>
Second line should be an evaluation of the first Answer Giving line of the input. The evaluation message will either be {Correct Answer or Incorrect Answer}
If the answer
is correct, output: 10points
is incorrect, output: 0points
is “PASS”-ed by the player,
output Question is PASSed
output Answer is: where correct_answer_value is the correct answer for the question passed by the player.
output: 0points
Overall points collected by players have to be tracked and output when all valid inputs are processed
If all inputs are valid, after processing all the inputs, the final output should be comprised of the following 4 lines
Output Total Points: on fourth last line
Output : points on 3rd last line, where Player1 is the one who first posed the question
Output : points on 2nd last line, where Player2 is the one who first answered the question
If there is a winner Output Game Result: is winner or Game Result: Draw
Print Invalid Input in case of invalid input or failing constraint
Constraints
0 < N <= 10
Player Names are Case-sensitive
Number of inputs in a Question posing line will be 2<=n<=7 and 1<=Xn<=100
<X1 ,X2,X3...,Xn> can only be integers
Sample Input / Output
Input

4
Sally 3,5
A Darrell 15
Darrell 4,8
A Sally 8
Output

Sally's question is: 3,5
Correct Answer
Darrell: 10points
Darrell's question is: 4,8
Correct Answer
Sally: 10points
Total Points:
Sally: 10points
Darrell: 10points
Game Result: Draw
Input

4
Darrell 5,6
A Sally 30
Sally 3,5
A Darrell PASS
Output

Darrell's question is: 5,6
Correct Answer
Sally: 10points
Sally's question is: 3,5
Question is PASSed
Answer is: 15
Darrell: 0points
Total Points:
Darrell: 0points
Sally: 10points
Game Result: Sally is winner
Input

2
Darrell
A Sally 15
Output

Invalid Input
Input

4
Sally 3,5
A Darrell 15
Darrell
A Sally 15
Output

Sally's question is: 3,5
Correct Answer
Darrell: 10points
Invalid Input
Input

2
Sally 3,5
A Darrell 3
Output

Sally's question is: 3,5
Incorrect Answer
Darrell: 0points
Total Points:
Sally: 0points
Darrell: 0points
Game Result: Draw
Input

2
Sally 3,5,15
A Darrell
Output

Sally's question is: 3,5,15
Correct Answer
Darrell: 10points
Total Points:
Sally: 0points
Darrell: 10points
Game Result: Darrell is winner
'''

print(math.gcd(2,4))



def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


# nums must have atleast 2 integers
def lcm(nums):
    assert len(nums) >= 2
    a, b, *rest = nums
    if len(nums) == 2:
        return (a * b) // gcd(a, b)
    return lcm([lcm([a, b])] + rest)


def play_game_turn():
    try:
        asked_by, questionstr = input().strip().split()
        question = questionstr.strip().split(",")

        # if one of the inputs isn't an int, an exception will be thrown here
        question = list(map(int, question))
        assert 2 <= len(question) <= 7
        assert all([1 <= n <= 100 for n in question])

        # find correct answer
        correct_answer = lcm(question)

        # parse "answer input line"
        _, answered_by, answer = input().strip().split()
        answer = answer.strip()

        assert asked_by != answered_by

        apoints = 0

        print(f"{asked_by}'s question is : {questionstr}")

        if answer == "PASS":
            print("Question is PASSed")
            print(f"Answer is: {correct_answer}")
            print(f"{answered_by}: 0points")
        else:
            answer = int(answer)
            if answer == correct_answer:
                print("Correct Answer")
                print(f"{answered_by}: 10points")
                apoints = 10
            else:
                print("Incorrect Answer")
                print(f"{answered_by}: 0points")

        return asked_by, answered_by, apoints

    except:
        raise Exception("Invalid Input Error")


if __name__ == "__main__":
    n = int(input()) // 2
    try:
        assert 0 < n <= 10

        first_question_asked_by = None
        POINTS = {"Darrell": 0, "Sally": 0}
        for _ in range(n):
            asked_by, answered_by, points = play_game_turn()
            POINTS[answered_by] += points

            if not first_question_asked_by:
                first_question_asked_by = asked_by

        # game ends, with all valid inputs

        print("Total Points:")

        if first_question_asked_by == "Sally":
            print(f"Sally: {POINTS['Sally']}points")
            print(f"Darrell: {POINTS['Darrell']}points")
        else:
            print(f"Darrell: {POINTS['Darrell']}points")
            print(f"Sally: {POINTS['Sally']}points")

        if POINTS["Sally"] == POINTS["Darrell"]:
            print(f"Game Result: Draw")
        elif POINTS["Sally"] < POINTS["Darrell"]:
            print(f"Game Result: Darrell is winner")
        elif POINTS["Sally"] > POINTS["Darrell"]:
            print(f"Game Result: Sally is winner")

    except:
        print("Invalid Input")