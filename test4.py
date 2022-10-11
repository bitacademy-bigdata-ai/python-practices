# 문제 1.
print(f"80은 짝수인가 {80%2==0}")
# 문제 2. 주석
list1 =[2,1,5,6,2,40,50,2,5,32] 
list2 =[4,6,2,3,9,10,2,3,42,5,4,63] 
print(set(list1) & set(list2))
union = list(set(list1) & set(list2))
union.sort()
print(union[len(union)-1])



a = 3
b = 0

testBool1 = True
testBool2 = False
testBool3 = a > b
testBool3 = 3 >= 0
testBool3 = 3 == 0
testBool3 = 3 == 0
testBool3 = 3 <= 0
testBool3 = 3 < 0

dict1 = {"name":"park", "age":30}
dict1.get("name") 

list1 = [dict1, 23, "age"]
list1[0] # dict1
len(list1) # 3

set1 = {1,2,1,2}
set1 # {1,2}

tuple1 = (1,2,3,4)

