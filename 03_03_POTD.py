class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        grea = []
        middle = []
        small = []
        for i in nums:
            if i > pivot:
                grea.append(i)
            elif i == pivot:
                middle .append(i)
            else:
                small.append(i)

        return small+middle+grea
