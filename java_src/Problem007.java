import java.math.*;


class Problem007
{
	public static void main(String[] args) {
		Integer [] simple_numb = new Integer[500000];
		simple_numb[0] = new Integer(2);
		int arrind=0;
		int i=0;
		int lim=10001;
		//for (int i=0; i<500000; i++)
		while(true)
		{
			i++;
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
			if (arrind==lim-1)
			{
				break;
			}
		}
		System.out.println(" simple_numb "+ simple_numb[lim-1]);

	}
}