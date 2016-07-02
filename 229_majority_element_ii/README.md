# Majority Element II

### 解法1

用哈希表来记录每个数的次数，最后判断，空间复杂度为O(n)

### 解法2

分析可知最多有2个majority number，我们用如下的算法来计算：

```Python
if n1 == num:
	c1 += 1
elif n2 == num:
	c2 += 1
elif c1 == 0:
	c1, n1 = 1, num
elif c2 == 0:
	c2, n2 = 1, num
else:
	c1, c2 = c1-1, c2-1
```

最后得到n1, n2，如果不为None且nums.count(ni)>n/3，ni就是majority number（i＝1，2）

#### Note
上述算法可以保证最后如果一个数是majority number，那么它一定可以被留下（可以亲自试一下过程就很显然可以知道）
