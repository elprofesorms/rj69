'''
istrue = False

while istrue is False:
    forty = int(input())
    if forty == 42:
        istrue == True
        break
    else:
        print(forty)
'''
'''
isTrue = False

while isTrue is False:
    n = int(input())
    rev = 0
    if n <= 9:
        continue

    else:

        while (n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10
    print(rev)

'''
'''
for i in range(int(input())): 
    n = input()
    output = n[::-1]  
    k = 0;
    for x in output:  
        if x == '0':  
            k += 1;
        else: 
            break

    print(output[k:])
'''

for i in range(int(input())):
    user = input()
    x = len(user)
    l=[]
    r=[]
    for x in range(i):
        if i<x/2:
            l.append(user[i])
        else:
            r.append(user[i])
    else:

