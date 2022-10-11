print("Q3. ")
list = [
{"name":"kim","money":50000},
{"name":"park","money":30000}
]
print("%s는 %s보다 %d 있습니다."
%(list[0].get("name"),
list[1].get("name"),
(list[0].get("money")-list[1].get("money"))))
print("%s는 %s보다 %d 있습니다."
%(list[1].get("name"),
list[0].get("name"),
(list[1].get("money")-list[0].get("money"))))