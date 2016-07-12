# Largest Rectangle in Histogram

### 解法

对于某一个Hi，若设li是左边第一个小于Hi的序列号，ri是右边第一个小于Hi的序列号，那么(li-ri-1)*Hi则是包括Hi在内的最大的矩形区域。由以上的结论可以知道，我们只要对每一个Hi，找到其对应的li和ri，计算出包含其的最大区域，最后取最大值即可。

如何找到Hi对应的li和ri呢？我们可以用一个堆栈维护一个递增序列。当hieghts[stack[top]] >= heights[current]时，current和栈顶的下一个值即我们所需要的值。

需要注意的是我们要在序列的末尾增加一个最小值，以处理序列本身就是递增的情况。
