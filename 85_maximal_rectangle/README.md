# Maximal Rectangle

### 解法

举一个例子。对于数组

```
0, 1, 1, 0
1, 0, 1, 1
0, 0, 1, 1
```

我们将数组预处理成这样的方阵：每一个元素为包括自身在内的前面连续个１的最大个数。

```
0, 1, 2, 0
1, 0, 1, 2
0, 0, 1, 2
```

这样之后，对于每一行，我们就可以按照[Largest Rectangle in Histogram](../84_largest_rectangle_in_histogram/README.md)的解法对每一列求最大区域，最后取最大值即可。

