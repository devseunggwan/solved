class NQueen:
    def __init__(self):
        self.__N = int
        self.__B = list
        self.__M = list
        self.ans = int
    
    def __initialize(self, N):
        self.__N = N
        self.__B = [0 for _ in range(N)]
        self.__M = [0 for _ in range(N)]
        self.ans = 0
    
    def __is_promising(self, i):        
        for j in range(i):
            if self.__B[i] == self.__B[j] or abs(self.__B[j] - self.__B[i]) == i - j:
                return False

        return True
    
    def __n_queen(self, N):
        if N == self.__N:
            self.ans += 1
            return

        for i in range(self.__N):
            if self.__M[i]:
                continue
            
            self.__B[N] = i
            if self.__is_promising(N):
                self.__M[i] = 1
                self.__n_queen(N+1)
                self.__M[i] = 0

    
    def solve(self, N):
        self.__initialize(N)
        self.__n_queen(0)
        
        return self.ans

def solution(n):
    n_queen = NQueen()
    return n_queen.solve(n)