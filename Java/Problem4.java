public class Problem4 {

	public static void main(String v[]) {
		double start = System.nanoTime();
		int a = 999, b = 999, resf = 0, res;

		System.out.println("Palindrome -  Highest Triplets");

		while (a > 900) {
			while (b > 900) {
				res = a * b;
				if (palindrome(res) != 0) {
					if (res > resf) {
						resf = res;
						System.out.println("The product of " + a + "*" + b
								+ "=" + resf);
					}

				}
				b = b - 1;

			}
			b = 999;
			a = a - 1;
		}

		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}

	static int palindrome(int num) {
		int numr = 0, rev = 0;
		numr = num;

		while (num != 0) {
			rev = rev * 10 + num % 10;
			num /= 10;
		}
		if (numr == rev) {
			return numr;
		} else
			return 0;

	}
}
