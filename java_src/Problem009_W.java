import java.time.*;

class Problem009_W
{
	public static void main(String[] args) {
		LocalDateTime date = LocalDateTime.now() ;
		int limitation=10;
		long iterations1=0L;
		long iterations2=0L;
		System.out.println( "\nСейчас 1 " + date.now() );
		for(int counter1 =0 ; counter1 < limitation ; counter1++ )
		{
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
						iterations1++;
						a++;
						sum=a+b+c;
						if ((a < b) && (b < c) && (((a*a)+(b*b))==(c*c))&& (sum==lim))
						{
							break;
						}
					}
					a=0;
					if(sum==lim)
						break;
				}
				b=0;
				if(sum==lim)
					break;
			}
		}
		System.out.println( "\nСейчас 2 " + date.now() );
		System.out.println( "iterations1 = " + iterations1);
		for(int counter2 =0 ; counter2 < limitation ; counter2++ )
		{
			int c=0;
			int sum=0;
			int lim = 10000;

			for (int a=0; a<lim; a++)
			{
				for (int b=0; b<lim; b++)
				{			
					sum=a+b+c;
					if ((a < b) && (b < c) && (((a*a)+(b*b))==(c*c))&& (sum==lim))
					{
						break;
					}
				}
				 if(sum==lim)
				 	break; 
			}		
		}
		System.out.println( "\nСейчас 3 " + date.now() );
		System.out.println( "iterations2 = " + iterations2);
	}
}