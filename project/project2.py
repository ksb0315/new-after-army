#06-2 3과 5의 배수 합하기
import math
result = []
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result.append(n)
#print(result)
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)