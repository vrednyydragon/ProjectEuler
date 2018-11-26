class Problem004
{
	public static void main(String[] args) {
		
		// int ProdLench=5;
		// int min = Integer.parseInt("1".lpad("0",ProdLench-1));
		// int max = Integer.parseInt("9".lpad("9",ProdLench-1));

		for (int i=999; i>99; --i)
		{
			for (int k=999; k>99; --k)
			{
				//int result = i * k;
				//int result = Integer.toString (result);
				String result = Integer.toString (i * k);
				int strlength = result.length() ;
				//
				boolean FlagEq=true;
				//System.out.println( result);
				for (int n = 0; n<Math.round(strlength/2); ++n)
				{
					if(FlagEq)
					{
						//System.out.println( result.substring( n,n+1 ) + " = " + result.substring(strlength-n-1,strlength-n));
						FlagEq = result.substring( n,n+1 ).equals(result.substring(strlength-n-1,strlength-n));
					}
					else
						break;

					//System.out.print( result.substring( n ) ) 

				}
				if(FlagEq)
					System.out.println( result + " - Polindrome");				
				//если длина строки четная (6) то делим строку на 2
				// если длинна строки не четная (5) то от длинны троки отнимаем 1 и потом делим на 2
				// 
				
			}
		}
	}
}