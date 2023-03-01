import os
os.system('cls')
dict1=dict()
while True:
    inp=input()
    if inp=='-----':
        break
    name,*score=inp.split()
    s=[]
    for i in score:
        s.append(int(i))
    if name in dict1:
        dict1[name].append(sum(s))
    else:
        dict1[name]=s

for i in dict1:
    dict1[i]=sum(dict1[i])

reverse_dict1 =dict()
for i in dict1:
    key = dict1[i]
    if key in reverse_dict1:
        reverse_dict1[key].append(i)
    else:
        reverse_dict1[key] = [i]
a=sorted(reverse_dict1,reverse=True)
d=dict()
for i in a:
    for j in reverse_dict1[i]:
        print(j,end=" ")