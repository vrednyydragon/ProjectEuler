import java.math.*;


class Problem010
{
	public static void main(String[] args) {
		Integer [] simple_numb = new Integer[5000000];
		simple_numb[0] = new Integer(2);
		int arrind=0;
		long sum = (long)simple_numb[0];
		long lim = 2000000L;

		for (int i=0; i<=lim; i++)
		{
			if ((i>0) && (i%2>0))
			{
				for(int k=0; k<=arrind;k++)
				{
					if((i % simple_numb[k] == 0) || (i <= simple_numb[k]))
					{
						break;
					}
					if(k == arrind)
					{
						// System.out.println("i : " + i + " k : " + k + " arrind : " + arrind + " simple_numb "+ simple_numb[k]);
						arrind++;
						simple_numb[arrind] = new Integer(i);

						sum+=simple_numb[arrind];
						// if (i==(lim+1))
						// {
						// 	System.out.println("sum : " + sum);
						// }

						break;
					}
				}
			}
		}
		System.out.println("sum : " + sum);
		// long del = 2000000L;



		// while(true)
		// {
		// 	for(int i=0; i<=arrind; i++)
		// 	{
		// 		if( del % simple_numb[i] == 0)
		// 		{
		// 			del = del/simple_numb[i];
		// 			System.out.println("simple_numb " + simple_numb[i] + " del " + del);
		// 			break;
		// 		}
		// 	}
		// 	if (del == 1)
		// 		break;
		// }
	}
}