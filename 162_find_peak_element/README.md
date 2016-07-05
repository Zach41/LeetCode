# Find Peak Element

### 解法1

最简单的解法就是遍历一遍数组，注意对只有一个元素的数组要特殊处理

### 解法2

二分法解该题。

设数组的左右边界为l和r，`mid = (l+r) / 2`，如果nums[mid-1]比nums[mid]来得大，那么peak element一定在左区间中，因为若nums[mid-2] < nums[mid-1]，那么nums[mid-1]就是peak element，否则继续在[0, mid-2]中查找。因为最左边是负无穷，所以一定存在peak element，右区间同理。
