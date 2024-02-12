package practice;
import java.util.Scanner;


public class UniqueProblem {
	public static void UniqueNumber()
	{
		Scanner input = new Scanner(System.in);
		int numberOfInputs = input.nextInt();
		for(int i=1; i<=numberOfInputs;i++)
		{
			int uniqueNumber = input.nextInt();
			System.out.println(uniqueNumber/6);
		}
		System.out.println("End!");
	}

}
