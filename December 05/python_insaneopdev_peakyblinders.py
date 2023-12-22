ave = 0
stole = []
sum = 0

for i in range(5):
    temp = int(input("enter the amount stolen:"))
    stole.append(temp)

for i in range( 5):
        ave += stole[i]

ave = ave/5

for i  in range(5):
    if stole[i] >= ave:
        sum += stole[i]

print("sum of amount stolen than average = ", sum)