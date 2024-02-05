def calc_run_average(nums):
    averages = [nums[0]]
    for i in range(1, len(nums)):
        sum = 0
        for j in range(i + 1):
            sum += nums[j]
        averages.append(sum/(i + 1))
    return averages

print(calc_run_average([1, 2, 3, 4]))