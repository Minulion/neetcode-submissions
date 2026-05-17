class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        productNoZero = 1
        product = 1
        productArr = []
        for num in nums:
            product *= num
            if num != 0:
                productNoZero *= num
            else:
                zeroCount += 1
        if product == 0:
            for num in nums:
                if num == 0:
                    if zeroCount > 1:
                        productArr.append(0)
                    else:
                        productArr.append(productNoZero)
                else:
                    productArr.append(0)
        else:
            for num in nums:
                productArr.append(int(product/num))
        return productArr
        