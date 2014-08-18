public class Problem7 {

	public static void main(String v[]) {
		double start = System.nanoTime();
		int num = 0, i = 0;
		System.out.println("10001 Prime number");

		while (num <= 10000) {
			if (is_prime(i) == true) {
				num += 1;
			}
			i++;
		}
		System.out.println(i - 1);
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}

	static boolean is_prime(int n) {
		int sqr = 0, i;
		if (n == 2) {
			return true;
		}

		else if (n % 2 == 0 || n <= 1) {
			return false;
		}

		else {
			sqr = (int) Math.sqrt(n) + 1;
			for (i = 3; i < sqr; i = i + 2) {
				if (n % i == 0) {
					return false;
				}
			}
			return true;
		}
	}
}
