triangle_result = ["Equilateral", "Isosceles", "Scalene"]

while True:
    sides = list(map(int, input().split()))
    if all(side == 0 for side in sides):
        break

    if max(sides) >= sum(sides) - max(sides):
        print("Invalid")
        continue

    print(triangle_result[len(set(sides))-1])
