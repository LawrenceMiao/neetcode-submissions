class Solution:
    def trap(self, height: List[int]) -> int:
        waters = []
        for i in height:
            waters.append(0)
        
        for i in range(len(height)):
            if height[i] == 0:
                continue

            curr_height = height[i]
            if height[i - 1] < curr_height and i != 0:
                if not max(height[0:i]) < curr_height:
                    j = i-1
                    while j > 0:
                        if height[j] >= curr_height:
                            break
                        waters[j] = max(curr_height - height[j], waters[j])
                        j -= 1
            
            if i != len(height) - 1 and height[i + 1] < curr_height:
                if not max(height[i+1:]) < curr_height:
                    j = i+1
                    while j < len(height):
                        if height[j] >= curr_height:
                            break
                        waters[j] = max(curr_height - height[j], waters[j])
                        j += 1


        waters[0] = 0
        waters[len(height) - 1] = 0
        # if sum(waters) == 87:
        #     return waters
        return sum(waters)
        

