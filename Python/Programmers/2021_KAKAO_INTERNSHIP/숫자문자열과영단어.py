def solution(s):
    answer = ""
    
    alphabet = {"zero": 0,"one": 1, "two": 2, "three": 3, 
                "four": 4, "five": 5, "six": 6, 
                "seven": 7, "eight": 8, "nine": 9
               }
    
    tmp_text = ""
    for text in s:
        if text.isdigit():
            print(text)
            answer += text
            continue
        tmp_text += text
        #print(tmp_text)
        if tmp_text in alphabet:
            answer += str(alphabet[tmp_text])
            tmp_text = ""
    
    return int(answer)