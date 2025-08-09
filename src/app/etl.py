def clean_sum(nums):
    # ignore None values; sum the rest
    return sum(x for x in nums if x is not None)
