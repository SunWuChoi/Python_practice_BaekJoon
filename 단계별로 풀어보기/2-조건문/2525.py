curr_hour, curr_min = map(int, input().split())
req_min = int(input())

total_min = curr_min + req_min
total_hour = curr_hour + total_min // 60

print(f"{total_hour % 24} {total_min % 60}")