class Solution:
    
    def merge(self, left,right):
        i = 0 
        j=0
        new = []
        while (i < len(left) and j < len(right)):
            if (left[i] < right[j]):
                new.append(left[i])
                i+=1
            else:
                new.append(right[j])  
                j+=1 

        new.extend(left[i:])  
        new.extend(right[j:]) 

        return new
        
    
    def sortArray(self, nums: List[int]) -> List[int]:
        high = len(nums)
        if high <= 1:
            return nums
        
        mid = high //2 
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:high])
        return self.merge(left,right)
