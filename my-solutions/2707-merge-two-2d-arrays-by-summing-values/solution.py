class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n,m = len(nums1),len(nums2)
        left = right = 0
        ans = []
        while left != n or right != m:
            if left == n :
                ans.append(nums2[right])
                right+=1
                continue
            elif right == m:
                ans.append(nums1[left])
                left += 1
                continue
            if nums1[left][0] == nums2[right][0]:
                ans.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
                left +=1 
                right += 1
            elif nums1[left][0] > nums2[right][0]:
                ans.append(nums2[right])
                right+= 1
            else:
                ans.append(nums1[left])
                left+= 1
            print(left,right)

        return ans
