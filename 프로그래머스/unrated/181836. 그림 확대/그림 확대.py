def solution(picture, k):
    answer = []
    for r in [''.join([pixel * k for pixel in row]) for row in picture]:
        for _ in range(k):
            answer.append(r)
    return answer    