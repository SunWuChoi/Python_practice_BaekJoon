import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

best_required_time = int(1e9)
best_height = 0

highest_height = 0
lowest_height = int(1e9)

for line in Map:
    for block in line:
        if block > highest_height:
            highest_height = block
        if block < lowest_height:
            lowest_height = block

for height in range(lowest_height, highest_height + 1):
    required_block = 0
    required_time = 0

    for line in Map:
        for block in line:
            diff = height - block

            if diff > 0:
                required_block += diff
                required_time += diff
            elif diff < 0:
                required_block += diff
                required_time -= 2 * diff
    if best_required_time >= required_time:
        if B >= required_block:
            best_required_time = required_time
            if best_required_time == required_time:
                if best_height < height:
                    best_height = height
            else:
                best_height = height
print(best_required_time, best_height)
