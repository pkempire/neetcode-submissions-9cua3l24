class MedianFinder:

    def __init__(self):
        self.nums = []
        self.n=0

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        self.n = len(self.nums)
        if self.n==1:
            return self.nums[0]
        elif self.n%2==1:
            return self.nums[self.n//2]    
        else:
            return (self.nums[(self.n//2)-1] + self.nums[self.n//2]) / 2 

        