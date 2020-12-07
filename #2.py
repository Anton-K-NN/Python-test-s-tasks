#first idea was:
"""def f(x):
    if x <=2:
        return x
    else:
        return f(x-1)+f(x-2)+42

a=int(input())
print(f(a))"""
#... but it's not very fast.. )))


#variant with list is more quikly:

"""a=int(input())
s,i=1,1
ss=[0]

while s<=a:
    if s<=2:
        ss.append(s)
    else:
        ss.append(ss[i-1]+ss[i-2]+42)
    #print(s,' ',ss)
    s+=1
    i+=1

print(ss[a])"""

#more optimize of memory code and it's an answer:

a = int(input())
s = 1
ss = []
while s <= a:
    if s <= 2:
        ss.append(s)
    else:
        ss.append(ss[0]+ss[1]+42)
        #print(s,' ',ss)
        ss.pop(0)
        #print(s,' ',ss)
    s += 1
print(ss[1])

