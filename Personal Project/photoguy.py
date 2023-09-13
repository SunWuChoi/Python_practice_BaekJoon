N = int(input())
A = list(map(int, input().split()))


def max_finder():
    curr_max = 0
    for window_size in range(N, 0, -1):
        print(window_size)
        for step in range(N - window_size + 1):
            l = [0 for i in range(1000000)]
            for i in range(step, step + window_size):

                if l[A[i]] == 0:
                    l[A[i]] = 1
                else:
                    break
            else:
                if window_size > curr_max:
                    curr_max = window_size

    return curr_max


print(max_finder())
