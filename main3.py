#1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#결과값은 shirt이다. 왜냐하면 문자열 a는 ' ' 슬라이싱 없이는 단어별로 나뉘는것이 아니라 알파벳별로 나뉘는 것이기 때문이다.
#그리고 shirt 단어는 알파벨이 아니기 때문에 'elif "shirt" not in a:' 조건문에 부합한다.

#2
num = 0
sum = 0
while num <= 1000:
    num += 1
    if num % 3 == 0:
        sum = sum + num
print('3의 배수의 합: %d' % sum)

#3
num = 1
while num < 6:
    print("* " * num)
    num += 1

#4
for i in range(1,101):
    print(i, end =' ')
    if i % 10 == 0:
        print('')

#5
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in range(0,10):
    sum += score[i]
ave = sum / 10
print("평균값: %.2f" % ave)

#6
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)