'''
하샤드 수
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
입출력 예
arr	return
10	true
12	true
11	false
13	false
입출력 예 설명
입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.
'''


def solution(x):
    # 하샤드 수 : x의 자릿수 합으로 x가 나누어 떨어져야 함
    # ex) 18의 자릿수 합은 1+8 = 9, 18을 9로 나누었을 때 나누어 떨어지므로 하샤드 수임
    # ex) 225의 자릿수 합은 2+2+5
    x_list = list(str(x))#문자+리스트형 변환
    print(x_list)#['2','2','5']
    all_num=0
    for i in range(len(x_list)):
        print(i)#0,1,2
        print(x_list[i])#2, 2, 5
        all_num = all_num + int(x_list[i])
    print(all_num)
    if x % all_num==0:
        answer = True
        print(answer)
        return answer
    else:
        answer = False
        print(answer)
        return answer
solution(225)

#10, 12 : 하샤드 수 True
#11, 13 : 하샤드 수 False