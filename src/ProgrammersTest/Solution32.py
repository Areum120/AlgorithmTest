'''

문제 설명
비밀지도
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다.
그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다.
다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로,
각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.

전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다.
각각 "지도 1"과 "지도 2"라고 하자.
지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다.->or
지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.->and
"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.

암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
secret map

네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.

입력 형식
입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

1 ≦ n ≦ 16
arr1, arr2는 길이 n인 정수 배열로 주어진다.
정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족한다.
출력 형식
원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

입출력 예제
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]
매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]

'''


def solution(n, arr1, arr2):
    # map1
    answer = []
    for k in range(len(arr1)):
        # print(arr1[i])
        binary = []
        while arr1[k]>0:#몫이 0이 될때까지
            div = arr1[k] // 2 #2로 나눈 몫
            mod = arr1[k] % 2 #2로 나눈 나머지
            binary.insert(0, mod)
            if div !=0:
                arr1[k] = div
            else:
                break
        # print(binary)
        # 전체 자릿수가 n개보다 작을 때 앞자리에 0이 빠지는 문제가 생김
        if len(binary) < n:#만약 n개보다 작으면
            while True:
                binary.insert(0,0)#0번째 순서에 0을 넣는다
                if len(binary) ==n:#요소 갯수가 n개가 될때까지
                    break#out
        # print('map1:', binary)
        answer.append(binary)
    print(answer)
    print('''\
        ''')

    # map2
    answer2=[]
    for i in range(len(arr2)):
        # print(arr1[i])
        binary2 = []
        while arr2[i]>0:#몫이 0이 될때까지
            div = arr2[i] // 2 #2로 나눈 몫
            mod = arr2[i] % 2 #2로 나눈 나머지
            binary2.insert(0, mod)
            if div !=0:
                arr2[i] = div
            else:
                break
        # print(binary2)
        # 전체 자릿수가 n개보다 작을 때 앞자리에 0이 빠지는 문제가 생김
        if len(binary2) < n:#만약 n개보다 작으면
            while True:
                binary2.insert(0,0)#0번째 순서에 0을 넣는다
                if len(binary2) ==n:#요소 갯수가 n개가 될때까지
                    break#out
        # print('map2:',binary2)
        answer2.append(binary2)

    print(answer2)

    # map1,2 겹치기
    # 두 2차원 리스트 비교: 행렬 더하기

    for s in range(len(answer)):
        for w in range(len(answer[0])):
            answer[s][w] += answer2[s][w]
    print(answer)

    # 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다.->or
    # 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.->and

    # final의 1은 #, 0은 공백으로 표시 11110->'#### '로 출력하기
    answer3=[]
    for b in answer:
        change_binary = []
        for r in b:
            print(r)
            if r >= 1:
                change_binary.append('#')
            else:
                change_binary.append(' ')
        print(change_binary)
        final = ''.join(map(str, change_binary))  # 리스트 요소를 모두 붙인다
        # print(final)
        answer3.append(final)
    print(answer3)
    return answer3

'''
value = arr1[i]#리스트 요소 출력
a = format(value, 'b')#내장함수 이진수 변환
print(a)
'''


# arr1 각 정수를 이진법으로 변환 ->벽"#" 1, 공백" " 0
# arr2  각 정수를 이진법으로 변환 ->벽"#" 1, 공백" " 0
# format(value, 'b')



n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)