


def twoSums(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            adding = nums[i] + nums[j]
            subtracting = nums[i] - nums[j]

            if adding == 9:
                return [i, j]
            
            if subtracting == 9:
                return [i, j]
            
def main():
    output = twoSums((2, 7, 11, 15), 9)
    print(output)

main()