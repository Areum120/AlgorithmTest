package codingTestPractice;

public class Solution {
	public long solution(int a, int b){
		int i;
		long sum;
		for(i=a, sum=0; i<=b; i++) {
			sum+=i;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		int a = 0;
		int b = 0;
		int i;
		long sum = 0;
		
		for(i=0; a>-10000000; a++) {
			for(i+=a; b<10000000; b++) {
				i+=b;
				sum+=i;
				for(i=0; b>-10000000; b++) {
					for(i+=b; a<10000000; a++) {
						i+=a;
						sum+=i;
					}
				}
						if(a==b) {
							sum+=a;
						}else {
							sum+=b;
						}
				}
			System.out.println("a부터 b사이의 더한 값은"+sum+"입니다.");	
		}	

	}
	
}		


//		for(a=-10000000+1, sum=0; a <10000000; a++) {
//			for(b=-10000000+1; b <10000000; b++ )
//			sum+=a;
//			}		



