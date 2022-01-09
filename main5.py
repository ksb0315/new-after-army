#pm5:00
#1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

#2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        
cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

#3-1
all([1, 2, abs(-3)-3])
#출력 결과 : False ==> all은 내장함수로 리스트 혹은 문자열과 같은 나열되어있는 자료형들 중에 단 하나라도 True 값이 있으면 True를 반환한다.
#3-2
chr(ord('a')) == 'a'
#출력 결과 : True ==> 내장함수 ord는 'a'값을 유니코드(아스키코드)값으로 반환시켜주며 내장함수 chr은 유니코드 값을 문자열로 반환시킨다. 따라서 반환된 값은 True이다.

#4
a = list(filter(lambda x : x > 0,[1, -2, 3, -5, 8, -3]))
print(a)

#5
print(int('0xea', 16))

#6
a = list(map(lambda x:x*3, [1,2,3,4]))
print(a)

#7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
result = max(a) + min(a)
print(result)

#8
print(round(17/3, 4))

#9~11번 idle 스크립트 작성으로 실행함
#9
#import sys
#
#numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력
#
#result = 0
#for number in numbers:
#    result += int(number)
#print(result)

#10
#다음처럼 os 모듈의 chdir을 사용하여 C:\doit 이라는 디렉터리로 이동한다.
#
#>>> import os
#>>> os.chdir("c:/doit")
#그리고 다음처럼 os 모듈의 popen을 사용하여 시스템 명령어인 dir을 수행한다.
#
#>>> result = os.popen("dir")
#popen의 결과를 출력하기 위해 다음과 같이 수행한다.
#
#>>> print(result.read())
#...
#abc.txt
#bidusource.html
#...

#11
#다음과 같이 glob 모듈을 사용한다.
#
#>>> import glob
#>>> glob.glob("c:/doit/*.py")
#['c:/doit/doit01.py', 'c:/doit/test.py']

#12
import time
a = time.strftime("%Y/%m/%d %H:%M:%S")   # %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초
print(a)

#13
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)

print(result)

#pm5:50 오늘을 풀이 보면서 했음 말이안됨 ㅠ