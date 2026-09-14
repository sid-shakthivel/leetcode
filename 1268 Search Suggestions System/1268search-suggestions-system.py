class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []

        currentSeachBit = ""
        eligibleProducts = products
        
        eligibleProducts.sort()

        for letter in searchWord:
            currentSeachBit += letter

            updatedEligibleProducts = []

            for product in eligibleProducts:
                if product.startswith(currentSeachBit):
                    updatedEligibleProducts.append(product)

            res.append(updatedEligibleProducts[:3])

            eligibleProducts = updatedEligibleProducts


        return res