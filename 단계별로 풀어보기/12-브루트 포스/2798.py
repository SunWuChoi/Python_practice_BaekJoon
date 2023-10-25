def brute(number_of_cards, cards, target):
    closest = 10000000
    for first in range(number_of_cards - 2):
        for second in range(first + 1, number_of_cards - 1):
            for third in range(second + 1, number_of_cards):
                curr = cards[first] + cards[second] + cards[third]
                if abs(closest - target) >= abs(curr - target):
                    if curr < target:
                        closest = curr
                    elif curr == target:
                        return curr
    return closest

number_of_cards, target = map(int, input().split())
cards = list(map(int, input().split()))
print(brute(number_of_cards, cards, target))
