#06-3 게시판 페이징하기
def getTotalPage(x,y): #x = 게시물 건수 y = 페이지당 보여줄 게시물 수
    if x % y == 0:
        return x // y
    else:
        return x // y + 1
print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))   
    