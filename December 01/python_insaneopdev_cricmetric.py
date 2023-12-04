n = int(input('no of players:'))
runs = []
total = 0
temp = 0
greatest = 0

for i in range(0,n):
    print("player",i,"score:")
    temp = int(input())
    runs.append(temp)


for i in range(0,n):
    total += runs[i]

print("total runs:",total)

greatest = max(runs)

for i in range(0,n):
    if greatest == runs[i]:
        print("highest score index:",i)
