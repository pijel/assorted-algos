class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        return how_much_water(height)
        
def how_much_water(height):
    elevation = 1
    rain_water = 0
    
    while elevation <= max(height):
        i = 0
        
        while i < (len(height)):
            #print(i)
            distance = 1
            if height[i] >= elevation:
                looking_for_right_closure  = True
                while looking_for_right_closure:
                    while i+1 < len(height) and height[i+1] >= elevation:
                        i += 1 
                    distance +=1 
                    if i+distance < len(height):
                        if height[i+distance] >= elevation:
                            looking_for_right_closure = False
                            rain_water += distance - 1
                            #distance = 1
                    else:
                        looking_for_right_closure = False
            if distance > 1:
                i += distance
            else:
                i+=1
        elevation +=1
                
    return rain_water