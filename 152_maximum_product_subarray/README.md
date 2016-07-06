# Maximum Product Subarray

### 解法

动态规划解题。设n和p是两个数组，p[i]表示以i结尾的最大的正阶乘，n[i]表示以i结尾的最小的负阶乘。

那么有：

```
if A[i] > 0
	p[i] = max(p[i-1] * A[i]), A[i]
	n[i] = n[i-1] * A[i]
if A[i] < 0
	p[i] = n[i-1] * A[i]
	n[i] = min(p[i-1]*A[i], A[i])
```

### Note

如果Ａ[i] = 0，那么就要跳过[1, i]这一个区间，从i+1重新开始计算。
