num = int(input())
counter = 1
i = 1
while num > i:
    counter += 1
    i += counter
diff = i - num
if counter % 2 == 1:
    print(f"{1 + diff}/{counter - diff}")
else:
    print(f"{counter - diff}/{1 + diff}")
