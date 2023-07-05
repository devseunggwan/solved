from operator import itemgetter

def fault_rate(n, stages):
    staging = 0
    not_clears = 0
    
    for stage in stages:
        staging += (1 if stage >= n else 0)
        not_clears += (1 if stage == n else 0)
        
    return (n, (0 if not staging else not_clears/staging))

def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs

def solution(N, stages):
    # O(N)
    answer = [fault_rate(n, stages) for n in range(1, N+1)]
    
    # O(2NlogN)
    answer = multisort(xs=answer, specs=((1, True), (0, False)))
    
    # O(N)
    answer = [x[0] for x in answer]
    
    return answer
    