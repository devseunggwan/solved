def sorting_board(board):
    """
    보드의 한 라인을 스택을 사용할 수 있는 구조(0: floor, -1: roof)로 변경합니다.
    """
    
    return [[board[b][idx] for b in range(len(board)-1, -1, -1) if board[b][idx]] for idx in range(len(board))]

def board_game(board, moves):
    stack = []
    clear = 0
    
    for move in moves:
        if not board[move-1]:
            continue
        
        stack.append(board[move-1].pop())
        if len(stack) < 2:
            continue
        
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            clear += 2
            for _ in range(2):
                stack.pop()
    
    return clear

def solution(board, moves):
    board = sorting_board(board)
    answer = board_game(board, moves)
        
    return answer