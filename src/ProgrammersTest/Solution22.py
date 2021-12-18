'''
K번째수
문제 설명
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열
commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때
나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.

입출력 예
array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

'''
def solution(array, command):
    answer = []
    for m in range(len(command)):
        print(m)#0,1,2 등 command의 길이
        print(command[m])
        #command 각 요소 길이는 3임
        numi = command[m][0]
        numj = command[m][1]
        numk = command[m][2]
        #i부터 j까지 자르기
        numi_j = array[numi-1:numj]
        numi_j.sort()#오름차순 정렬
        #k번째 수 출력
        numi_j_k = numi_j[numk-1]
        answer.append(numi_j_k)
    print(answer)
    return answer

    '''
    의사코드 작성 및 중첩리스트 i,j번째 요소 출력 연습
    
    i = command[0][0] and command[1][0] and command[2][0]->2,4,1
    j = command[0][1] and command[1][1] and command[2][1]->5,4,7
    k = command[0][2] and command[1][2] and command[2][2]->3,1,3
    for i in range(len(command)):
        # print(i)#0,1,2
        #for j in range(len(command[i])):
            # print(j)#0,1,2,0,1,2,0,1,2
            # print(i)#0,0,0,1,1,1,2,2,2
            # print(command[i])#[2, 5, 3],[2, 5, 3],[2, 5, 3],[4, 4, 1],[4, 4, 1],[4, 4, 1],[1, 7, 3],[1, 7, 3],[1, 7, 3]
            # print(command[j])#[2, 5, 3],[4, 4, 1],[1, 7, 3],[2, 5, 3],[4, 4, 1],[1, 7, 3],[2, 5, 3],[4, 4, 1],[1, 7, 3]
            # print(command[i][j])#2,5,3,4,4,1,1,7,3
            # print(command[j][i])#2,4,1,5,4,7,3,1,3
  # command의 i번째 숫자부터 j번째까지 자르기
    # array[i-1:j-1]
    # 오름차순 정렬
    # answer = command의 k번째 있는 수를 저장
    '''
array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# [i, j, k]
# i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수
# print(command[0][1]#첫번째 커맨드 요소 출력)
solution(array, command)

'''
 # 2,5,3만 출력해보는 연습
def solution(array, command):
    answer=[]
    for v in command:
        #print(v[0])
        i=v[0]
        j=v[1]
        k=v[2]
        numi_j = array[i-1:j]
        #print(numi_j)
        numi_j.sort()
        #print(numi_j)
        numi_j_k = numi_j[k-1]
        #print(numi_j_k)
        answer.append(numi_j_k)
'''