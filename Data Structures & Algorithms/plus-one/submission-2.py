class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mult = 1 
        num = 0
        for i in range(len(digits)-1, -1,-1):
            num += digits[i] * mult
            mult *= 10
        num+=1
        res = []
        str_num = str(num)
        for i in range (len(str(num))):
            res.append(int(str(num)[i]))

        return res    
