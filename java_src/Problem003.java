import java.math.*;


class Problem003
{
	public static void main(String[] args) {
		Integer [] simple_numb = new Integer[500000];
		simple_numb[0] = new Integer(2);
		int arrind=0;
		for (int i=0; i<13195; i++)
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
						break;
					}
				}
			}
		}
		long del = 600851475143L;

		while(true)
		{
			for(int i=0; i<=arrind; i++)
			{
				if( del % simple_numb[i] == 0)
				{
					del = del/simple_numb[i];
					System.out.println("simple_numb " + simple_numb[i] + " del " + del);
					break;
				}
			}
			if (del == 1)
				break;
		}
	}
}