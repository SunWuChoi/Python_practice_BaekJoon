n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    print(f"{len([i for i in l[1:] if i > (sum(l[1:]) / l[0])]) / l[0] * 100:.3f}%")

# num_of_tests = int(input())
# for i in range(num_of_tests):
#     array = list(map(int, input().split()))
#     num_of_students = array[0]
#     array = array[-num_of_students:]
#     average = sum(array) / num_of_students
#     num_above_average = len([i for i in array if i > average])
#     percentage = num_above_average / num_of_students * 100
#     print(f"{percentage:.3f}%")