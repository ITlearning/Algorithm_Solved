# 킹

# 알파벳 -> 숫자
columns_alphabet = { 
    "A": 1, "B": 2, "C": 3, "D": 4, 
    "E": 5, "F": 6, "G": 7, "H": 8
    }

# 숫자 -> 알파벳
columns_number = { value: key for key, value in columns_alphabet.items() }

# 컨트롤러
controller = {
    "R": [1,0], "L": [-1,0], "B": [0,-1],
    "T": [0,1], "RT": [1,1], "LT": [-1,1],
    "RB": [1,-1], "LB": [-1,-1]
    }

# 왕의 위치, 돌의 위치, N
king_location, stone_location, N = input().split()
N = int(N)

# 왕,돌 위치 가져오기 
king = [columns_alphabet[king_location[0]], (int(king_location[1]))]
stone = [columns_alphabet[stone_location[0]], (int(stone_location[1]))]
# 움직임 저장
for _ in range(N):
    key = input()
    move = controller[key]
    # 움직인 것 적용하기 전에 확인
    king_x = king[0] + move[0]
    king_y = king[1] + move[1]

    stone_x = stone[0] + move[0]
    stone_y = stone[1] + move[1]

    if 1 <= king_x < 9 and 1 <= king_y < 9:
        # 돌의 위치가 넘어가지 않고, 동시에 킹이 움직일 위치에 있으면
        if 1 <= stone_x < 9 and 1 <= stone_y < 9 and king_x == stone[0] and king_y == stone[1]:
            king = [king_x, king_y]
            stone = [stone_x, stone_y]
        # 돌의 위치와 킹의 위치가 같아졌다면
        elif king_x == stone[0] and king_y == stone[1]:
            continue
        else:
            # 그것도 다 아니고 왕만 움직일 수 있으면
            king = [king_x, king_y]

# 답 변환
answer_king = str(columns_number[king[0]]) + str(king[1])
answer_stone = str(columns_number[stone[0]]) + str(stone[1])

print(answer_king, answer_stone)

    
