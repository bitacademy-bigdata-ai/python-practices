# 반복문 
# while for 
# index
# 0 <= i < 3

# for i in range(0,3):
#     print(i)
# # 0 <= i < 3
# list1 = ["a","b","c"]
# for i in range(0,len(list1)):
#     print(list1[i])

# for element in list1:
#     print(element)

# index = 0
# while index < len(list1):
#     print(list1[index])
#     index+=1

# break continue
# list1 = [9,4,2,1,6,7,5,4,3,7]
# 만약에 홀수면 2배 짝수면 그냥의 리스트 만드는 중
# 만약 합이 20 이 넘으면 끝 

# list1 = [9,4,2,1,6,7,5,4,3,7] -> [18,4,2,2,6]

# list1 = [9,4,2,1,6,7,5,4,3,7]
# 만약에 홀수면 2배 짝수면 그냥의 리스트 만드는 중
# 만약 합이 20 이 넘으면 끝 
# list1 = [9,4,2,1,6,7,5,4,3,7]
# list2 = []
# i = 0
# sum1 = 0
# # if sum1 >20 :
# #     break
# while i < len(list1):
#     # i = 0, sum1 = 0, list1[i=0] =9
#     # i = 1, sum1 = 9, list1[i] =4 
#     # i = 2, sum1 = 13, list1[i] =2 
#     # i = 3, sum1 = 15, list1[i] =1
#     # i = 4, sum1 = 16, list1[i] =6 
#     sum1 = sum1 + list1[i]
#     # i = 0, sum1 = 9
#     # i = 1, sum1 = 13
#     # i = 2, sum1 = 15
#     # i = 3, sum1 = 16
#     # i = 4, sum1 = 22
#     if list1[i] % 2 == 1:
#         list2.append(list1[i]*2)
#     else:
#         list2.append(list1[i])   
#     i+=1
#     # i = 1, sum1 = 9
#     # i = 2, sum1 = 13
#     # i = 3, sum1 = 15
#     # i = 4, sum1 = 16
#     # i = 5, sum1 = 22
#     if sum1 >20 :
#         continue
#     print("끝 ")
# print(list2)
# list1 = [9,4,2,1,6,7,5,4,3,7] -> [18,4,2,2,6]

list1 = ["안","녕","하","세","요"]
index = 0
hi = ""
# while index < len(list1):
#     # index = 0, hi = ""
#     print(hi)
#     hi += list1[index]
#     # index =0 ,hi ="안"
#     print(hi)
#     index+=1
    # index = 1 ,hi ="안"
# print(hi)
# while 조건이 True인 동안 아래를 실행함 : 
# 0 <= i < len(list1) = 5
# for i in range(0, len(list1),10):
#     hi += list1[i]
# print(hi)
# print(list1[3])
# for element in list1:
#     hi = hi + element

#     # hi = hi + element
# print(hi)    
x = { "isPartTime": True,"company":"카카오"}
for element in x:
    print(x.get(element))
print(x["isPartTime"])

tup = (1,2,3)
for element in tup:
    print(element)

# num = 5
# for element in num:
#     print(element)

st ="안녕하세요"
print(st[0])
for element in st:
    print(element)




