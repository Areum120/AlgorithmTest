

package ProgrammersTest;

import java.util.Arrays;
/*String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 
김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. 
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
Kim은 반드시 seoul 안에 포함되어 있습니다.

*/
public class Solution3 {


	//출력이 아닌 반환하는 걸로 고치기 answer 없애기
	public String solution(String[] seoul) {
	
	String answer = "";

	String name = "Kim";
	//int x = Arrays.binarySearch(seoul, "kim");
	//Arrays 라이브러리 사용하여 1.배열 이름, 2.찾고자 하는 데이터 로 인덱스번호 찾기
	
	for(int i =0; i<seoul.length; i++) {
		if(name.equals(seoul[i])) {
			answer = "김서방은"+i+"에 있다";
		}
	}
	return answer;
	}
	
	public static void main(String[] args) {
	
	Solution3 s3 = new Solution3();	
	
	String[] seoul = {"Jane","Kim"};
	
	System.out.println(s3.solution(seoul));//배열 선언, 초기화
	
	}
	
	
}
	


