#학교 멘토링활동에서 멘토역활로 맡아서 멘티들은 총 3회의 멘토링을 필수 참여해야합니다.
#하지만 매번 출석체크간에 여러움이 있고 마지막 멘토링때 모두에게 자신의 참여횟수를 보여주고자 만들었습니다.
def attend(name):
    mentoring1 = ['x하x', 'x승x','x정x','x동x','x재x','x경x','xx규','xx호','xx서','xx혁'
    ,'x현x','x재x','x동x','x선x','xx혁','김xx','xx욱','xx현','xx건']

    mentoring2 = ['김xx', '김xx','x정x','x동x','x재x','x경x','xx규','xx호','xx현','xx서'
    ,'박xx','x현x','x재x','x건x','x동x','안xx','김xx','김xx','장xx','xx건','x호x']

    mentoring3.append(name)
    num_attend = 0

    if name in mentoring1:
        num_attend += 1
        print(name,"님은 1회차 출석")
    else:
        print(name,"님은 1회차 X")
    
    if name in mentoring2:
        num_attend += 1
        print(name,"님은 2회차 출석")
    else:
        print(name,"님은 1회차 X")
    
    if name in mentoring3:
        num_attend += 1
        print(name,"님은 3회차 출석")
    else:
        print(name,"님은 1회차 X")

    print(name,"의 멘토링 참석 횟수:",num_attend)
    print(mentoring3)

mentoring3 = [] #추후 확인하고 출결을 남기기 위해 계속 학생이름 추가
total = int(input()) #zoom에서 총명수는 확인 할 수 있으니 참가자 수를 입력
for i in range(total):#참가자 수만큼 추가할 것이니 그 횟수만큼 반복
    my_name = input() #학생이름 입력
    attend(my_name)#최종 참석 횟수와 누적 학생이름 출력