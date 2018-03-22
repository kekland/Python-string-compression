def decode(data, n):
    s = data[n]
    if len(s)==0:                   #if a parent is null (num 0 in a data)
        return s
    temp = ''                       #index of a parent
    i = 0
    while s[i] != ' ':
        temp += s[i]
        i+=1
    i+=1                            #index of a new char
    return decode(data, int(temp)) + s[i]

s = "0 a0 b0 r1 c1 d1 b3 a"         #coded string

data = ['']                         #dictionary
s2 = ''                             #decoded string
i=0

while i<len(s):
    temp = ''                       #index of a parent
    while s[i] != ' ':
        temp += s[i]
        i+=1
    i+=1                            #index of a new char
    data.append(temp + ' ' + s[i])
    i+=1                            #index of a next part

for i in range(1, len(data)):
    s2 += decode(data, i)

print(s2)


