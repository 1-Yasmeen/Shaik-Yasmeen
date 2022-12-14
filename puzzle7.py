def test(nums):
   nums=[1,1,1,1,1]
   return all([sum(nums[:i])==i for i in range(len(nums))])
print(nums)
print(test(nums))
