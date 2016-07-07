# Best Time to Buy and Sell Stock III

### 解法

对于某一个序列ｉ来说，最大利润就是[1, i]和[i, n]这两个区间各自的最大利润之和。于是解题的思路就显而易见了：

1. max_left[i]表示到ｉ为止的最大利润，有max_left[i] = max(max_left[i-1], prices[i]-min_p)
2. max_right[i]表示从ｉ开始的最大利润，有max_right[i] = max(max_right[i+1], max_p - prices[i])

最后枚举每一个ｉ，得到最大值。
