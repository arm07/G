
*****Max Sum Contiguous Subarray*****

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.

public class Solution {
	// DO NOT MODFIY THE LIST. 
	public int maxSubArray(final List<Integer> a) {
	    
	    int len=a.size();
	    int maxTemp=a.get(0);
	    int res=a.get(0);
	    
	    for(int i=1;i<len;i++){
	        
	        int nxtVal=a.get(i);
	        //int temp=nxtVal+maxTemp;
	        maxTemp=Math.max(nxtVal,nxtVal+maxTemp);
	        res=Math.max(maxTemp,res);
	        
	    }
	    return res;
	}
}