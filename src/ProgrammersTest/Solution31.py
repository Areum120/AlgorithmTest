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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # print(len(alphabet))
    print(alphabet[len(alphabet) - 1])

    # print(alphabet[0:1])#a
    # print(alphabet[1:2])#b

    n_str = []
    for v in s:
        print(v)
        if v.isupper()==True: #대문자면 n만큼 이동한 문자 대문자로 변경
            v_lower = v.lower()#소문자로 변경
            v_num = alphabet.find(v_lower)#알파벳에서 인덱스 위치 찾기
            if v_num+n > 25:
                change_str = alphabet[(v_num+n)-26:(v_num+n)-26+1]
                n_str.append(change_str.upper())
            elif v_num+n <= 25:
                change_str = alphabet[v_num + n:(v_num + n) + 1]
                n_str.append(change_str.upper())
        elif v==' ':#공백일 때
            n_str.append(' ')
        else: #소문자면 n만큼 이동한 소문자 출력
            v_num = alphabet.find(v)#알파벳에서 인덱스 위치 찾기
            print(v_num)
            if v_num + n > 25:
                change_str = alphabet[(v_num + n) - 26:(v_num + n) - 26 + 1]
                n_str.append(change_str)
            elif v_num+n <= 25:
                change_str = alphabet[v_num + n:(v_num + n) + 1]
                n_str.append(change_str)
    print(n_str)
#     리스트를 문자열로
    list_to_str = ''.join(n_str)
    print(list_to_str)
    return list_to_str

# num 리스트에 대문자와 소문자 인덱스 번호 담기
    # num = []
    # answer = ''
    # for i in range(len(s)):
    #     # print(s[i])
    #     for j in range(len(alphabet)):
    #         if s[i].isupper()==True:  # 대문자면
    #             alphabet_upper = alphabet[j].upper()#알파벳을 대문자로 바꾸기
    #             if s[i] == alphabet_upper: #같은 문자일 때
    #                # print(j)
    #                num.append(j)
    #         else: #소문자면
    #             if s[i] == alphabet[j]: #같은 문자일 때
    #                # print(j)
    #                num.append(j)

    #     n만큼 이동하는 로직 짜기 -> for문 바깥에서 바꿔야 할듯
    # print(num)

# n만큼 이동하는 로직짜기
    # n은 1이상 25이하 자연수
    # n만큼 이동할 때 z=25를 넘어가는 경우

    # k가 1이상 이고 n이 24보다 클 때
    # k가 2이고 n이 23보다 클 때
    # k가 3이고 n이 22보다 클 때
    # -> 즉, k + n이 25보다 클 때

    # k=1, n = 25 , len(n) = 1, b -> a, k에서 -1만큼
    # k=2, n = 24, 25 , len(n) = 2, n이 24면 c -> a, k에서 -2만큼, n이 25이면 c -> b, k에서 -1만큼
    # k=3, n = 23, 24, 25 -> -3, -2, -1만큼 이동
    # k=4, n = 22, 23, 25, 25 -> -4, -3, -2, -1만큼 이동
    # k=5, n = 21, 22, 23, 24, 25 -> -5, -4, -3, -2, -1만큼 이동

    # for k in num:
    #     # print(alphabet[k:k+1])
    #     if k+n > 25:
    #         print(alphabet[(k+n)-26:(k+n)-26+1])
    #     else:
    #         print(alphabet[k+n:(k+n)+1])


s = "aaaaaaaaaaaaaaa"
n = 25

print(solution(n, s))