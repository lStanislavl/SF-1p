multipl=1
i=1
while i<10:
    i += 1
    if i % 2 == 0:
        continue
    multipl *= i
print(multipl)