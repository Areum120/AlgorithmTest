
package ProgrammersTest;

import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 *대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
 *'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
 *단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
 *예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
 *제한사항
 *문자열 s의 길이 : 50 이하의 자연수
 *문자열 s는 알파벳으로만 이루어져 있습니다.
	
	입출력 		예
	s			answer
	"pPoooyY"	true
	"Pyy"		false
 * 
 */

class Solution9 {
	  		boolean Solution9(String s) {
	  			
	  			
	  			int pcnt = 0;
	  			int ycnt = 0;
	  			//문자열 찾기 contains, indexOf, matches
	  			//if s에서 p를 찾고 개수 세기== s에서 y를 찾고 개수 세기 return true; 
	  			//else if s의 p의 개수 !== s의 y의 개수 return false;
	  			//else p,y 하나도 없는 경우 return true;
	  			
	  			//방법 1
	  			
	  			//s = s.toLowerCase();//대문자 받으면 모두 소문자로 변환
	  			for(int i=0; i<s.length(); i++) {
	  				if(s.charAt(i) == 'p'||s.charAt(i)=='P') {//""가 아니라 ''로 써야 함 한글자이기 때문
	  					pcnt++;
	  				}else if(s.charAt(i) == 'y'||s.charAt(i)=='Y') {
	  					ycnt++;
	  				}
	  			}
	  			System.out.println("p(P)의 총 갯수는"+pcnt+"개"+ "y(Y)의 총 갯수는"+ycnt+"개 입니다");
	  			if(pcnt==ycnt) {
	  				return true;
	  			}else if(pcnt==0&&ycnt==0) {
	  				return true;
	  			}else return false;
	  			
	  			
	  			//방법 2. 패턴매칭 그러나 대문자는 어떻게?
	  			
//	  			Pattern p = Pattern.compile("p");
//	  			Matcher m = p.matcher(s);
//	  			
//	  			Pattern y = Pattern.compile("y");
//	  			Matcher m1 = y.matcher(s);
//	  			
//	  			for(int i =0; m1.find(i); i=m1.end()) {
//	  				ycnt++;
//	  			}
//	  			for(int i=0; m.find(i); i=m.end()) {
//	  				pcnt++;
//	  			}
//	  			if (pcnt==ycnt) {
//	  				return true;
//	  			}else if (pcnt==0&&ycnt==0) {
//	  				return true;
//	  			}else return false;
	  		
	  		}
    
   public static void main(String[] args) {
	
	   Solution9 s9 = new Solution9();

	
	   System.out.println(s9.Solution9("pdPsryy"));

}

}


