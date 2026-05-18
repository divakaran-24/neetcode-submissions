class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxval = 0
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackind , stackh = stack.pop()
                width = i - stackind
                maxval = max(maxval, stackh * width)
                start = stackind
            stack.append((start,h))

        for i,h in stack:
            maxval = max(maxval,h*(len(heights) - i))
        return maxval 

        