#문제 설명
#정수 num이 짝수일 경우 
# "Even"을 반환하고 
# 홀수인 경우 
# "Odd"를 반환하는 함수, 
# solution을 완성해주세요.
# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.
# num = 3 -> "ODD"
# num = 4 -> "EVEN"
# 28분
# def solution(num):
#     answer = ''
#     return answer

# print(solution(3)) # ODD
# print(solution(4)) # EVEN
# def sum(a,b):
#     return a+b # "5" + "5"
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))

# def sum(a,b):
#     if a =="짝수":
#         return # return 한순간 끝
#     print("sum after")
#     for i in range(0,9):
#         print(i)
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))

# 형변환
def sum(a,b):
    # a = "5" , b = "5"
    try:
        if type(a) == int and type(b) == int:
            return a + b # return 한순간 끝
        else :
            return int(a) + int(b)
    except:
        return f"{a}랑 {b} 중 숫자가 아닌게 있습니다."
        
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))
# while True:
#     a = input("입력하세요")
#     if a =="end":
#         break
#     b = input("입력하세요")
#     if b =="end":
#         break
#     print(sum(a,b))

# for i in range(0, 10):
#     a = input("입력하세요")
#     if a =="end":
#         break
#     b = input("입력하세요")
#     if b =="end":
#         break
#     print(sum(a,b))

# 3,6,9 게임
# 들어온 숫자 에 3,6,9 
# c 
# 계속 지속되어야하는 게임
# 369369 현재 {i}
# 입력 다음 할 것

# hint : 함수 , 지역변수 전역변수, 코딩테스트
# 형변환, input, while, for 

# 3시 10분 
# def gama():
#     i = 0
#     while True:
#         i += 1
#         myInput = input(f"현재 값 {i} ") # "2" "c"
#         answer = str(i + 1) #2 "2"
#         for c in str(i + 1):
#             if c=="3" or c=="6" or c=="9":
#                 answer = "c"
#         if myInput == answer:
#             print("맞았다")
#         else: 
#             print("game over")
#             break

# gama()


# def gama(cur, myInput):
#     answer = str(cur) #2 "2"
#     ccc = ""
#     for c in str(cur):#3
#         if c=="3" or c=="6" or c=="9":
#             ccc += "c"
#     if myInput == answer or myInput == ccc:
#         print("맞았다")
#         return True
#     else: 
#         print("game over")
#         return False
# i = 0
# while True:
#     i += 1
#     myInput = input(f"현재 값 {i} ")
#     isWin = gama(i+1,myInput)
#     if(not isWin):
#         break

# def solution(phone_number):
#     # 01033334444
#     answer = ''
#     for i in range(0,len(phone_number)):
#         if i < len(phone_number) - 4: #i=7, 7<7
#             if phone_number[i] == "-" :
#                 answer += "-"
#             else:
#                 answer += "*"
#         else :
#             answer += phone_number[i]
#     return answer
# phone_number = input("번호 000-0000-0000")
# print(solution(phone_number)) # = "*******4444"
# print(solution("027778888")) # = "*****8888"
# 뒤 4자리만 빼고 다 *
# input 번호받아서 010-2222-2222
# 뒷 4자리 만 살리고 ***-****-2222
# 02-7777-8888 **-****-8888


# 파일 입출력
# 상대 경로(내 위치에서 -> 하고 싶은 곳)
# . 현재위치 c/test
# .. c
# . 현재위치 c/test/test1
# ../test12.py
# 절대 경로 
# C:/test/test2/test.py
# f = open("")
# 서버는 linux 
# window c:/
print("실행")
# 관규 
# C:/test/test2/test.py 
# 실행하고 
# C:/test/test.py 
# 준선 
# C:/project/test2/test.py 
# 실행하고
# C:/project/test.py

# 프로젝트 있는 폴더 C:/test/ C:/project/
# 관규 
# python test.py 
# 실행하고 
# python ../test.py 
# 준선 
# python test.py 
# 실행하고
# python ../test.py
hi ="hi"
# \t TAB   
f = open("./test.txt",'w') # . = c/test/test2
f.write("""hi


	bye""")
f.close()

f = open("./test.txt",'a') # . = c/test/test2
f.write("""
    sdfasfdsafdsa""")
f.close()

# git clone https://git.com/배승준/python 

# f = open("./input.py",'r')
# lines = f.readlines()
# for line in lines : 
#     print(line)
# f.close()

# 파일 입출력 읽기 쓰기 추가

# f = open("./test.txt",'w') # . = c/test/test2
# f.write("""hi


# 	bye""")
# f.close()

# f = open("./test.txt",'a') # . = c/test/test2
# f.write("""
#     sdfasfdsafdsa""")
# f.close()

# 내일 업데이트, class 











































