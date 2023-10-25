sides = list(map(int, input().split()))
sides.sort()
small_two_sum = sum(sides[0:2])
if small_two_sum > sides[2]:
    print(sum(sides))
else:
    print(2 * small_two_sum - 1)
