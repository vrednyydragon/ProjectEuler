class Problem001_2
{
	public static void main(String[] args) {
		int iterator=0 ;
		int sum = 0 ;
		do 
		{
			if ((iterator%3==0) || (iterator%5==0)){
				System.out.println("������� 3 ��� 5: " + iterator ) ;
				sum+=iterator ;
			}
			iterator++ ;
		}
		while (iterator<1000) ;
		System.out.println("����� ����� ������� 3 � 5 : " + sum);
	}
}