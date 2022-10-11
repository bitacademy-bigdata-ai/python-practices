# main 
# main 내가 실행시킬 것 
# java는 무조건 main start

# package 묶음 
from calc import Calc
from calculator.add import add
from calculator.diff import diff
from person import Person
from test4.input import testInput
from user.age import showAge
from user.name import showName
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
def solution(n:int):
    answer = 1
    first = 0
    second = 1
    # answer= first + second
    # F(2) = F(0) + F(1) = 0 + 1 = 1
    for i in range(2,n+1): # 2<= i <5+1
        answer= first + second 
        # F(2) = F(0) + F(1)
        # F(3) = F(1) + F(2)
        first = second
        second = answer
    return answer % 1234567

# def main():
#     # count = 0
#     # count = add(count,4) # 4
#     # count = diff(count, 10) # -6
#     # print(count) # -6
#     # text = testInput()
#     # print(text)
#     # a=Person() 
#     # # Person.count +=1 count = 1
#     # # self.count +=1 count = 2
#     # b=Person()
#     # # Person.count +=1 count = 2
#     # # self.count +=1 count = 3
#     # c=Person()
#     # # Person.count +=1 count = 1
#     # # self.count +=1 count = 2
#     # print(c.count)
#     # c.printCount()
#     # c.printCount2()
#     # print(b.count)


def main():
    print(solution("1234")) # -> 2
    print(solution(5)) # -> 5

main()
# class animal():
#     def __init__(self) -> None:
#         print('동물')
#         pass
# animal()