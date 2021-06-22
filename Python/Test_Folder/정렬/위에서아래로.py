N = int(input())
board = []
for i in range(N):
    board.append(int(input()))

def quick_sort(board):
    if len(board) <= 1:
        return board
    
    pivot = board[0]
    tail = board[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(board))