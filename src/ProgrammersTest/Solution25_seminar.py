'''
https://programmers.co.kr/learn/courses/30/lessons/42840

모의고사
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

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

'''
문제 분석하기

1. 정답지와 수포자의 답안지가 있다.
2. 수포자 3명은 각자 다른 답안지를 제출한다.
3. 수포자는 각자 정답을 찍는 방식이 정해져 있다. 

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

4. 문제의 정답은 1,2,3,4,5 중에 하나다.
5. 가장 높은 점수를 가진사람을 리턴한다. ex) 수포자 1이면 return [1]
6. 각자 찍은 답안지와 정답지와 비교하여 문제를 많이 많이 맞출수록 높은 점수를 가진다.
정답지 : [1,2,3,4,5,1,2,3,4,5]
수포자1 : [1,2,3,4,5,1,2,3,4,5]
수포자2: [2,1,2,3,2,4,2,5,2,1]
수포자3: [3,3,1,1,2,2,4,4,5,5]

7. 1명이 최고로 높은 점수를 받을수도, 2명이 동점을 가질수도, 3명이 동점을 가질 수도 있다.
8. 시험지는 1문제부터 10000문제까지 출제될 수 있다.
9. 높은 점수를 가진 사람이 여러명일 경우 오름차순으로 출력 ex) [1],[2],[3]

'''

'''
의사코드 작성하기

1. 정답지를 생성한다.
2. 정답지 갯수를 입력받아 = 수포자들의 답안지 갯수를 맞춘다.
3. 수포자들의 찍는 방식을 로직으로 만든다.
4. 정답지와 수포자들의 답안지를 비교하여 순서를 맞춘 개수를 집계한다.
5. 가장 많은 갯수의 순서가 일치 = 가장 높은 점수 
6. 가장 높은 점수의 수포자를 return한다.
'''

answers=[1,2,3,4,5]*2
# print(answers)

# supoja1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] #5
# supoja2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] #8
# supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10

def solution(answers):
    n = len(answers)
#   각 반복되는 정수 세트가 몇번 곱해져야 n개가 될까?
#   supoja1 -> 5x = n
#   x = n/5
#   supoja2 -> 8x = n
#   x = n/8
#   supoja3 -> 10x = n
#   x = n/10

# n = 11개일 때
# 딱 나누어 떨어지지 않는 경우? 실수x , 몫 + 나머지
# supoja1 -> x = 11/5 -> 정수여야 하므로 5개의 정수가 2번 반복, 하지만 n개와 갯수가 같아야 하므로 나머지를 더해야 한다
# 즉 supoja1 * 몫 + 나머지

    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]

    supoja1_list = supoja1 * (n // len(supoja1)) + supoja1[:n % len(supoja1)]
    supoja2_list = supoja2 * (n // len(supoja2)) + supoja2[:n % len(supoja2)]
    supoja3_list = supoja3 * (n // len(supoja3)) + supoja3[:n % len(supoja3)]

    # print(supoja1_list)
    # print(supoja2_list)
    # print(supoja3_list)

# 정답지와 답안지 비교

    #   zip함수를 쓰면 여러 그룹 데이터를 한번의 for문으로 2개 인자를 넘겨서 병렬처리 가능
    #   방법1
    #     same_list=[]
    #     for i, j in zip(supoja1, answers):
    #         if i==j:
    #             print(same_list.append(i))
    #     print(same_list)

    same1 = [i for i, j in zip(supoja1_list, answers) if i == j]
    print(same1)

    same2 = [i for i, j in zip(supoja2_list, answers) if i==j]
    print(same2)

    same3 = [i for i, j in zip(supoja3_list, answers) if i==j]
    print(same3)

# 일치하는 갯수 비교하여 가장 높은 점수 return

    if len(same1) > len(same2) and len(same1) > len(same3):
        return [1]
    elif len(same2) > len(same1) and len(same2) > len(same3):
        return [2]
    elif len(same3) > len(same1) and len(same3) > len(same2):
        return [3]
    elif len(same1) == len(same2) and len(same1) > len(same3):
        return [1, 2]
    elif len(same2) == len(same3) and len(same2) > len(same1):
        return [2, 3]
    elif len(same1) == len(same3) and len(same1) > len(same2):
        return [1, 3]
    elif len(same1) == len(same2) and len(same2) == len(same3):
        return [1, 2, 3]


solution(answers)




