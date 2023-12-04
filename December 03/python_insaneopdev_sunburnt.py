n = int(input("enter no.of buildings:"))

view = 0
max = 0
h = []

for i in range (0,n):
    temp = int(input("enter building height: "))
    h.append(temp)

for i in h:
    if i > max:
        view += 1
        max = i

print("no. of building that gets sunrise view:",view)
