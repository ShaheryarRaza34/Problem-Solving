package practice;

public class CricketProblem {
	
	
	public static String Cricket(int I1, int I2, int I3,int I4, int I5)
	{	String result="";
		int matchPlayed;
		if((I1+I2+I3)==I4)
		{
			matchPlayed=I4;
			result=Integer.toString(matchPlayed)+" "+CricketProblem.calculatePoints(I1, I2, I3, I5);
		}
		if((I1+I2+I3)==I5)
		{
			matchPlayed=I5;
			result=Integer.toString(matchPlayed)+" "+ CricketProblem.calculatePoints(I1, I2, I3, I4);
		}
		if((I2+I3+I4)==I1)
		{
			matchPlayed=I1;
			result=Integer.toString(matchPlayed)+" "+CricketProblem.calculatePoints(I2, I3, I4, I5);
		}
		if((I2+I3+I4)==I5)
		{
			matchPlayed=I5;
			result=Integer.toString(matchPlayed)+ " "+CricketProblem.calculatePoints(I2, I3, I4, I1);
		}
		
		if((I3+I4+I5)==I1)
		{
			matchPlayed=I1;
			result=Integer.toString(matchPlayed)+" "+CricketProblem.calculatePoints(I3, I4, I5, I2);
		}
		
		if((I3+I4+I5)==I2)
		{
			matchPlayed=I2;
			result=Integer.toString(matchPlayed)+ " "+CricketProblem.calculatePoints(I3, I4, I5, I1);
		}
		
		
	return result;
	}
	public static String calculatePoints(int a ,int b,int c,int points)
		{
			String result="";
			if((a*3)+(b*1)==points)
			{
				result = Integer.toString(a)+" "+Integer.toString(b)+" "+Integer.toString(c)+" "+Integer.toString(points);
			}
			if((a*3)+(c*1)==points)
			{
				result = Integer.toString(a)+" "+Integer.toString(c)+" "+Integer.toString(b)+" "+Integer.toString(points);
			}
			if((b*3)+(a*1)==points)
			{
				result = Integer.toString(b)+" "+Integer.toString(a)+" "+Integer.toString(c)+" "+Integer.toString(points);
			}
			if((b*3)+(c*1)==points)
			{
				result = (Integer.toString(b)+" "+Integer.toString(c)+" "+Integer.toString(a)+" "+Integer.toString(points));
			}
			if((c*3)+(a*1)==points)
			{
				result = (Integer.toString(c)+" "+Integer.toString(a)+" "+Integer.toString(b)+" "+Integer.toString(points));
			}
			if((c*3)+(b*1)==points)
			{
				result = Integer.toString(c)+" "+Integer.toString(b)+" "+Integer.toString(a)+" "+Integer.toString(points);
			}
			return result;// formated string
		}
	
	
}
