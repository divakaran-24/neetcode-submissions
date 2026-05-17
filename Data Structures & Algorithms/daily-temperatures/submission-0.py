class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i,tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                stackt,stackind = stack.pop()

                output[stackind] = (i - stackind)

            stack.append([tem,i])
        return output


