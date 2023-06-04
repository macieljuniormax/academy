for i in range(10):
    print(i)
    if i == 5:
        break

j = 0
while j < 10:
    j += 1
    if j % 2 == 1:
        continue
    print(j)
