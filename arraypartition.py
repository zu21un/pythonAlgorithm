def array_partition(self, nums:List[int])->int:
    return sum(sorted(nums)[::2])