N = str(input())
L = []
for x in range(len(N)):
    L.append(int(N[x]))

count = [0] * 10

for x in L:
    count[x] += 1

same69 = int(((count[6] + count[9])+1)/2) 
count[6] = 0
count[9] = same69



print(max(count))








                
    