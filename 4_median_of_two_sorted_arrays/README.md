# Media of Two Sorted Arrays

### 解法

如果总序列元素个数为奇数，我们要求的就是总序列中排列第k的元素（k = (m+n) / 2 + 1），元素个数为偶数也只是多求一个元素。于是这一题转换成求两个有序序列合并后第k大的元素。

易知这样一个性质：在序列1中取前k/2个元素，在序列2中取前k/2个元素，那么这k个元素是总序列中的前k个元素。

那么我们令：

- p = k/2
- q = k-p

取序列1前p个元素，序列2前q个元素，如果nums1[p-1] < nums2[q-1]，我们这时并不知道nums2[q-1]是否太大，但是nums1的前p个序列一定是小于目标的，我们可以抛弃这一部分，得到新的nums1；同理如果nums[p-1] > nums[q-1]，可以得到信息的nums2。如此迭代，我们一定可以删掉总序列前k个元素，即可以得到第k大的元素。

