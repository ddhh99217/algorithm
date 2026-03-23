a = int(input())
b = int(input())
c = int(input())

x = a*b*c
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
x = str(x)

for i in x:
    if i == '0':
        count0 += 1


for i in x:
    if i == '1':
        count1 += 1
        
for i in x:
    if i == '2':
        count2 += 1


for i in x:
    if i == '3':
        count3 += 1


for i in x:
    if i == '4':
        count4 += 1


for i in x:
    if i == '5':
        count5 += 1

for i in x:
    if i == '6':
        count6 += 1


for i in x:
    if i == '7':
        count7 += 1

for i in x:
    if i == '8':
        count8 += 1


for i in x:
    if i == '9':
        count9 += 1

print(count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, sep="\n")