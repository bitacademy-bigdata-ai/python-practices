# 정적 
from typing import overload


class Calc:
    @staticmethod # @ 는 어노테이션
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def diff(s,a):
        print("diff 2개짜리")