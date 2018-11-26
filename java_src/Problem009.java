class Problem009
{
	public static void main(String[] args) {
		double c=0;
		int sum=0;
		int lim = 10000;

		for (int a=0; a<lim; a++)
		{
			for (int b=0; b<lim; b++)
			{			
				c= Math.sqrt(Math.pow(a, 2)+ Math.pow(b,2));
				
				double src = c;//123.45;
				int res = (int)src; //целая часть
				double res2 = src - res; //дробная часть
			
				sum = a+b+(int)c;
			
				if (res2 == 0)
				{
					if ((a < b) && (b < c) && (sum==lim) )
					{
						System.out.println("a = "+a +" b = "+b +" c = "+c);
						System.out.println("условие выполнилось ");
						System.out.println(sum);
						break;
					}
				}
			}
			 if(sum==lim)
			 	break; 
		}		
	}
}