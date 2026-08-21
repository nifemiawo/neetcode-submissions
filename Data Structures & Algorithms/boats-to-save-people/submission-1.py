class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right = len(people)-1
        people.sort()
        boats =0
        while left <=right:
            if people[right] == limit:
                right-=1
                boats+=1
            elif people[right] < limit:
                if people[right]+people[left] <= limit:
                    right-=1
                    left+=1
                    boats+=1
                else:
                    boats+=1
                    right-=1
        return boats