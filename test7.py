# list = [1,2,3,4,5,6,2,3,5,1]
# 뭐는 짝수입니다.
# 뭐는 홀수입니다.
# 30 분에 카톡에 올려요
from functools import reduce


list1 = [1,2,3,4,5,6,2,3,5,1]
# for el in list1:
#     if el % 2 == 0:
#         print(f"{el} 은 짝수 입니다")
#     elif el % 2==1:
#         print(f"{el} 은 홀수 입니다")
# i = 0
# while i<len(list1):
#     #list1[0] = 1, i = 0 
    
#     if list1[i] % 2 == 0:
#         print(f"{list1[i]} 은 짝수 입니다")
#     elif list1[i] % 2 == 1:
#         print(i)
#         # print(f"{list1[i]} 은 홀수 입니다")
#         continue # 반복문의 continue 뒤 실행 x
#         # break 반복문이 끝남 
#     i+=1
    # print(f"-----{list1[i]} -------")
# 2개?
# match case
# java switch case 
# list1 = [1,2,3,4,5,6,2,3,5,1]
# for el in list1:
#     match el % 2:
#         case 1:
#             print(f"{el} 은 홀수 입니다")
#         case 0: 
#             print(f"{el} 은 짝수 입니다")
    # if el % 2 == 0:
    #     print(f"{el} 은 짝수 입니다")
    # elif el % 2 == 1:
    #     print(f"{el} 은 홀수 입니다")

# 람다 버전 3.6 부터 
# 예제) list1 의 요소를 *2 해서 찍어봐라 




# list3 =[]
# for el in range(0, len(list1)):
#     list3.append(list1[el] * 2)
# print(list3)
# list1 = [1,2,3,4,5,6,2,3,5,1]
# list2 = []
# for el in list1:
#     list2.append(el * 2)
# print(list2)
# # map 은 새로운 리스트를 만든다 (반환한다)
# list4 = list(map(lambda el: el ** 2, list1))
# print(list4)


# tmpd = {"name":"re", "age":100}
# list5 = [tmpd,tmpd,tmpd]
# list6 = list(map(lambda el: el.copy(), list5)) 
# # [tmpd.copy(),tmpd.copy(),tmpd.copy()]
# list7 = list5.copy() # [tmpd,tmpd,tmpd]
# print(list5)
# print(list6)
# print(list7)
# list5.append(1)
# print()
# print(list5)
# print(list6)
# print(list7)
# tmpd["age"] = 10
# print()
# print(list5)
# print(list6)
# print(list7)

#list1 요소의 합 ? int (수)
# list1 = [1,2,3,4,5,6,2,3,5,1]
# sum = 0
# for el in list1:
#     sum = sum + el
#     # sum += el
# print(sum)

# sum2 = reduce(lambda x,y: x + y, list1)
# # 합계 구할때
# print(sum2)

# 2시에 하나 더하고 복습하죠
list1 = [1,2,3,4,5,6,2,3,5,1]
# 4이상 것 만 리스트를 만들려고 함 
# 영어로 
# 파이썬 이란 언어로 번역
list0 = []
# 리스트를 만드려고 하니까 리스트를 선언함 
# for el in list1:
#     # print(el)
#     # 만약에 4이상 것 만 (조건)
#     if el >= 4:
#         list0.append(el)
# print(list0)

list01 = list(filter(lambda x: x >=4, list1))
print(list01)


