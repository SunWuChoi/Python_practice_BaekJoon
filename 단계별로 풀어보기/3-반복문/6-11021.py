num = int(input())
for i in range(num):
    first, second = map(int, input().split())
    print(f"Case #{i+1}: {first+second}")