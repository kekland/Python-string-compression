s = 'abracadabra'

data = ['']                     #dictionary
s2 = ''
i = 0

while i < len(s):
    c = s[i]                    #index of a new char
    t = 0                       #index of a parent
    form = str(t) + ' ' + str(c)#formed dictionary value
    while form in data:
        t = data.index(form)    #new index of a parent
        i+=1
        if i >= len(s):
            break
        c = s[i]
        form = str(t) + ' ' + str(c)
    data.append(form)
    i+=1

for d in data:
    s2+=d

print(s2)
