package ProgrammersTest;

public class Solution {
	/*���� ����
	���̰� n�̰�, ���ڼ��ڼ��ڼ�....�� ���� ������ �����ϴ� ���ڿ��� �����ϴ� �Լ�, solution�� �ϼ��ϼ���. ������� n�� 4�̸� ���ڼ����� �����ϰ� 3�̶�� ���ڼ��� �����ϸ� �˴ϴ�.

	���� ����
	n�� ���� 10,000������ �ڿ����Դϴ�.
	*/
	public static String Solution(int n) {
		String answer ="";

//		ù��° ���		
//		String str2 = new String(new char[10000]).replace("\0", "����"); //"����"���ڿ� 10000�� �ݺ��ϱ�
//		System.out.println(str2.substring(0, n));//ó������ n-1������ ���ڿ� ����ϱ�

		//2��° ���
		for(int i = 0; i<n; i++) {
			if(i%2==1) {//i�� Ȧ����°
				answer += "��";
			}else {//i�� ¦����°
				answer += "��";//i�� 0���� �����ϱ� ������ "��"���� ���� 
			}
		}
		return answer;
	}
	
	public static void main(String[] args) {
		System.out.println(Solution(3));//test���
	}
}
//3��° ���->1��° ������� ��ȭ
/*
public class WaterMelon {
public String watermelon(int n){

    return new String(new char [n/2+1]).replace("\0", "����").substring(0,n);
}//n/2+1->���̴� 1���� ���� 

// ������ ���� �׽�Ʈ�ڵ��Դϴ�.
public static void  main(String[] args){
    WaterMelon wm = new WaterMelon();
    System.out.println("n�� 3�� ���: " + wm.watermelon(3));
    System.out.println("n�� 4�� ���: " + wm.watermelon(4));
}
}
*/