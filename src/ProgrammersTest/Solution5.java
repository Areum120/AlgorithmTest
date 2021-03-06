
package ProgrammersTest;

/*
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
  ex) s="abcde", return="c"
s는 길이가 1 이상, 100이하인 스트링입니다.
*/
public class Solution5 {

	public static String solution(String s) {
	
	String answer = "";//가운데 반환 글자
	
		if(s.length()%2==0) {//가 짝수이면 가운데 2글자 반환 
		System.out.println(s.substring(s.length()/2-1, s.length()/2+1));//s의 인덱스로 접근하여 substring 몫을 구한 뒤 4/2= 2, 6/2= 3, 즉 몫-1, 몫
		}else //홀수이면 가운데 1글자 반환
		System.out.println(s.charAt(s.length()/2));//s의 인덱스로 접근하여 몫을 구한 뒤 +1위치 글자 반환 5/2=2, 7/2=3, 9/2=4

	return answer;
	}
	
	public static void main(String[] args) {
		
		solution("abcdef");

	}
	
	
}
	


