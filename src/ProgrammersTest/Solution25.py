'''
모의고사
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, / 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,/ 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,/ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.

'''

def solution(answers):
    # 정답지 갯수
    n = (len(answers))
    print(n)
    supoja1 = list(range(1, 6))
    # (답안지갯수*몫)+나머지
    supoja1_list = supoja1* (n//5)+supoja1[0:(n%5)]#몫을 곱하면 int형 변환 안해도 됨
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja2_list = supoja2* (n//8)+supoja2[0:(n%8)]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supoja3_list = supoja3* (n//10)+supoja3[0:(n%10)]
    print(len(supoja1_list))
    print(len(supoja2_list))
    print(len(supoja3_list))

#   겹치는 원소 찾기
#   zip함수를 쓰면 여러 그룹 데이터를 한번의 for문으로 2개 인자를 넘겨서 병렬처리 가능
#   방법1
#     same_list=[]
#     for i, j in zip(supoja1, answers):
#         if i==j:
#             print(same_list.append(i))
#     print(same_list)
#   방법2
    same1 = [i for i, j in zip(supoja1_list, answers) if i==j]
    print(same1)
    print(len(same1))

    same2 = [i for i, j in zip(supoja2_list, answers) if i == j]
    print(same2)
    print(len(same2))

    same3 = [i for i, j in zip(supoja3_list, answers) if i == j]
    print(same3)
    print(len(same3))

    print("========정답은=======")
    # 정답 갯수 비교 출력
    if len(same1)>len(same2) and len(same1)>len(same3):
        answer=[1]
        print(answer)
        return answer
    elif len(same2)>len(same1) and len(same2)>len(same3):
        answer=[2]
        print(answer)
        return answer
    elif len(same3)>len(same1) and len(same3)>len(same2):
        answer=[3]
        print(answer)
        return answer
    elif len(same1)==len(same2) and len(same1)>len(same3):
        answer=[1,2]
        print(answer)
        return answer
    elif len(same2)==len(same3) and len(same2)>len(same1):
        answer=[2,3]
        print(answer)
        return answer
    elif len(same1)==len(same3) and len(same1)>len(same2):
        answer=[1,3]
        print(answer)
        return answer
    elif len(same1)==len(same2) and len(same2)==len(same3):
        answer=[1, 2, 3]
        print(answer)
        return answer


# 답안지 생성
answers = [3,2,3,1,2]*100
# print(answers)
solution(answers)

