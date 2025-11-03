# Grade Calculator:

"""
Write a program that calculates and displays the letter grade
for a given numerical store (e.g.. A, B, C, D or F)
based on the following grading scale
A : 90-100
B : 80-89
C : 70-79
D : 60-79
F : 0-59
"""
Score = int(input('Enter the score:'))

if Score > 100 or Score <= -1:
    print('Invalid score! Please enter a value between 0 and 100')
else:

    if 90 <= Score <= 100:
        print('A grade')

    elif 80 <= Score <= 89:
        print ('B grade')

    elif 70 <= Score <= 79:
        print('C grade')

    elif 60 <= Score <= 69:
        print('D grade')

    else:
        print('E grade')

