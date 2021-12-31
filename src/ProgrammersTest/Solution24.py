'''
문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
입출력 예
arr	divisor	return
[5, 9, 7, 10]	5	[5, 10]
[2, 36, 1, 3]	1	[1, 2, 3, 36]
[3,2,6]	10	[-1]
입출력 예 설명
입출력 예#1
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

입출력 예#2
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

입출력 예#3
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

'''

def solution(arr, divisor):
    # arr의 각 element : 자연수를 담은 배열, 길이 1 이상
    # divisor : 자연수
    # arr를 divisor로 나누어 떨어지는 수만 배열 반환
    # 오름차순 정렬
    # 나누어 떨어지지 않으면 -1 요소인 배열 반환
    answer = []
    for i in range(len(arr)):
        # print(i)#0,1,2,3
        # print(arr[i])#1,2,3,4
        if arr[i] % divisor==0:#divisor로 나누었을 때 나머지가 0 : 나누어 떨어지면
            answer.append(arr[i])#배열에 담기
        else:#모든 요소가 나누어떨어지지 않는다면
            answer.append(-1)#-1 요소 한개만 반환한다(여기선 for문 안에 있어서 -1이 4개가 들어감)
    answer.sort()#answer 배열의 오름차순 정렬
    # print(answer)
    # return answer
    for j in answer:
        print(j)
    # if -1 in answer:
    #     answer=[-1]#answer요소 중에 -1이 있으면 -1 한개만 반환한다.
    #     print(answer)
    #     return answer
    # else:
    #     print(answer)
    #     return answer

arr = [5, 9, 7, 10]
divisor = 5
solution(arr, divisor)