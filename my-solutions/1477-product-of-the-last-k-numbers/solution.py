class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.product = 1

    def add(self, num: int) -> None:
    
        if num != 0:
            self.product *= num
            self.arr.append(self.product)
        else:
            self.product = 1
            self.arr = []

    def getProduct(self, k: int) -> int:
        if len(self.arr) < k:
            return 0
        elif len(self.arr) == k :
            return self.product
        else:
            # print(self.product,'self_pr')
            # print(self.arr,'self_arr')
            return self.product // self.arr[len(self.arr)-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
