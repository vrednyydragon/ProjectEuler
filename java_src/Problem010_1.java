import java.math.*;


class Problem010_1
{
	public static void main(String[] args) {
		Integer [] simple_numb = new Integer[500000];
		simple_numb[0] = new Integer(2);
		int arrind=0;
		long sum = (long)simple_numb[0];
		long lim = 10L;
		System.out.println("i : 0 k : 0" + " arrind : " + arrind + " simple_numb "+ simple_numb[arrind]);
		for (int i=0; i<=(lim); i++)
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
						//System.out.println("arrind : " + arrind + " simple_numb "+ simple_numb[k]);
						arrind++;
						simple_numb[arrind] = new Integer(i);
						System.out.println("i : " + i + " k : " + k + " arrind : " + arrind + " simple_numb "+ simple_numb[arrind]);

						sum+=simple_numb[arrind];
						//if (i==(lim))
						//{
						//}

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