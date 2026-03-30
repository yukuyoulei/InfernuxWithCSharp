---
category: 教程
tags: ["coroutines", "timing"]
---

# 协程与时间系统

协程可以把跨多帧的延迟逻辑写得更直接，而不必把所有流程都手写成状态机。时间工具与协程体系配套，使帧间逻辑保持可读。

## 常用类型

- [Coroutine](../api/Coroutine.md)
- [WaitForSeconds](../api/WaitForSeconds.md)
- [WaitForSecondsRealtime](../api/WaitForSecondsRealtime.md)
- [WaitUntil](../api/WaitUntil.md)
- [WaitWhile](../api/WaitWhile.md)
- [Time](../api/Time.md)

## 常见用法

- 延迟播放特效或音效。
- 冷却、无敌帧等时序逻辑。
- 跨多帧轮询游戏条件。
