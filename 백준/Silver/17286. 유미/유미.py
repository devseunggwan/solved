def get_data():
    return [list(map(int, input().split())) for _ in range(4)]

def distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def get_short_distance(M):
    short_distance = min(
        [
            distance(M[0], M[1]) + min(distance(M[1], M[2]), distance(M[1], M[3])) + distance(M[2], M[3]),
            distance(M[0], M[2]) + min(distance(M[2], M[1]), distance(M[2], M[3])) + distance(M[1], M[3]),
            distance(M[0], M[3]) + min(distance(M[3], M[1]), distance(M[3], M[2])) + distance(M[1], M[2]),
        ]
    )
    
    return int(short_distance)

if __name__ == "__main__":
    M = get_data()
    short_distance = get_short_distance(M)
    print(short_distance)