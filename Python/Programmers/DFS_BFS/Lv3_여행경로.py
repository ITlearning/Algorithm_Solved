def solution(tickets):
    answer = []
    board = {}
    # 전체 답을 넣을 answer 리스트와
    # 현재 각 공항과 연결된 딕셔너리를 구현할 board
    
    # 딕셔너리에 연결된 공항들을 key, value 로 연결
    for a,b in tickets:
        board[a] = board.get(a,[]) + [b]
        
    # 연결된 공항들의 순서를 역순으로 정렬
    # 역순으로 정렬하는 이유는 리스트는 가장 늦게 들어간거부터
    # 먼저 뽑으니까 뒤에서부터 알파벳 순서대로 뽑기 위해서
    for a in board:
        board[a].sort(reverse=True)
        
    # ICN 먼저 출발한다고 했으니 먼저 추가해주고
    # PATH는 이동한 공항의 이름들
    tmp = ["ICN"]
    path = []
    
    # tmp가 0이 될때까지 돌아감
    while tmp:
        # 현재 위치한 공항
        cur = tmp[-1]
        
        # 만일 현재 위치한 공항이 board에 없거나,
        # 혹은 해당 공항에서 더이상 갈 곳이 없을 경우
        if cur not in board or len(board[cur]) == 0:
            # 이동했던 공항을 path에 푸시
            path.append(tmp.pop())
        else:
            # 그게 아니면 계속 이동해야 하니,가장 뒤에 있는 공항 추가 후
            # 넣었으니 빼줘야 함
            tmp.append(board[cur][-1])
            board[cur] = board[cur][:-1]
    # 이동이 모두 끝난 path의 공항 순서는 역순으로 되어있으니,
    # answer에는 원래의 순서대로 다시 바꿔줌
    answer = path[::-1]
    return answer