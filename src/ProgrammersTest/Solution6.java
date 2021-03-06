
package ProgrammersTest;

import java.util.Arrays;

/*
 * 함수 solution은 정수 x와 자연수 n을 입력 받아, 
 * x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
 * 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
 * 
 * 제한 조건
	x는 -10000000 이상, 10000000 이하인 정수입니다.
	n은 1000 이하인 자연수입니다.
	
	입출력 예
	x	n	answer
	2	5	[2,4,6,8,10]
	4	3	[4,8,12]
	-4	2	[-4, -8]
 * 
 */

class Solution6 {
    public long[] solution(int x, int n) {//배열
        
    	//long[] answer = {};
        
    	long[] num = new long[n];//배열 사이즈 생성
    	
        for(int i=0; i<n; i++) {//n의 크기만큼  i 증가 
        	num[i]=(i+1)*x;//i는 1,2,3,4, n개만큼 거지므로 x를 곱한 수만큼 증가
        }
        //x, 2x, 3x, 4x ->for문 앞에 붙은 숫자 증가 
		return num;
        
    }
    
   public static void main(String[] args) {
	
	   Solution6 s6 = new Solution6();
	   
	   System.out.println(Arrays.toString(s6.solution(2, 2)));//배열의 주소값이 출력되므로 Arrays.toString()메서드 사용
	   //int=>long은 작은 것에서 큰 데이터로 자동형변환 가능
} 
   
}


