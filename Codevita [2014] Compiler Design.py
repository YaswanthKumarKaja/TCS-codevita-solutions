'''Compiler Design - Limit the Method Instructions
Raj is a newbie to the programming and while learning the programming language he came to know the following rules:

Each program must start with { and end with }.
Each program must contain only one main function. Main function must start with < and end with >.
A program may or may not contain user defined function(s). There is no limitation on the number of user defined functions in the program. User defined function must start with ( and end with ).
Loops are allowed only inside the functions (this function can be either main function or user defined function(s)). Every loop must start with { and end with }.
User defined function(s) are not allowed to be defined inside main function or other user defined function(s).
Nested loops are allowed.
Instructions can be anywhere inside the program.
Number of instructions inside any user defined function must not be more than 100.
If any of the above conditions is not satisfied, then the program will generate compilation errors. Today Raj has written a few programs, but he is not sure about the correctness of the programs. Your task is to help him to find out whether his program will compile without any errors or not.

Input Format:
First line starts with T, number of test cases.
Each test case will contain a single line L, where L is a program written by Raj.

Output Format:
Print No Compilation Errors if there are no compilation errors, else print Compilation Errors.

Constraints:
1<=T<=100

L is a text and can be composed of any of the characters {, }, (, ), <, >and P, where P will represents the instruction.

L, comprised of characters mentioned above should be single spaced delimited.
Number of characters in the text, |L| < = 10000

Sample Input and Output
Input

3
{ < > ( P ) }
{ < { } > ( { } ) )
{ ( { } ) }
Output

No Compilation Errors
Compilation Errors
Compilation Errors

'''


t = int(input())
try:
    assert 1 <= t <= 100
    while (t):
        isDone = True
        program = input()
        # print(len(program))
        assert len(program) <= 10000
        stack = []
        # if(program.count('{')!=program.count('}') and program.count('<')!=program.count('>')and program.count('(')!=program.count(')')):
        # print('Compilation Errors')
        # isDone=False
        if (program[0] != '{' or program[len(program) - 2] != '}'):
            # print(program[0],program[len(program)-2])
            print('Compilation Errors')
            isDone = False
        elif (program.count('<') != 1 and program.count('>') != 1):
            print('Compilation Errors')
            isDone = False
        else:
            pp = []
            program = program[1:len(program) - 1]
            for i in program:
                if i == ' ':
                    continue
                if i == '<':
                    if '(' not in stack and '{' not in stack:
                        stack.append(i)
                    else:
                        isDone = False
                        print('Compilation Errors')
                        break

                if i == '{':
                    if '<' in stack or '(' in stack:
                        stack.append(i)
                if i == '(':
                    count = 0
                    if '<' not in stack and '(' not in stack:
                        stack.append(i)
                    else:
                        isDone = False
                        print('Compilation Errors')
                        break
                if i == 'P':
                    if '(' in stack:
                        count += 1
                        if (count > 100):
                            print('Compilation Errors')
                            isDone = False
                            break
                if i in '>':
                    if (len(stack) < 1):
                        break
                    else:
                        top = stack.pop()
                        if (top != '<'):
                            print('Compilation Errors')
                            isDone = False
                            break
                if i in ')':
                    if (len(stack) < 1):
                        break
                    else:
                        top = stack.pop()
                        if (top != '('):
                            print('Compilation Errors')
                            isDone = False
                            break
                if i in '}':
                    if (len(stack) < 1):
                        break
                    else:
                        top = stack.pop()
                        if (top != '{'):
                            print('Compilation Errors')
                            isDone = False
                            break
        if isDone and len(stack) < 1:
            print('No Compilation Errors')
        t -= 1
except:
    raise error
    print('Compilation Errors1')