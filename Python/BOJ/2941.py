# 크로아티아 알파벳

cAlphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

text = input()
# 와;; 맞네 이거네. 저 위에 알파벳에 어울리는 글자에 별표를 해두면 그게 숫자이니까 와,,
# 문자 수 찾기 문제에선 별 표시 좋은 것 같다
for i in cAlphabet:
    text = text.replace(i, "*")

print(len(text))