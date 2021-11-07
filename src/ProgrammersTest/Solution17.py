# 문자열 다루기 기본
# Description
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
#
# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# 입출력 예
# s	return
# "a234"	false
# "1234"    True


#s는 문자열
# isdecimal() 정수 및 소수점으로 구성된 문자열 판별
# isdigit() 정수와 지수로 구성된 문자열 판별할 수 있는 함수


# print("a1234".isdecimal())


def solution(s):
    print(len(s))
    if len(s)==4 or len(s)==6:#길이가 4 or 6
        print(s)
        answer = s.isdecimal()#문자열이 섞여있으면
        # print(answer)
    else:
        answer = False
    print(answer)
    return answer

solution("1234")