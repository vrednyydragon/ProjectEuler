class Problem001
{
	//https://projecteuler.net/problem=1
	public static void main(String[] args) {
		int sum=0;

		for (int i=1; i <= 1000 ; ++i ) {
			if(i==996)
				continue;//break;
			if ((i%3)==0 || (i%5)==0) {
				sum += i;
				System.out.println("???????? ?? 3 ??? 5 : " + i);
			}
		}
		System.out.println("????? ????????? ?? 3 ??? 5 : " + sum);
	}
}