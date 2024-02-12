package practice;

public class LongestIncreasingSubsequence {
	public static int LIS(int[]arr)
	{
		int[]memory= new int[arr.length];
		for(int i=0 ;i<memory.length;i++)
		{
			memory[i]=1;
		}
		
		for(int i = 1;i<arr.length;i++) {
			for(int j=0; j<i;j++) {
				if(arr[j]<arr[i]) {
					memory[i]=Math.max(memory[i], memory[j]+1);
				}
			}
		}
		int maxLength=memory[0];
		for(int i=1 ;i<memory.length;i++) {
			maxLength=Math.max(memory[i], maxLength);
		}
		return maxLength;
	}

}
