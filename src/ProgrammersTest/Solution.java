package ProgrammersTest;

public class Solution {
	/*문제 설명
	길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

	제한 조건
	n은 길이 10,000이하인 자연수입니다.
	*/
	public static String Solution(int n) {
		String answer ="";

//		첫번째 방법		
//		String str2 = new String(new char[10000]).replace("\0", "수박"); //"수박"문자열 10000번 반복하기
//		System.out.println(str2.substring(0, n));//처음부터 n-1까지의 문자열 출력하기

		//2번째 방법
		for(int i = 0; i<n; i++) {
			if(i%2==1) {//i가 홀수번째
				answer += "박";
			}else {//i가 짝수번째
				answer += "수";//i는 0부터 시작하기 때문에 "수"부터 시작 
			}
		}
		return answer;
	}
	
	public static void main(String[] args) {
		System.out.println(Solution(3));//test출력
	}
}
//3번째 방법->1번째 방법에서 진화
/*
public class WaterMelon {
public String watermelon(int n){

    return new String(new char [n/2+1]).replace("\0", "수박").substring(0,n);
}//n/2+1->길이는 1부터 시작 

// 실행을 위한 테스트코드입니다.
public static void  main(String[] args){
    WaterMelon wm = new WaterMelon();
    System.out.println("n이 3인 경우: " + wm.watermelon(3));
    System.out.println("n이 4인 경우: " + wm.watermelon(4));
}
}
*/