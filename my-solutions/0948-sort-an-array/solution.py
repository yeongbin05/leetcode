class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        MIN_RUN = 32
        def insertion_sort(arr, left, right):
            for i in range(left + 1, right + 1):
                key_item = arr[i]
                j = i - 1
                while j >= left and arr[j] > key_item:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key_item

        def merge(arr, l, m, r):
            len1, len2 = m - l + 1, r - m
            left, right = [], []

            for i in range(0, len1):
                left.append(arr[l + i])
            for i in range(0, len2):
                right.append(arr[m + 1 + i])

            i, j, k = 0, 0, l

            while i < len1 and j < len2:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len1:
                arr[k] = left[i]
                k += 1
                i += 1

            while j < len2:
                arr[k] = right[j]
                k += 1
                j += 1

        def tim_sort(arr):
            n = len(arr)
            for i in range(0, n, MIN_RUN):
                insertion_sort(arr, i, min((i + MIN_RUN - 1), (n - 1)))

            size = MIN_RUN
            while size < n:
                for left in range(0, n, 2 * size):
                    mid = min((n - 1), (left + size - 1))
                    right = min((left + 2 * size - 1), (n - 1))

                    if mid < right:
                        merge(arr, left, mid, right)

                size = 2 * size
        tim_sort(nums)
        return nums
