print("hello")
#이건 주석이에요

a="hobby"
#원하는값 count함수
print(a.count("b"))
#원하는 값 find 함수(첫번째로 찾은 값의 인덱스 return), 비슷함 함수로 index함수도 있는데 이건 찾는 값있으면 index리턴 없으면 에러
print(a.find("b"))
#원하는 문자열 삽입
a=","
print(a.join('abcd')) #==>결과:a,b,c,d
