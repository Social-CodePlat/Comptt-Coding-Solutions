def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict=dict()
        for i in range(len(nums)):
            comp=target-nums[i]
            if nums[i] in my_dict:
                return [my_dict[nums[i]],i]
            else:
                my_dict[comp]=i
       
#def twoSumoneforloop(self, nums: List[int], target: int) -> List[int]:
 #       for i in range(len(nums)):
  #          reqd=target-nums[i]
   #         if reqd in nums:
    #            if i!=nums.index(reqd):
     #               return [i,nums.index(reqd)]

#def twoSumbruteforce(self, nums: List[int], target: int) -> List[int]:
 #          for j in range(i+1,len(nums)):
  #              if nums[i]+nums[j]==target:
   #                 return [i,j]#