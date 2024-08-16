N = int(input())


for i in range(1, N + 1):
    print(f"Class {i}")

    grades = sorted(list(map(int, input().strip().split()))[1:])

    max_grade = grades[-1]
    min_grade = grades[0]
    largest_gap = max([grades[i + 1] - grades[i] for i in range(len(grades) - 1)])

    print(f"Max {max_grade}, Min {min_grade}, Largest gap {largest_gap}")
