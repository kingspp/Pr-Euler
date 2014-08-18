public class Problem3 {

	public static void main(String v[]) {
		double start = System.nanoTime();
		double NUM = 600851475143.0;
		int root = (int) Math.sqrt(NUM);
		int pr = 0, fin = 0;
		System.out.println("Largest Prime Factor\n");

		for (int j = 2; j < root; j++) {
			pr = is_prime(j);
			if (pr != 0) {
				if (NUM % pr == 0) {
					fin = pr;
				}
			}
		}
		System.out.println(fin);

		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}

	static int is_prime(int n) {
		int sqr = 0, i;
		if (n == 2) {
			return 2;
		}

		else if (n % 2 == 0 || n <= 1) {
			return 0;
		}

		else {
			sqr = (int) Math.sqrt(n) + 1;
			for (i = 3; i < sqr; i = i + 2) {
				if (n % i == 0) {
					return 0;
				}
			}
			return n;
		}
	}
}
