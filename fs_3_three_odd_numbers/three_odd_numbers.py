def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    sum = 0;
    for num in nums:
        idx = nums.index(num);
        if idx <= len(nums) - 1 - 2:
            sum = num + nums[idx + 1] + nums[idx + 2];
            if sum % 2 == 1:
                return True;
            else:
                sum = 0;
    return False;

        
