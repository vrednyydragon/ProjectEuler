class Problem001_1
{
	public static void main (String[] args) 
	{
		
		int sum=0;
		int iterator=0;
		
			while (sum<=1000) 
			{
			  sum+=1 ;
			  if ((sum%3)==0 || (sum%5)==0) {
			  	iterator+=sum;
				System.out.println("Число деленное на 3 или 5 : " + sum);
				}
			}
			System.out.println(" sum " + iterator);
			
	}
}