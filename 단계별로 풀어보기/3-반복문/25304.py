total_price = int(input())
types = int(input())
total_added = 0
for i in range(types):
    price, num = map(int, input().split())
    total_added += price * num
if total_price == total_added:
    print("Yes")
else:
    print("No")