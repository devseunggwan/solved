def run(query, idx, entity):
    s, e, k = query
    return entity + 1 if s <= idx <= e and idx % k == 0 else entity
    
def solution(arr, queries):    
    for query in queries:
        arr = [run(query, idx, entity) for idx, entity in enumerate(arr)]
    return arr