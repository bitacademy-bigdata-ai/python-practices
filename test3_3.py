print("Q3. ")
p1 = {"name":"kim", "money": 50000}
p2 = {"name":"park", "money": 30000}
print("%s는 %s보다 %d 있습니다."%(
p1.get("name"),
p2.get("name"),
p1.get("money")-p2.get("money")))

print("%s는 %s보다 %d 있습니다."%(
p2.get("name"),
p1.get("name"),
p2.get("money")-p1.get("money")))

print("%s와 %s의 합 %d 있습니다."%(
p2.get("name"),
p1.get("name"),
p2.get("money")+p1.get("money")))
print("둘의 평균은 %.0f(소수점 제거)입니다"%(
(
(p2.get("money")+p1.get("money"))
)
/2)
)
