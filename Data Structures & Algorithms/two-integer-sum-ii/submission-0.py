class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        leftpointer = 0
        rightpointer = len(numbers) - 1

        while leftpointer < rightpointer:
            if numbers[leftpointer] + numbers[rightpointer] > target:
                rightpointer -= 1
            if numbers[leftpointer] + numbers[rightpointer] < target:
                leftpointer += 1
            if numbers[leftpointer] + numbers[rightpointer] == target:
                return [leftpointer + 1, rightpointer + 1]
