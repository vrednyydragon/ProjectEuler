class Problem002
{
	public static void main(String[] args) {
		
		/*int sum=0;
		
			while (sum<4000000000) {
			  sum+=1 ;
			  if ((sum%2)==0) {
				System.out.println("Сумма четных чисел Фибоначчи : " + sum);
				}
			}  */

		int n0 = 1;
		int n1 = 1;
		int n2;
		long sum=0;
		//System.out.print(n0+" "+n1+" ");
		for(int i = 3; i < 4000000; i++){
			n2=n0+n1;
			//System.out.print(n2+" ");
			n0=n1;
			n1=n2;
			if ((n2%2)==0) {
				sum+=n2;
				//System.out.println("Четное число: "+ n2);
			}
		}

		System.out.println("Сумма четных чисел: "+ sum);
	}
}

