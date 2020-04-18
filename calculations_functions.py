import math


def rectangle(a, b):
    """rectangle area"""
    return a * b


def square(a):
    """square area"""
    return a * a


def triangle(a, h):
    """triangle area"""
    return (a * h) / 2


def trapezoid(a, b, h):
    """trapezoid area"""
    return (a + b) / 2 * h


def circle(r):
    """circle area"""
    return round(math.pi * pow(r, 2), 2) # two decimal places

