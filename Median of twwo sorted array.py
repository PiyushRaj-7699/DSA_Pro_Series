def merge(nums1, nums2):
    a = len(nums1)
    b = len(nums2)
    i = 0
    j = 0
    ans = []
    while i < a and j < b:
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i = i + 1
        else:
            ans.append(nums2[j])
            j = j + 1

    while i < a:
        ans.append(nums1[i])
        i = i + 1
    while j < b:
        ans.append(nums2[j])
        j = j + 1
        
    c = len(ans)
    if c % 2 != 0:
        median = ans[c//2]
    else:
        median = (ans[c//2]+ans[(c//2)-1])/2

    return median

nums1 = list(map(int, input("Enter the value of nums1 array: ").split()))
nums2 = list(map(int, input("Enter the value of nums2 array: ").split()))

print(merge(nums1, nums2))