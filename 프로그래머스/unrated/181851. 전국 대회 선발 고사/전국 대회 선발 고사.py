def solution(ranks, attendance):
    ranks = sorted([(idx, rank) for idx, rank, flag in zip(range(len(ranks)), ranks, attendance) if flag], key=lambda x: x[1])
    return 10000 * ranks[0][0] + 100 * ranks[1][0] + ranks[2][0]