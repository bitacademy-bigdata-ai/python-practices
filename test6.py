# 반복문 
a = ["a","b","c","d","e"]
# i = 0,1
# 0 <= i < len(a)
for i in range(0, 5, 2) :
    print(i)
    print(a[i])   
# foreach 
for i in a:
    print(i)
re = 0
while re < 5:
# re = 4
    print(a[re])
    re+=1 # re = re(0) + 1 = 1 

b = [1,2,3,4,5]
re = 0
while True:
    print(b[re])
    if(b[re] % 2 ==0):
        break # 반복 중지
    re+=1
for i in a:
    if i=="c":
        break
    print(i)








