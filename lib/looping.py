#!/usr/bin/env python3

def happy_new_year():
    """Counts down from 10 to 1 and prints 'Happy New Year!'."""
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")


def square_integers(int_list):
    """Returns a list with each integer squared."""
    return [x ** 2 for x in int_list]


def fizzbuzz():
    """
    Prints numbers from 1 to 100.
    - Multiples of 3 → 'Fizz'
    - Multiples of 5 → 'Buzz'
    - Multiples of 3 and 5 → 'FizzBuzz'
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
