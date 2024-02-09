# has3 consequent to 3
a = [1 , 3 , 3]
def has33(nums):
   for i in range(len(nums) - 1):
      if(nums[i] == nums[i + 1] == 3):
         return True
   return False
print(has33(a))