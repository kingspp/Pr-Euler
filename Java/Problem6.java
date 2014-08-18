public class Problem6 {

	public static void main(String v[]) {
		double start = System.nanoTime();
		int sum = 0, sum1 = 0;
		System.out
				.println("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum");
		for (int i = 1; i < 101; i++) {
			sum += i;
			sum1 += Math.pow(i, 2);

		}
		sum = (int) Math.pow(sum, 2);
		System.out.println(sum - sum1);
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}
}
