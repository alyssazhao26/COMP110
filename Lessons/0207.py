"""Demonstrates Functions"""
from random import randint

x: int = round(10.25)

z: int = randint(1, 7)

def my_max(number1: int,  number2: int) -> int:
    """Returnes the maximum values out two numbers"""
    if number1 >= number2:
        return number1
    else:
        return number2


