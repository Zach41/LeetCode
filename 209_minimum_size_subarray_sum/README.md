# Minimum Size subarray Sum

### 解法1

典型的移动窗口问题。设置两个指针left，right。

1. sum[left->right] < s，right右移
2. sum[left->right] >=s，更新最小值，同时left右移

重复上述步骤，最后得到的便是符合要求的最小值

### 解法2

因为所有的值都是正整数，我们设sum[i]表示[0, i-1]的和，那么sum[1], ... , sum[n]递增，于是对于每一个i，我们可以用二分查找找到一个j，使得

```
sum[j] >= sum[i] + s > sum[j-1]
```

更新最小值为j-i即可。

时间复杂度为O(nlogn)

##### Note

解法2在写代码的时候要注意细节。
