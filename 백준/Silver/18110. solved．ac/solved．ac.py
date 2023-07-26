import sys

def readline():
    return sys.stdin.readline()

def custom_round(n):
    return int(n) + (1 if n - int(n) >= 0.5 else 0)

if __name__ == "__main__":
    n = int(readline())
    answer = 0

    if n:
        cut_avg = custom_round(n*(0.15))
        opinion = sorted([int(readline()) for _ in range(n)])
        opinion = opinion[cut_avg:len(opinion)-cut_avg]
        answer = custom_round(sum(opinion)/len(opinion))

    print(answer)
