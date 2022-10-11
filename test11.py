# 파이선은 절차 지향 언어
# 자바 OPP
# 함수 
# define 정의
# sum(a,b) -> return
# return 반환 
# sum(a,b) => a,b 매개 변수
# isPrimaryKey = True cammel case
# is_primary_key = True snake case

# def sum(a,b):
#     return a+b
# print(sum(1,2)) # sum(1,2) => 1,2 => 인수
# print(sum(3,5))
# argument 매개변수
# def sum1(*args):
#     print(args)
#     pppp = 0
#     for arg in args:
#         pppp+= arg
#     return pppp
# print(sum1(1,1,1,1,1,1))
# def printFunc(**kwargs):
#     print(kwargs)
# printFunc(a=1, b=1)

# def makeHuman(name, age):
#     return {"name":name, "age":age}
# human1 = makeHuman("kim", 30)
# human2 = makeHuman("park", 34)
# print(human1)
# print(human2)


def isPrimaryNumber(num):
    isPrimary = True # 소수인가?
    for j in range(2, num):# i=2 2<=2<2
        if num%j ==0: # 5%2 ==3 ,5%3 ==2 ,5%4 ==1  
            isPrimary =False
            break
    if isPrimary: 
        return f"{num}은 소수입니다"
    else:
        return f"{num}은 소수가 아닙니다"



def sum1(*args):
    print(args)
    pppp = 0
    for arg in args:
        pppp+= arg
    return pppp
print(sum1(1,1,1))
print(3)
def isPrimaryNumbers(*nums): # nums = (9,4,2,11,16)
    for num in nums:
        isPrimary = True # 소수인가?
        for j in range(2, num):# i=2 2<=j<9
            if num%j ==0: # 5%2 ==3 ,5%3 ==2 ,5%4 ==1  
                isPrimary =False
                break
        if isPrimary: 
            print(f"{num}은 소수입니다") 
        else:
            print(f"{num}은 소수가 아닙니다")
# isPrimaryNumbers(9,4,2,11,16) -> None 
# return 반환 
print(isPrimaryNumbers(9,4,2,11,16))
def ooo(a):
    print(a)

print(ooo("hi"))
# ooo("hi") -> return "hello" 
# a = ooo("hi")
# a = "hello"
# print(a) print("hello") 

name = "park" # 전역 변수
name1 = "lee" # 전역 변수

def setName1(name): # 매개 변수
    print(f"2.{name}") # kim
    # name = name # kim 
    pppp = name # 지역 변수
    print(f"3.{name} {name1}") # 3. kim lee

def setName2(name): # 매개변수
    print(f"2.{name}") # kim
    print(f"3.{pppp} {name1}")

print(f"1. name1 : {name1}") # 1. name1 : 
print(f"1.{name}") # park
setName1("kim") # 인자값
print(f"4.{name}") # park
print(f"2. name1 : {name1}") # 2. name1 : 
# 코딩 테스트 (
# 1. 백준(31%)난이도가 있음
#  2. 프로그래머스(30%)
# )

