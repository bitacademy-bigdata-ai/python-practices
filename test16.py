

# 스터디 자기 모르는거 
# 1,2,3,4 (난이도 1)
# 1 자연수 뒤집어 배열로 만들기
# 2 제일 작은 수 제거하기
# 3 두 정수 사이의 합
# 4 정수 제곱근 판별
# 오전 밥먹고 설명 
# 아무나 나와서 2 -> 4 코드 짜는거야
# 4번 코드 개선점이나 배울점 찾아보는거
# 1조 1
#두 정수 사이의 합
import math


def solution(a, b):
    answer = 0
    if b>a:
        # list=list(range(a,b+1))
        # sum(list1)
        return sum(range(a,b+1))
    elif a>b:        
        list1=list(range(b,a+1))
        answer=sum(list1)
    else:
        answer = a
    return answer
# print(solution(10,5))



# 2조 
# a = 123
# [3,2,1]

a = 123 # 백이십삼
# a =  '123'# 일이삼
answer = []
arr = list(str(a))
arr.reverse()
print(arr) # ['3','2','1']     결과로나와야할값[3,2,1]
for i in range(0,len(arr)) : 
    answer.append(int(arr[i]))
# print(answer) #[3,2,1]
    
def sol(a):
    answer =[]
    strA = str(a)
    for i in range(len(strA),0,-1) : 
        answer.append(int(strA[i-1]))
    return answer
# print(sol(123))
# print(sol(12345))



# 3조 3
# 정수 제곱근 판별
#임의의 양의 정수 n에 대해,
#  n이 어떤 양의 정수 x의 제곱인지 
# 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 
# x+1의 제곱을 리턴하고, 
# n이 양의 정수 x의 제곱이 아니라면 
# -1을 리턴하는 함수를 완성하세요.
# n = 121 -> 144
# n = 3 -> -1
 
def solu(n):
    answer = 0
    for i in range(1,n):
        if i * i == n:
            answer = (i+1)*(i+1)
            break
        elif i * i > n: #144> 123
            break
    if answer==0:
        return -1
    return answer
print(solu(12300202))
print(solu(3))



# 정수를 저장한 배열,
#  arr 에서 가장 작은 수를
#  제거한 배열을 리턴하는 함수,
#  solution을 완성해주세요.
#  단, 리턴하려는 배열이 빈 배열인 경우엔 
# 배열에 -1을 채워 리턴하세요. 
# 예를들어 arr이 [4,3,2,1]인 경우는
#  [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 문제 이해 
# list 에서 제일 작은 수 제거하기
# 1개일땐 [-1]
# def solution(arr):
#     answer = []
#     # 1개일땐 [-1]
#     if len(arr)==1:
#         return [-1]
#     #제일 작은 수
#     minNumber = 1000000 #
#     for a in arr:
#         if a < minNumber:
#             minNumber = a
#     # 제거하기
#     for a in arr:
#         if minNumber != a:
#             answer.append(a)
#     return answer

# print(solution([10]))
# print(solution([4,3,2,1]))









