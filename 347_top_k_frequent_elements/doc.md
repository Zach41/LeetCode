# Top K Frequent Elements

### O(n)的解法

1. 记录列表每一个数的频率
2. 获得每一个频率所对应的数，不同的数可能对应同一个频率，所以字典中的值是一个列表
3. 从n开始遍历（从最大的频率开始更好），如果有存在频率a，那么取出频率对应的值，k值作对应的减法

