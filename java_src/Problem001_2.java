class Problem001_2
{
	public static void main(String[] args) {
		int iterator=0 ;
		int sum = 0 ;
		do 
		{
			if ((iterator%3==0) || (iterator%5==0)){
				System.out.println("кратное 3 или 5: " + iterator ) ;
				sum+=iterator ;
			}
			iterator++ ;
		}
		while (iterator<1000) ;
		System.out.println("сумма чисел кратных 3 и 5 : " + sum);
	}
}