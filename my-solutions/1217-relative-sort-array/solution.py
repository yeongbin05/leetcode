class Solution(object):
    def relativeSortArray(self, arr1, arr2):
            # Create a dictionary for the order in arr2
        order_map = {num: index for index, num in enumerate(arr2)}

        # Elements in arr2
        arr1_in_arr2 = [num for num in arr1 if num in order_map]
        # Elements not in arr2
        arr1_not_in_arr2 = [num for num in arr1 if num not in order_map]

        # Sort elements in arr1 according to the order in arr2
        arr1_in_arr2.sort(key=lambda x: order_map[x])
        # Sort elements not in arr2 in ascending order
        arr1_not_in_arr2.sort()

        # Combine the sorted arrays
        return arr1_in_arr2 + arr1_not_in_arr2
        
