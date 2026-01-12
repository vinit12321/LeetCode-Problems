class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=0
        while (i<j):

            min_height=min(height[i],height[j])

            width=(j-i)
            c_area=min_height*width

            if area<c_area:
                area=c_area
            
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area
        

        