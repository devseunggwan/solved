import sys

class FloydWarshall:
    def __init__(self, N, M):
        self.__N = N
        self.__M = M
        self.__map = {
            i : {
                j: sys.maxsize for j in range(1, self.__N+1)
            } for i in range(1, self.__N+1)
        }

    @staticmethod
    def readline():
        return sys.stdin.readline()
    
    def __get_map(self) -> None:
        for _ in range(self.__M):
            a, b, c = map(int, self.readline().strip().split())
            self.__map[a][b] = min(self.__map[a][b], c)

    def __mapping(self) -> None:
        for k in range(1, N+1):
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if i == j or i == k or k == j:
                        continue

                    self.__map[i][j] = min(self.__map[i][j], self.__map[i][k]+self.__map[k][j])

    def __print_map(self) -> None:
        for i in range(1, self.__N+1):
            print(*[self.__map[i][j] if self.__map[i][j] != sys.maxsize else 0 for j in range(1, self.__N+1)])

    def run(self):
        self.__get_map()
        self.__mapping()
        self.__print_map()
        
        return self.__map

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    floyd_warshall = FloydWarshall(N, M)
    floyd_warshall.run()