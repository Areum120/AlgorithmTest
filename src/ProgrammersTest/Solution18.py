
'''
정수 내림차순으로 배치하기

함수 solution은 정수 n을 매개변수로 입력받습니다.
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.

n은 1이상 8000000000 이하인 자연수입니다.
'''

def solution(n):
    num_list = []
    for i in str(n):# 문자열 변환후 각 숫자 콤마로 분리 1,1,8,3,7,2
        num_list.append(i)# 리스트에 넣기
    print(num_list)
    numreverse_list = sorted(num_list,reverse=True) # 리스트 안의 숫자 내림차순 정렬 sorted(A_list, reverse=True)
    print(numreverse_list)# A_list([8,7,3,2,1,1])
    answer = ''.join(numreverse_list)# 콤마 제거하여 붙이기
    answer = int(answer)#정수변환
    print(answer)
    # 리스트 안의 요소 return
    return answer

    # for j in numreverse_list:
    #     deletecomma = j.replace(',','')# 콤마 제거한 리스트 요소 1개씩 출력
    #     deletecomma_int = int(deletecomma)#정수변환
    #     print(deletecomma_int)

solution(118372)