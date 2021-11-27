'''
자연수 뒤집어 배열로 만들기

Description
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]

'''

# 문제 1
# def solution(n):
#     n_split = list(str(n))
#     str_answer = n_split.reverse()
#     print(str_answer)
# solution(1234)
# 여기까진 str형으로 거꾸로 출력
# 여기서 int형으로 바꿔야 통과


# 문제2
# def solution(n):
#     # n을 한자리씩 쪼갠다
#     n_split = str(n)
#     # print(len(n_split))
#     print(n_split)
#     arr =[]
#     for i in range(len(n_split)):
#         print(i)
#         print(n_split[i])
#         arr.append(n_split[i])
#     # 쪼갠 n을 뒤에서부터 하나씩 꺼내어 앞자리에 넣는다
#     arr_reverse = arr[::-1]
#     print(arr_reverse)
#     # 쪼갠 n을 다시 int형으로 바꾼다
#     answer = []
#     for j in arr_reverse:
#         j = int(j)
#         print(j)
#         answer.append(j)
#     # 쪼갠 n을 answer에 넣는다
#     print(answer)
#     return answer

# 문제3
def solution(n):
    answer=[]
    while (n>0):
        # n을 10으로 나눈 나머지
        reminder = n % 10
        print(reminder)#4
        answer.append(reminder)
        # n을 10으로 나눈 몫
        n = n // 10
        print(n)#123
        # break를 걸면 마지막 글자만 출력됨, 안걸면 계속 반복되므로 전체 숫자를 input
    return answer

solution(123456)