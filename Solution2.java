package codingTestPractice;

public class Solution2 {

	public static String solution(int n) {//외부에서 입력

//		String str = "수";//n이 1일 때 
//		String str2 = str+"박";//n이 2일 때
//		String str3 = str2+str;//n이 3일 때 
//		String str4 = str2+str2;//n이 4일 때 
//		String str5 = str4+str;
//		String str6 = str4+str2;
//		String str7 = str6+str;
//		String str8 = str6+str2;
		String answer = "";
		String str = "수";
		String str2 = "박";
		
//		String str = "수박";
//		String[] answer;
//		answer = str.split("");//배열에 한글자씩 저장하기
//	
//		for(int i =0; i<n; i++) {
//			answer[i] = Character.toString((str.charAt(i)));
//			System.out.println(answer[i]);
//		}
//		
//	

//		char c1 = str.charAt(0);
//		char c2 = str.charAt(1);
		
//		String str2 = new String(new char[str.length()]).replace("\0", str);

		
		for(int i =0; i<5; i++) {//i는 n이 될때까지 1씩 증가
			answer += str+str2;
			answer = answer;
			System.out.println(answer.substring(0, 3));
			//최종 출력값 문자열 길이는 10000이하이고, 1이상인 자연수 (n1<=10000 and n1>=1)
		}
		return answer;
	}


//		i = 1 -> "수" ,첫번째자리, 1개 출력
//		i = 2 -> "수박", 첫번째자리, 두번째자리, 2개 출력
//		i = 3 -> "수박수" 첫번째자리, 세번째자리, 3개 출력
	
		
//				
//		for(n=0; n<10000; n++) {
//			if(n%2==1) {
//				
//				System.out.println(a);//가 n번 반복
//			}else if(n%2==0){
//				System.out.println(b);
//			

//		
		//n=1-> a n=2 ->a+b n=3 ->a+b+a n=4->a+b+a+b
		//n++ 일수록 -> (a+b+a+
		
		
		//if 숫자 n/2 = 0이면 짝수이므로 boolean 문자열'박'을 return
		//숫자 n/2 = 1이면 홀수이므로  boolean 문자열 '수'를 return
		
		//for(홀수면 수+짝수면 박)n이 10000이 될 때까지 반복
		
	
	public static void main(String[] args) {
	
		solution(3);
		
	}
	
}

