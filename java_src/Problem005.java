class Problem005
{
	public static void main(String[] args) {
		try
		{			
			long small_numb = 0L ;
			int lowerD = Integer.parseInt(args[0]);
			int maxD = Integer.parseInt(args[1]);

			boolean flag = false;
			while(!flag)
			{
				small_numb++ ;
				for (int i=lowerD; i<=maxD; i++)
				{
					if (small_numb%i!=0)
					{
						break;
					}
					if(i == maxD)
						flag = true;
				}

				// if (flag)
				// {
				// 	System.out.println( " the smallest positive number :" + small_numb);
				// 	break;
				// }
			}
			System.out.println( " the smallest positive number :" + small_numb);
		}
		catch(Exception ex)
		{
			System.out.println( " Need params ");	
		}
	}
}