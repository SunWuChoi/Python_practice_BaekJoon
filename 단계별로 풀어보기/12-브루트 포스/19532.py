a, b, c, d, e, f = map(int, input().split())

# Brute force
# for x in range(-999, 1000):
#     for y in range(-999, 1000):
#         if a * x + b * y == c and d * x + e * y == f:
#             print(x, y)

# Cramer's rule
# https://rosettacode.org/wiki/Cramer%27s_rule

print((c * e - b * f) // (a * e - b * d), (a * f - c * d) // (a * e - b * d))
