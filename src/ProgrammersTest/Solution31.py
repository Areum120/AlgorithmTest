'''
시저 암호

문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로
바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고,
3만큼 밀면 "DE"가 됩니다.

"z"는 1만큼 밀면 "a"가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수,
solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.

입출력 예
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"
'''

def solution (n, s):
#     s는 소문자 or 대문자 or 소문자+대문자 + 공백
#
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # print(alphabet[0:1])#a
    # print(alphabet[1:2])#b
    num = []
    answer = ''
    for i in range(len(s)):
        print(s[i])
        for j in range(len(alphabet)):
            if s[i].isupper()==True:  # 대문자면
                alphabet_upper = alphabet[j].upper()#알파벳을 대문자로 바꾸기
                if s[i] == alphabet_upper: #같은 문자일 때
                   print(j)
                   num.append(j)
                   # s[i] == alphabet_upper
                   # print(s[i])
                #     n만큼 이동하는 로직 짜기
            else: #소문자면
                if s[i] == alphabet[j]: #같은 문자일 때
                   print(j)
                   num.append(j)
                   # s[i] == alphabet[j] #그대로 출력
                   # print(s[i])
                #     n만큼 이동하는 로직 짜기 -> for문 바깥에서 바꿔야 할듯
                # s[i] = alphabet[j+n:(j+n)+1]#동일한 알파벳에서 n만큼 이동한다
    print(num)
    for k in num:
        # print(alphabet[k:k+1])
        if #끝이 z일 때 처리는 어떻게 해야 할 지?
        print(alphabet[k+n:(k+1)+n])

s = "a B z"
n = 1

print(solution(n, s))