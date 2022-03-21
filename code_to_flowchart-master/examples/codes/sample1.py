temp = []
for i in range(n):
    temp.append(a[i])
a = a[n:]
print(a)
print(temp)
for ele in temp:
    a.append(ele)
print(a)

a = [1,2,3,4,5,6]    
print(a)