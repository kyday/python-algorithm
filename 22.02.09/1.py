# strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거한다.
# capitalize() : 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다. 

def solution(s):
     return " ".join(x.capitalize().strip() for x in s.split(" "))
     