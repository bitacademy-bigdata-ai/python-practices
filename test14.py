# 계산기를 만들거야
# 기본적으로

# def add(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# i = 0
# i = add(i, 10)
# i = diff(i, 5)
# print(i)
# j = 0
# j = add(j, 10)
# j = diff(j, 5)
# print(j)
# class 



# class Calculator:
#     def __init__(self) -> None:
#         self.result = 0

#     def add(self, b):
#         self.result += b

#     def diff(self, b):
#         self.result -= b







# 모듈 
from animal import Animal
from arm import Arm
from cal import Calculator
from cat import Cat
from dog import Dog
from human import Human
from leg import Leg
from user import User
# 클래스는 하나의 물체를 만들기위해 쓰고 
# 상속 공통 코드를 줄이기위해서 
# cal1 = Calculator()
# cal1.add(10)
# cal1.diff(5)
# print(f"cal1\t{cal1.result}")

# cal2 = Calculator()
# cal2.add(10)
# cal2.diff(2)
# print(f"cal2\t{cal2.result}")

# cal3 = Calculator()
# cal3.add(10)
# cal3.diff(2)
# print(f"cal3\t{cal3.result}")

# user1 = User("bit", "1234")
# user1.printUser()
# user1.change_id("pppp")
# user1.printUser()

# l = Leg("left","park")
# print(l.side)
# print(l.name)
# # l.name = "ffff"
# l.setName("kim")
# print(l.name)


# an = Animal()
# print(an.name)
# an.__setattr__("name", "?")
# print(an.__dict__)
# 부모꺼 가져다 쓸 수 있음

# cat = Cat()
# cat.printSound()
# print(cat.name)
# print(cat.master)

dog = Dog()

dog.printSound()
print(dog.type)
print(dog.master)

print(dog.__dict__) 
#{
# 'type': '강아지',
#  'sound': ' 멍멍',
#  'master': True
# } = Dog
# 객체 
# 객체 지향  자바에서 더 자세히 
# 절차 지향 
# human = 
# {
# "name":"park",
#  'age': 46,
#  'gender': '남자'
# }








