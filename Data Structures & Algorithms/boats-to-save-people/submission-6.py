class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 1, len(people)
        # best case: only need one boat, worst scenario we need oen boat for each el
        # constrains say we people[i] <= limit always./

        # if empty -> boats just return 0
        # 
        people.sort()
        # use 2 pointers we find a erlationship if r + l > we just keep on finding etc.
        l, r = 0, len(people) - 1
        boatsUsed = 0
        while l <= r:
            amt = people[l] + people[r]
            if amt <= limit:
                l+= 1
            r -= 1
            boatsUsed += 1
        return boatsUsed

        
        
        


                    

                






        