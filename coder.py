s = 'abracadabra'

dict = ['']
s2 = ''
i = 0

while i < len(s):
    c = s[i]                    #index of a new char
    t = 0                       #index of a parent
    form = str(t) + ' ' + str(c)#formed dictionary value
    while dict.count(form)>0:
        t = dict.index(form)    #new index of a parent
        i+=1
        if i >= len(s):
            break
        c = s[i]
        form = str(t) + ' ' + str(c)
    dict.append(form)
    i+=1

for i in range(len(dict)):
    s2+=dict[i]

print(s2)
