
package ProgrammersTest;

import java.util.Arrays;

/*
 *정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
 *제한 조건
 *num은 int 범위의 정수입니다.
 *0은 짝수입니다.
	
	입출력 예
	num			return
	3			"Odd"
	4			"Even"
 * 
 */

class Solution8 {
	  public String solution(int num) {
	       
	        
	        if(num%2==0) {//짝수
	        	return "Even";
	        }else return "Odd";
    }
    
   public static void main(String[] args) {
	
	   Solution8 s8 = new Solution8();
	   

	   System.out.println(s8.solution(4));

}

}


