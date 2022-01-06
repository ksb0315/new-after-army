#pm 5:07
#1
def odd_even(a):
    if a % 2 == 0:
        print('even')
    elif a % 2 == 1:
        print('odd')
odd_even(5)

#2
def average(*args):
    sum = 0
    leng = len(args)
    for i in args:
        sum += i
    return sum / leng
print(average(1,2,3,4,5))

#3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" % total)

#4
#다음 중 출력 결과가 다른 것 한 개를 골라 보자.
#print("you" "need" "python")
#print("you"+"need"+"python")
#print("you", "need", "python")
#print("".join(["you", "need", "python"]))
#3번이 다르다 다른 출력함수는 'youneedpython'이란 띄어쓰기가 없는 출력물을 보여주는 반면 3번은 'you need python'이란 띄어쓰기가 있는 출력물을 보여준다. print안의 문자열 사이에 ,(쉼표)를 넣었기 때문이다.

#5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f1 = open("test.txt", 'r')
print(f1.read())
f1.close()

#6
scan = input('내용을 작성하시오: ') #you need java로 입력
f1 = open("test.txt", 'a', encoding='utf-8')
f1.write('\n' + scan)
f1.close()

#7
f = open('test.txt', 'r', encoding='utf-8')
data = f.read()
print(data.replace('java', 'python'))
f.close()

#pm5:47(실망...)