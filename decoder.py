def decode(dict, n):
    s = dict[n]
    if len(s)==0:                   #if a parent is null (num 0 in a dict)
        return s
    temp = ''                       #index of a parent
    i = 0
    while s[i] != ' ':
        temp += s[i]
        i+=1
    i+=1                            #index of a new char
    return decode(dict, int(temp)) + s[i]

s = "0 a0 b0 r1 c1 d1 b3 a"         #coded string

dict = ['']                         #dictionary
s2 = ''                             #decoded string
i=0

while i<len(s):
    temp = ''                       #index of a parent
    while s[i] != ' ':
        temp += s[i]
        i+=1
    i+=1                            #index of a new char
    dict.append(temp + ' ' + s[i])
    i+=1                            #index of a next part

for i in range(len(dict)):
    s2 += decode(dict, i)

print(s2)


