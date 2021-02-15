package codingTestPractice;

public class Solution {
	public long solution(int a, int b){
		int i;
		long sum;
		if(a<b) {
			for(i=a, sum=0; i<=b; i++) {
				sum+=i;
			}
				
		}else {for(i=b, sum=0; i<=a; i++) {
			sum+=i;
			}
			
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
					}
				if(a==b) {//a와 b가 같을 때
					sum+=a;
				}else {
					sum+=b;
				}
					if(a<b) {//만약 a가 b보다 작을 때
						for(i=0; b>-1000000; b++) {
							for(i+=b; a<10000000; a++) {
								i+=a;
								sum+=i;
							}
					}
				}		
			}
			System.out.println("a부터 b사이의 더한 값은"+sum+"입니다.");
		}	
	
	}
	
		


//		for(a=-10000000+1, sum=0; a <10000000; a++) {
//			for(b=-10000000+1; b <10000000; b++ )
//			sum+=a;
//			}		



