print("Q1 . ")
a = [1,1,2,3,4,2,1,4,5,6,7,8,10]
setA = set(a)
print(setA)

print("Q2 . ")
a={"name": "park", "score": 70}
b={"name": "kim" , "score": 80}
c={"name": "park", "score": 50}
print("%s는 점수가 80점 이상이 %s"%(a["name"],a["score"]>=80))
print("%s는 점수가 80점 이상이 %s"%(b["name"],b["score"]>=80))
print("%s는 점수가 80점 이상이 %s"%(c["name"],c["score"]>=80))