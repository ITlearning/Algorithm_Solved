def solution(s, n):
    result = ""
    for i in s:
        if i != ' ':
            if 65 <= ord(i) <= 90:
                if int(ord(i)) + n > 90:
                    tmp = int(ord(i)) + n - 90
                    tmp -= 1
                    result += chr(65+tmp)
                else:
                    tmp = int(ord(i)) + n
                    result += chr(tmp)
                
            elif 97 <= ord(i) <= 122:
                if int(ord(i)) + n > 122:
                    tmp = int(ord(i)) + n - 122
                    tmp -= 1
                    result += chr(97+tmp)
                else:
                    tmp = int(ord(i)) + n
                    result += chr(tmp)
        else:
            result += " "
    return result