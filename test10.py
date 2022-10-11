# 2부터 20까지 짝수의 합 
# 10분에 카톡
# 코딩테스트 난이도 0 
# i = 2
# answer = 0
# while i<=20:
#     # if i%2 ==0:
#     answer +=i
#     i+=2
# print(answer)
# answer = 0
# for index in range(2, 21,2):
#     # if index%2 ==0:
#     answer +=index
# print(answer)

# 코딩테스트 난이도 1
# 남은 시간에 깃허브 한번해보고
# 2 부터 30 까지 소수 리스트 뽑아내기 
# 30분까지
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# 구구단 
# 2*1 =2 2*2 =4
# num = 2
# for i in range(2,10) :
#     for num in range(1,10):
#         print(f"{i} * {num} = {num*i}")


# 별 찍기
# *
# **
# ***
# ****
# *****


# text = "*"
# for i in range(2,7):
#     st =""
#     for j in range(1, i):
#         st = text*j
#     print(st)

# 2 부터 30 까지 소수(1과 자신) 리스트 뽑아내기 
# 30분까지
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
answer = []
for i in range(2,31):
    # i=4
    isPrimary = True # 소수인가?
    for j in range(2, i):# i=2 2<=2<2
        if i%j ==0: # 5%2 ==3 ,5%3 ==2 ,5%4 ==1  
            isPrimary =False
            break
    if isPrimary: 
        answer.append(i)

print(answer)






























