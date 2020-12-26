#변하지 않는 자료형: Immutable ==> 정수, 실수, 문자열, 튜플
#변할 수 있는 자료형: Mutable ==> 리스트, 딕셔너리, 집합

#클래스(class)
class Calculator:
    def __init__(self):
        self.result=0 #초기값 설정, 자바에서 생성자같은 개념
    
    def add(self, num): #self 매개변수로 객체가 들어감 ex)cal1 or cal2 java에서 this랑 비슷한 느낌인듯
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#상속
class MoreCal(Calculator):#자식 클래스
    pass
#부모클래스의 메소드와 동일한 이름의 메소드가 자식클래스에도
#구현되어져있으면 자식클래스에 있는 것을 사용 ==>overwrite
#모듈 ==> 다른 파일에 있는 파이썬 파일(.py)를 import해서 가져오는것
#그 파일 전부를 가져오고 싶을 땐 : import outer1
#그 파일의 특정 메소드만 가져오고 싶을 땐: from outer1 import add

#같은 폴더에 있는 파일이 아닌 외부 폴더에 있는 파일 import할때
#import sys
#sys.path.append("절대경로")

#패키지 ==> 모듈 여러 개 모아놓은 것

#예외 처리 ==> java에서 배운거랑 같음
#오류 강제 ==> raise 오류메세지

#내장함수
#filter 함수: 참인 결과 값만 남김
def positive(x):
    return x > 0
a = list(filter(positive,[1,-3,2,0,-5,6]))
print(a) #==> 0보다 큰 값만 남아서 1,2,6

#직접 만들어보기

#숫자를 넣으면 구구단을 리스트로 출력해주는 함수
def GuGu(num):
    a=[]
    for i in range(1,10):
        a.append(num*i)
    return a

result = GuGu(2)
print(result)

#3과 5의 배수 합 구하기
result = 0
for i in range(1,1000):
    if i % 3 ==0 or i % 5 ==0:
        result += i
print(result)

#페이징
def getTotalPage(m, n):
    if m % n ==0:
        return m//n
    else:
        return m// n + 1 #// 정수나눗셈 소수점 뒷자리 버림

#정규표현식 ==> import re
import re
p = re.compile('[a-z]+')
m = p.match('phython')
print(m)
m = p.search('3 phython')
print(m)
m = p.findall('life is too short') # 일치하는 구문을 리스트에 담아서 return
print(m)
m= p.finditer('life is too short')
for r in m:
    print(r)

#메타문자
# |(or), ^ (맨 처음을 나타내는) , $(맨 끝을 의미), \b(공백을 의미)

#전방탐색:긍정형 (?=)
#전방탐색:부정형 (?!)