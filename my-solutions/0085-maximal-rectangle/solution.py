class Solution(object):
    def maximalRectangle(self, matrix):
        
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                # Update the height of the histogram
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Append a zero at the end to handle the end of the list

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            # Pop the top of the stack and calculate the area
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area



        
