from copy import copy  # copy라이브러리 import
print("hello")
# 이건 주석이에요

a = "hobby"
# 원하는값 count함수
print(a.count("b"))
# 원하는 값 find 함수(첫번째로 찾은 값의 인덱스 return), 비슷함 함수로 index함수도 있는데 이건 찾는 값있으면 index리턴 없으면 에러
print(a.find("b"))
# 원하는 문자열 삽입
a = ","
print(a.join('abcd'))  # ==>결과:a,b,c,d
# 공백지우기
a = " hi "
print(a.strip())
# 파이썬에는 문자열 리스트도 있음
# 리스트에 요소추가
a = ["손민철", "유현욱", "이경우"]
a.append("강승훈")
print(a)
# 리스트 vs 튜플==> 리스트는 append, pop, extend등의 함수를 통해 삽입,삭제 등이 가능하지만 튜플은 불가능, 자물쇠로 잠겨있다고 생각, final과 같이 변경 불가
# 튜플 끼리 더하여 새로운 튜플을 출력하는건 가능
# ex)
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1+t2)
# 튜플에 *3을하면 3번 반복되어 출력
# dictionary == JSON == OBJECT 비슷한 개념 ==> Key를 통해 Value를 얻는다는 것이 핵심개념
# ex) dictionary key값과 value추가
dic = {1: 'a'}
dic['name'] = "손민철"
print(dic)

# ex) 키값 삭제
del dic[1]
print(dic)

# ex) key 값만 추출, value 값만 추출
dic = {1: "a", 2: "b", 3: "c"}
print(dic.keys())
print(dic.values())
print(dic.items())
# 반복문에서 각각의 key값, value값만 추출할때 많이사용


# ex)모두 지우기
dic.clear()
print(dic)

# ex)키 값으로 직접추출 vs get메소드 활용 vs in
dic = {1: "a", 2: "b", 3: "c"}
# print(dic[4]) ==>키값이 없으면 에러
print(dic.get(4))  # ==> 없으면 none이라고 나옴 none이 default값이고 따로 메세지 줄수 있음
print(dic.get(4, "없어요"))
print(4 in dic)  # ==>bool형으로 있으면 true 없으면 false


# 집합 자료형: 중복허용 x , 순서 x(unordered) 데이터 다룰때 사용할 일이 많다.
s1 = set([1, 2, 3])
# s1 ={1,2,3} 둘다 똑같이 집합을 정의
print(s1)
# ex) 중복된 값이 있는 리스트가 있을때 이를 집합으로 바꾸어 중복 제거후 리스트로 다시 변경해
# 중복 값을 제거할 수 있음.
s2 = [1, 2, 2, 3, 3]
s3 = list(set(s2))
print(s3)
# 집합에 문자열을 넣으면 한글자 씩 쪼개짐, 순서가 없으므로 순서가 뒤죽박죽, 중복제거

# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
# 합집합
print(s1 | s2)
print(s1.union(s2))
# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 집합에 요소 추가:add ,여러개 요소 추가: update
s1.add(7)
print(s1)
s1.update([8, 9, 10])
print(s1)
# 요소 제거:remove
s1.remove(1)
print(s1)

# bool ==> True or False
a = True
if a:
    print(s1)

# 리스트, 문자열, 튜플, 딕셔너리 값이 있으면 True, 비어있으면 False
a = "안녕"
if a:
    print(a)

a = ""
if a:
    print(a)


# 메모리와 주소
a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)
# ==>값을 복사한 것이 아니라 메모리의 같은 주소를 가지고 있으므로 a의 값을 바꾸면 b도 바뀐다
# ex)b의 값을 변하지 않게 하고싶을때
a = [1, 2, 3]
b = a[:]  # 슬라이싱해서 넣어주면 가능
a[1] = 4
print(a)
print(b)
a = [1, 2, 3]
b = copy(a)
a[1] = 4
print(a)
print(b)

# 변수 할당 방법
a, b = ('python', 'life')
print(a)
print(b)

(a, b) = 'python', 'life'
print(a)
print(b)

a, b = ['python', 'life']
print(a)
print(b)

[a, b] = 'python', 'life'
print(a)
print(b)

a = b = 'hello'
print(a)
print(b)

# 두 값을 바꾸기 c에서의 SWAP함수
a = 3
b = 5
print(a, b)
a, b = b, a
print(a, b)

# 조건문 if
money = True
if money:
    print("택시를 타고 가라")
    print("adsf")
else:
    print("걸어가라")
# 들여쓰기들 맞춰야함 tab키로 제어 중괄호 안에 묶듯이 같은 if문안의 실행문은 들여쓰기로 맞춰줘야함

# in 과 not in
number = [1, 2, 3]
if 1 in number:
    print("존재합니다")
else:
    print("존재하지 않습니다")

if 1 not in number:
    print("존재합니다")
else:
    print("존재하지 않습니다")

# 조건문에서 아무 것도 실행하지 않게하려면 :pass

if 1 in number:
    pass
else:
    print("존재하지 않습니다")

# 다중 조건 판단 elif ==> else if 랑 같은 개념

# 조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
# 이를 조건부 표현식으로 표현하면
message = "success" if score >= 60 else "failure"
print(message)

# while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit+1  # treeHit++ 사용불가
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

# break: 내가 알던 break문이랑 기능 동일, continue ==> 이 구문을 만나면 while의 맨 위로 올라감.
# continue example
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue  # continue구문때문에 짝수는 출력되지 않음.
    print(a)


# for 문
# 기본 구조 for i in 리스트,튜플:
# ex)
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)
for (first, last) in a:
    print(first)
    print(last)
# for문에서도 break나 continue 사용 가능

# range함수
# for i in range(1,11) ==> 1이상 11미만의 범위 지정 i를 자바나 c에서 for문에 i값의 범위지정하는거랑 마찬가지
# print메소드의 option값중에 end메소드는 출력문 뒤에 값을 정해줄 수 있음
print(2, end=" ")  # 연속되는 문자 사이에 공백이나 특정값 넣어줄 수 있음, 단위나 뒤에 특정값 붙일때 사용
print(3)

# 리스트 내포(List comprehension)
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)
#같은 의미
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num*3 for num in a if num % 2 == 0]
print(result)
#같은 의미
result = []
for num in a:
    if num % 2 ==0:
        result.append(num*3)
print(result)

result = []
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
#같은 의미
result = []
for x in range(2,10):
    for y in range(1, 10):
        result.append(x*y)
print(result)  



#함수:funcion==> def
def sum(a,b):
    result = a + b
    return result
print(sum(3,4))

def hi():
    print("hi")
hi()

#여러개의 인자를 받고싶을 때 ==>*args , dictionary를 인자로 ==> **kwargs
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3,4,5))

#return 값은 하나이다. 튜플형태로 묶여서 하나로 출력
def sum_and_mul(a,b):
    return a+b, a*b, a-b
print(sum_and_mul(1,2))
#그중 하나만 뽑아서 쓰고싶다면?
print(sum_and_mul(1,2)[0]) #나온 튜플 값중 첫번째 index의 값을 추출

#함수 default 값지정
def myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
myself("손민철",24) #함수 선언시 값을 미리 지정해놓으면 default값으로 지정되어 함수호출 때 비워도 dafault값으로 지정

#lambda 함수
def add(a,b):
    return a+b
add = lambda a,b: a+b #두개다 같은 의미 람다함수를 쓰면 축약해서 사용가능하므로 리스트 안에 함수를 넣을수 있음

#ex
myList = [lambda a,b: a+b, lambda a,b: a*b]
print(myList[0](1,2)) #myList의 0번째 인덱스에 있는 더하는 함수를 가져와서 매개변수로 1과2를 넣은 문장
print(myList[1](1,2))

#input ==> scanf

#print
print("life" "is" "too short") #문자열 합쳐줌 알아서
print("life","is","too short") #문자열 합쳐주고 콤마를 기준으로 공백 생성

#파일 읽고 쓰기
#write mode
f = open("새파일.txt", 'w')
for i in range(1, 11):
    date = "This is %dLine\n" % i
    f.write(date)
f.close()
#read mode
f = open("새파일.txt", 'r')
while True:
    line = f.readline() #readline() ==> 한 줄씩 읽어온다.
    if not line: break
    print(line)
f.close()
#readlines ==>리스트형태로 가져옴.
#read ==> 통채로 가져옴.
#readline ==> 한 줄씩 가져옴

#add mode(추가)
f = open("새파일.txt", 'a')
f.write("This is new line")
f.close

#with 함수
with open("foo.txt", 'w') as f: 
    f.write("Life is too short, you need python")
#foo.txt란 파일을 write모드로 생성하고 f라는 변수에 저장한다.라는 뜻이다.
#들여쓰기가 되어 있으므로 개별 함수로 생각, 따라서 close()해줄 필요가 없다.


