# 왕실의 나이트

input_data = input() # 수 입력

row = int(input_data[1]) # 뒤에 있는 수 입력

# 아스키 코드를 이용해 입력받은 글자를 수로 변환
col = int(ord(input_data[0]) - int(ord('a'))) + 1 

# 8개의 나이트 이동
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 이동할 수 있는 곳 수
result = 0

for step in steps :
    nrow = row + step[0]
    ncol = col + step[1]
    # 1 이하 8 이상은 옮길 수 없게 조건문 설정
    if nrow < 1 or nrow >= 8 or ncol < 1 or ncol >= 8 : continue 
    result += 1
    
print(result) # 갈 수 있는 수 출력