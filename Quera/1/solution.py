import math


def square(x):
    return x ** 2


def circle(r):
    return math.pi * (r ** 2)


def rectangle(x, y):
    return x * y


def triangle(x, h):
    return (x * h) / 2


all_functions = {"square": square, "circle": circle, "rectangle": rectangle, "triangle": triangle}


def get_func(ls):
    results = []
    for function in ls:
        results.append(all_functions.get(function))
    return results
