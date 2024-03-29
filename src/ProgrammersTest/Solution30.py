'''
체육복
문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
학생들의 번호는 체격 순으로 매겨져 있어,
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
입출력 예 설명
예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
'''

# 테스트 20개 중에 3개는 틀림

def solution(n, lost, reserve):
    # reserve 요소 하나씩 꺼내어 앞, 뒤 숫자가 lost의 각 요소와 일치하는 갯수 반환
    # 일치하는 갯수가 n보다 같거나 크면 return n
    # 일치하는 갯수가 n보다 작으면 일치하는 갯수 반환
    # 문제 lost에 2,4 reserve에 3이 있을 때 3은 2에게 빌려줄수도 4에게 빌려줄수도 있음
    # reserve학생이 체육복 도난당했을 경우
    # lost와 reserve에 같이 들어갈 수 있음
    # 만약 lost와 reserve에 중복이 있으면 lost와 reserve에서 동시에 제외해야함, 본인은 입을 수 있음
    inter_num = list(set(lost) & set(reserve))#reserve와 lost에 동시에 들어갈 경우
    print(inter_num)
    for i in inter_num:#lost에서 삭제
        lost.remove(i)
    for i in inter_num:#reserve에서 삭제
        reserve.remove(i)
    Pe_Student_Num =[]
    for i in reserve:
        for j in lost:
            print(i, j)
            if i-1 == j: #앞번호와 일치하는 경우
                Pe_Student_Num.append(i)#값넣기
            elif i+1 == j:#앞번호도 일치하고 뒷번호도 일치할 경우
                Pe_Student_Num.append(i)#값 넣기
    answer = list(set(Pe_Student_Num))#중복제거

    print(answer)
    if n - len(lost) + len(answer) >= n:
        return n
    else:
        return n - len(lost) + len(answer)#전체 학생 수 - 체육복 잃어버린 학생 수 - 여벌 체육복 빌려줄 수 있는 학생 수

n = 3
lost = [1, 2, 3]
reserve = [1, 4, 5]
print(solution(n, lost, reserve))

