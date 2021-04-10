'''문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.

예시
입력
5 3

출력
*****
*****
*****
practice
참고문법 : https://dojang.io/mod/page/view.php?id=2259
def make_star(n,m):
    for i in range(m):
        for j in range(n):
             print('*', sep='', end='')
        print('*', sep='')


make_star(5, 3)

a: 입력받은 정수숫자만큼 '*'갯수를 출력한다
b: a를 3번 반복 출력한다:


a,b =  map(int, input().strip().split(' ')) # 입력받은 값을 정수로 변환, strip()은 공백제거, split()은 문자열 공백으로 나누기
print(a+b)'''

#참고문법: https://inma.tistory.com/129
a,b = map(int, input('숫자를 입력하세요:').strip().split())
'''숫자를 입력하세요: 1 2 3
1)방법
for i in range(b):
    print('*'*a)
2)방법'''
answer = ('*'*a+'\n')*b
print(answer)
