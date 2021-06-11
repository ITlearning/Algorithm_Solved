def solution(genres, plays):
    answer = []     # 답 리스트
    board = []      # 수록하는 기준대로 저장하는 리스트
    board_name = {} # 중복되는 이름 제거한 딕셔너리
    
    # 첫 번째 for 문
    # 먼저 board에 [['장르', 재생된 횟수], 인덱스] 순으로 한번에 묶어서 리스트를 생성
    index = 0 # 고유 인덱스
    for name, play in zip(genres, plays):
        board.append(([name,play], index))
        index += 1
        board_name[name] = 0
        
        
    # 두 번째 for 문
    # 람다식으로 처리가 가능하겠지만, 람다식이 미숙하여 for문으로 처리
    # 딕셔너리에 저장된 장르들의 총 재생된 횟수를 for문으로 돌며 처리
    for i in board:
        board_name[i[0][0]] = board_name[i[0][0]] + i[0][1]
    
    
    # 재생된 횟수 기준으로 많은 횟수부터 차례대로 정렬
    board_name = sorted(board_name.items(),reverse=True, key=lambda x:x[1])
    
    # 문제에서 설명한 기준대로 정렬
    board.sort(reverse=True, key=lambda x: ((x[0][1]), -x[1]))
    
    # board_name과 board는 다른 리스트입니다. (심지어 board_name은 딕셔너리로 시작)
    
    
    # 마지막 for 문
    # board_name 리스트에 저장된 중복을 뺀 이름들을 차례대로 불러온다.
    # 이미 횟수 기준으로 정렬이 되어있는 상태라 가져와서 사용하면 된다.
    
    # 중첩 for문을 돌려 가져온 이름에 해당하는 인덱스를 answer에 추가시켜준다.
    # 이때 각 리스트에서 2개씩 가져온다.
    for key in board_name:
        num = 0
        key_name = key[0]
        for i in range(len(board)):
            if board[i][0][0] == key_name:
                if num == 2:
                    break
                answer.append(board[i][1])
                num += 1
    
    return answer

#이게 왜 통과된건지 의문이지만..아무튼 통과다 ㅎㅎ ㅋㅋ