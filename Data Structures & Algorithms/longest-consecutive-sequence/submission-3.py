class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #turn the list into a set --> look up numbers quick
        num_set = set(nums)
        longest = 0

        for num in num_set:
            #start counting if this is the first # in sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                #keep checking for the next # in sequence
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                #update the longest streak
                if current_streak > longest:
                    longest = current_streak
                
        return longest