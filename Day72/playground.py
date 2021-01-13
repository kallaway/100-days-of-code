def add(*nums):
    for n in nums:
        sum = 0
        for n in nums:
            sum += n
        return sum


print(add(1, 2, 3, 4))
