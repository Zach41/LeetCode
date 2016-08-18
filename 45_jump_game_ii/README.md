# Jump Game II

### 题解

如果maxJump表示当前位置所能达到的最大位置，maxReach表示上一跳的点能达到的最大位置，那么如果

```
i > maxReach
```

那么就应该增加一步，同时更新maxReach为maxJump。

这样做之后可以保证每一步都是跳的最大距离。

