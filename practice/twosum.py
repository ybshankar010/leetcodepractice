
class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i
        
        for i, num in enumerate(nums):
            curr = target - num
            j = num_dict.get(curr,-1)
            # print(curr,"",j)
            if j != -1 and i != j:
                indices.append(i)
                indices.append(j)
                break
        
        return indices


def main():
    # Example usage
    solution = Solution()
    # nums = [2, 7, 11, 15]
    nums = [3,2,4]
    target = 6
    result = solution.twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()

