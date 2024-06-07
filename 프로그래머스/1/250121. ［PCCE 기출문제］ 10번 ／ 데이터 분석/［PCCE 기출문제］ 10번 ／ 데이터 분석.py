def solution(data, ext, val_ext, sort_by):
    schema_index = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    data = [row for row in data if row[schema_index[ext]] < val_ext]
    data = sorted(data, key=lambda x: x[schema_index[sort_by]], reverse=False)
    
    return data