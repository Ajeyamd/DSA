nums1=[1,2,3]
nums2=[4,5,6]

def merge(nums1, m, nums2, n):
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        nums1.sort()
        
print(merge(nums1,m)