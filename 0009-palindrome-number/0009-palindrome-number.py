class Solution(object):
    def isPalindrome(self, x):
        original=x
        rev=0
        while x>0:
            rev=(rev*10)+(x%10)
            x=x//10
        if(original==rev):
            return True 
        else:
            return False
                     
 
             
        """
        :type x: int
        :rtype: bool
        """
        