import sys

r = sys.stdin.readline


def get_vertex(g):
    vertexs = {}

    for v, e in g:
        vertexs[v] = vertexs[v] + 1 if v in vertexs else 1
        vertexs[e] = vertexs[e] + 1 if e in vertexs else 1

    return sorted(vertexs.values())


def read_data():
    m1 = int(r())
    g1 = [list(map(int, r().strip().split())) for _ in range(m1)]
    m2 = int(r())
    g2 = [list(map(int, r().strip().split())) for _ in range(m2)]

    return m1, g1, m2, g2


if __name__ == "__main__":
    T = int(r())

    for _ in range(T):
        m1, g1, m2, g2 = read_data()
        print("yes" if m1 == m2 and get_vertex(g1) == get_vertex(g2) else "no")