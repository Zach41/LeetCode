# Find Minimum in Rotated Array

### 没有重复元素

如果没有重复元素，由于数组最初是已经排好序的，那么我们可以利用二分搜索来寻找最小的元素。

1. nums[mid] < nums[end], end = mid
2. nums[min] > nums[end], start = mid

可以这样的原因是因为如果[mid, end]中存在最小值，那么mid一定是旋转过来的，那么一定有nums[mid] > nums [end]；如果不存在最小值，那么nums[mid] < nums[end]。

### 有重复元素

考虑极端的情况[1, 2, 2, 2, 2, 2, 2]，此时旋转之后如果nums[mid] == nums[end]，那么end -= 1，因为１在旋转之后可能在右区间，也可能在左区间。如果完全不旋转，那么时间复杂度就变成了O(n)。所以最简单的方法就是遍历数组，取最小值。
