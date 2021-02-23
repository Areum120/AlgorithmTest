

package ProgrammersTest;


/*
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
n은 0 이상 3000이하인 정수입니다.
*/
public class Solution4 {

	
	public static int solution(int n) {
	
	int answer = 0;
	//int[] a = {1,2,3,4,5,6,7,8,9,10};
	int[] a = new int[3000];//배열 사이즈 생성
				
	for(int i=0; i<3000; i++) {
		a[i]= i+1; //1. 1~3000이하의 수 생성한 정수 배열 안에 넣기 3.랜덤으로 생성 안해도 됨
		System.out.println(a[i]+",");
		}
		for(int j=0; j<a.length; j++) {//반복문
			//System.out.println(a[j]);
			if(n%a[j]==0) {// 약수 구하기 : a 배열 안의 모든 요소를 꺼내어 n으로 나누어떨어졌을 때 
				System.out.println(a[j]);
				answer+=a[j];//구한 약수를 모두 더한 값
			}
		}
	
	return answer;
	
	}
	
	public static void main(String[] args) {
		solution(20);
	}
	
	
}
	


