# 한 줄 짜리 주석
"""
코드 작성일
코드 작성자
코드 이름
코드 목적
"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


def gugudan(x):
    for i in range(9):
        print(x * (1 + i))
