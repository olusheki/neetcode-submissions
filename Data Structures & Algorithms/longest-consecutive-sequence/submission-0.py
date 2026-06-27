class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        understand: return just the length. So, you're given the array, and 
        the order of them matter. the algorithm must be O(N), so no nested
        for loops. brute force isn't an option. They must be 1 greater exactly
        
        match: I know that this is supposed to be arrays and hashing, so I'm 
        thinking of an optimal way to iterate through the array and track it
        using those data structures. if I used `in` then that is O(n), so..
        I was thinking that I would get a dict maybe, then I would track the times
        that a number greater than 1 came after it, then follow the trail until it stops?

        or I convert the list to a set, and then just iterate through that since
        `in` for a set is O(1). For each element, if... that needs a nested for loop

        Maybe sort it? Then just count the max as you go?
        """

        # 2, 3, 4, 4, 5, 10, 20
        # 0, 1, 1, 2, 3, 4, 5, 6,
        if not nums:
            return 0
        nums.sort()
        maxCount = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                maxCount = max(maxCount, count)
                count = 0
        maxCount = max(maxCount, count)
        return maxCount + 1