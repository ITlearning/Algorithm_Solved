import string 

num = int(input().strip())

if num == 0 :
    string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
else :
    string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ


# etc
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789