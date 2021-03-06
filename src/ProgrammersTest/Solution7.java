
package ProgrammersTest;

import java.util.Arrays;

/*
 *정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요. 
 * 제한 조건
	arr은 길이 1 이상, 100 이하인 배열입니다.
	arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
	
	입출력 예
	arr			return
	[1,2,3,4]	2.5
	[5,5]		5
 * 
 */

class Solution7 {
    public double solution(int[] arr) {
    	
        double avg = 0;//평균이 실수로 반환될 수 있으므로 
        int sum = 0;
        
        int[] arr1 = new int[100];//배열 사이즈 생성
        
        
        for(int i=0; i<arr.length; i++) {
        	sum+=arr[i];
        }
        avg = sum/(double)arr.length;//(double)표시를 안해주면 정수로만 계산됨
        return avg;
    }
    
   public static void main(String[] args) {
	
	   Solution7 s7 = new Solution7();
	   
	   int[] arr = {1,2,3,4};
	   	
	   System.out.println(s7.solution(arr));

}

}


