n = int(input("enter no. of items:"))
id = []
frequ = []

for i in range (0,n):
    temp = int(input("enter product id:"))
    id.append(temp)

print(id)

id = sorted(id)

freq = {}

for num in id:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for i,j in freq.items():
    frequ.append(j)
    
print(frequ)

