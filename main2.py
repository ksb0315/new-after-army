#8
atu = (1,2,3)
btu = (4,)
print(atu + btu)

#9
a = dict()
a = {}
#다음중 오류는?
#a['name'] = 'python'
#a[('a',)] = 'python'
#a[[1]] = 'python'
#a[250] = 'python'      
#3번째 : mutable 값이기 때문

#10
aten = {'A':90, 'B':80, 'C':70}
print(aten.pop('B'))

#11
aelev = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
result = set(aelev)
print(result)

#12
atwel = btwel = [1,2,3]
atwel[1] = 4
print(btwel)
