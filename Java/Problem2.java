public class Problem2 {
	public static void main(String v[]) {
		double start = System.nanoTime();

		System.out.println("Fibonacci Series");
		System.out.println(fib(0, 4000000));

		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}

	static int fib(int MIN, int MAX) {
		int even = 0, a = MIN, b = MIN + 1, i, t = 0;

		for (i = 0; i < MAX; i++) {
			t = a;
			a = b;
			b = t + b;

			if (b > MAX) {
				break;
			}
			if (b % 2 == 0) {
				even += b;
			}
			// System.out.println(b);
		}
		return even;
	}
}
