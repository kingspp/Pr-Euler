public class Problem1 {

	public static void main(String v[]) {
		double start = System.nanoTime();
		int num = 0;

		System.out.println("Find Multiples of 3 and 5");

		for (int i = 3; i < 1000; i++) {
			if (i % 3 == 0) {
				num += i;
			}
			if (i % 5 == 0) {
				num += i;
			}
		}
		System.out.println(num);
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}
}
