Ko = 80
Eng = 75
Math = 55
sum = Ko + Eng + Math
ave =  sum / 3
print(ave)

hong = "881120-1068234"
age = hong.split("-")
year = int(age[0]) + 19000000
print("홍길동 연월일", year)
print(age[1][0])

string = "a:b:c:d"
print(string.replace(":", "#"))

integer = [2,3,1,4,5]
integer.sort()
integer.reverse()
print(integer)

string2 = ['Life', 'is', 'too', 'short'] 
result = " ".join(string2)
print(result)