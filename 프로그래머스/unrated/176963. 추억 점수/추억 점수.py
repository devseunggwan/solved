def scoring(photo, score_board):
    return sum([score_board[p] for p in photo if p in score_board])

def solution(name, yearning, photos):
    score_board = {
        n: y for n, y in zip(name, yearning)
    }
    
    return [scoring(photo, score_board) for photo in photos]