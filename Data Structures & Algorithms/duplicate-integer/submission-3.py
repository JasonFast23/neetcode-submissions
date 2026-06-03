class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #create the guest list

        for num in nums: #go through each guest
            if num in seen: #if i see the same guest in seen
                return True #return True... we have found a duplicate
            seen.add(num) # add every guests i come across, then refer back to the for loop
            #we don't add seen.add(num) first because that's like adding the guest name first even though 
            #that guest never entered and then marking him as a duplicate that makes no sense

        return False #but if there is no guest that returns twice, return False
