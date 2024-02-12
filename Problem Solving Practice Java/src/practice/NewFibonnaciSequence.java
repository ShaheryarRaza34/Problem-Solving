package practice;

public class NewFibonnaciSequence {
	public static int newFibonnaciSequence(int a , int b)
	{
		int firstNumber=a;
		int secondNumber=b;
		int newNumber;
		int count=2;
		boolean flag= false;
		while(flag!=true)
		{
				newNumber=firstNumber+secondNumber;
				if(newNumber>9)
				{
					newNumber=newNumber%10;
				}
				firstNumber=secondNumber;
				secondNumber=newNumber;
				count++;
				if(firstNumber==a && secondNumber==b)
				{
					flag=true;
				}
		}
		return count;
	}
}
