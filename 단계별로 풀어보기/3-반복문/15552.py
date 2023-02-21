import sys

for _ in range(int(sys.stdin.readline())):
    first, second = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(first + second)+"\n")
