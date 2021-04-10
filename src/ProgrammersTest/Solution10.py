'''문제 설명
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
예를 들면,
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

입출력 예
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]
입출력 예 설명
입출력 예 #1,2
문제의 예시와 같습니다.


방법3
def solution (arr):
    answer = []
    length = len(arr)#들어온 파라미터값 세기
    for i in range(0, length):#전체 범위 값 중에서 하나씩 세기
        answer.append(arr[i])#전체 값 넣기
        # print(answer)
        for j in range(i+1, length):#더한 값 루프문
            # if arr[i] == arr[i+1]:  # 인덱스의 숫자 같은지 확인
            answer.remove(arr[i])# 같은 숫자를 arr에서 앞에서부터 제거
                # break
    print(answer)
    return answer
문제 앞에서 1을 제거하면서 for문으로 계속해서 제거해버림

def solution(arr):
    answer = []
    length = len(arr)#들어온 파라미터값 세기
    for j in range(0, length):#전체 범위 값 중에서 하나씩 세기
        answer.append(arr[j])#전체 값 넣기
        # print(answer)
        for i in range(j+1, length):#더한 값 루프문
            if arr[j] == arr[j+1]:# 인덱스의 숫자 같은지 확인
                print(arr[j])
                answer.pop()#뒤에서부터 제거(문제가 앞에서 제거하는 것이 문제이므로)
                break #break을 안하면 IndexError: pop from empty list 발생
            #range(0, length)1,1,1,4,4,1,1를 4번씩 돔
            #in answer경우, 2,2,3,2,3,4,2,3,4
            #answer.remove(arr[i])

    print(answer)
    return answer


문제 속도가 느려서 효율이 떨어짐 70점->list comprehension
'''
def solution(arr):
    a = [j for j in arr]# 1,2,3,3,0,1,1
    # c = [i for i in arr if a[i] == a[i + 1]] #0
    # b = [i for i in arr if a[i]==a[i+1] or a.remove(i)] # 1,3,1
    d = [i for i in range(len(arr[i]-1))]
    print(d)

    return d
a1 = [1, 1, 3, 3, 0, 1, 1]
solution(a1)


'''방법1 뒤에 1이 또 붙을 때 제거되지 않아야 함
from collections import OrderedDict

def solution(arr):
    answer = list(OrderedDict.fromkeys(arr))
    return answer

방법2 뒤에 1이 또 붙을 때 제거되지 않아야 함
def solution(arr):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    print(answer)
    return answer

1. 중복제거 - set을 이용하면 중복은 제거되나 순서가 뒤죽박죽
2. 순서 유지
for문 not in으로 할 경우 뒤에 똑같은 숫자가 와도 나타나지 않음'''