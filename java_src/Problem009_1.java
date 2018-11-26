class Problem009_1
{
	public static void main(String[] args) {
		int a=0;
		int b=0;
		int c=0;
		int sum=0;
		int lim = 1000;

		for (int i=0; i<lim; i++)
		{
			c++;
			for (int n=0;n<lim ;n++ ) 
			{
				b++;
				for (int k=0;k<lim ;k++) 
				{
					a++;
				
					//System.out.println("a = "+a +" b = "+b +" c = "+c);

					sum=a+b+c;
					//System.out.println("sum = "+sum);
					if ((a < b) && (b < c) && (((a*a)+(b*b))==(c*c))&& (sum==lim))
					{
						System.out.println("--------------------------------------------------");
						System.out.println("a = "+a +" b = "+b +" c = "+c);
					 	System.out.println(sum);
					}
				}
				a=0;
			}
			b=0;
		}
	}
}