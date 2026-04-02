class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product =0 
        for idx in range(len(nums)):
            temp = nums.pop(idx)
            product = nums[0]
            for i in range(1, len(nums)):
                product = nums[i] * product
            output.append(product)
            nums.insert(idx,temp)
        return output
