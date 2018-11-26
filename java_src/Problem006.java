class Problem006
{
	public static void main(String[] args) {
		try
		{			
			long sumSQ = 0L ;
			long SQsum = 0L ;

			int lowerD = Integer.parseInt(args[0]);
			int maxD = Integer.parseInt(args[1]);

			for (int i=lowerD; i<=maxD; i++)
			{
				sumSQ+=(i*i);
				SQsum+=i;
			}
			SQsum=(SQsum*SQsum);

			System.out.println( " сумма квадратов :" + sumSQ);
			System.out.println( " квадрат суммы :" + SQsum);

			System.out.println( " разница сумм :" + (SQsum-sumSQ));
		}
		catch(Exception ex)
		{
			System.out.println( " Need params ");	
		}
	}
}