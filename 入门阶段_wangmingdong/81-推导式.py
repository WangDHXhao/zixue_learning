# 引入：现在需要快速产生1，3，5，7，9。。。最大值是99

# 之前的方法

nums = []
for i in range(100):
    if i % 2 != 0:
        nums.append(i)

print(nums)

####用推导式就一行代码


nums1 = [x for x in range(100) if x % 2 != 0]

print(nums1)


nums2 = {x:111 for x in range(100) if x%2==0}
print(nums2)
