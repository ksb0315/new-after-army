#06-1 내가 프로그램을 만들 수 있을까?(구구단)
def GuGu(x):
    result = []
    num = 1
    while num < 10:
        result.append(x * num)
        num += 1
    return result
    
print(GuGu(2))