# 성적이 낮은 순서로 학생 출력하기

n = int(input())
board = []

for _ in range(n):
    inputData = input().split()
    board.append((inputData[0], int(inputData[1])))

# 점수를 기준으로 정렬(오름차순)
board = sorted(board, key=lambda student: student[1])

for student in board:
    print(student[0], end=' ')