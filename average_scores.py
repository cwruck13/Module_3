"""
program: average_scores.py
Author: Cassandra Wruck
Last date modified: June 7th, 2020

This program is meant to calculation an average score for 3 tests. It gets the user's input
such as first and last name, age, and the test scores. It calls a method to calculate told and
prints off the information.
"""

def average():

    #defining start point
    average_scores = 0

    #get input from user for test scores
    score1 = int(input('First test score: '))
    score2 = int(input('Second test score: '))
    score3 = int(input('Third test score: '))

    #calucate average of test scores
    average_scores = (score1 + score2 + score3) / 3

    return average_scores

if __name__ == '__main__':

    #get input from user for name
    first_name = input('What is your first name? : ')
    last_name = input('What is your last name? : ')

    #get input from user for age
    age = input('What is your age? : ')

    #calling a method to return calculation
    average_scores = average()

    #printing information
    print(last_name + "," + first_name + " Age: " + age + " Average Grade: " + str(average_scores))
