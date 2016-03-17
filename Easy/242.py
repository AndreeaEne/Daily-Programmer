"""
Scientist have discovered a new plant. The fruit of the plant can feed 1 person for a whole week and best of all, the plant never dies. Fruits needs 1 week to grow, so each weak you can harvest it fruits. Also the plant gives 1 fruit more than the week before and to get more plants you need to plant a fruit.
Now you need to calculate after how many weeks, you can support a group of x people, given y fruits to start with.
Input
15 1
Output
5
"""

from sys import argv

x = int(argv[1])
y = int(argv[2])

def fun_plant(people, fruits):
    # Initially 0 fruits that have been harvested
    fruits_in_harvest = 0

    # Week counter starts from 1
    week = 1

    # Make sure that the harvested number isn't more than
    # we actually need. (number of people)
    while (fruits_in_harvest < people):
        fruits += fruits_in_harvest
        fruits_in_harvest += fruits
        week += 1
    return week


print(fun_plant(x, y))
