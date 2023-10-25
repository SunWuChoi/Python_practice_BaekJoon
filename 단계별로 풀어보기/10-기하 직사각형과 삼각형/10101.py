angles = []
angle_set = set()

for _ in range(3):
    input_angle = int(input())
    angles.append(input_angle)
    angle_set.add(input_angle)

is180 = sum(angles) == 180
diff_angles = len(angle_set)
triangle_result = ["Equilateral", "Isosceles", "Scalene"]

if is180:
    print(triangle_result[diff_angles-1])
else:
    print("Error")
