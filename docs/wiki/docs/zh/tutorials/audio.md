---
category: 教程
tags: ["audio"]
---

# Infernux 音频入门

音频播放采用组件式工作流。使用 [AudioSource](../api/AudioSource.md) 发声，使用 [AudioListener](../api/AudioListener.md) 定义听音位置，声音资源则由 [AudioClip](../api/AudioClip.md) 提供。

## 常见流程

1. 导入或引用音频资源。
2. 给需要发声的对象添加 `AudioSource`。
3. 确保相机或玩家对象上存在 `AudioListener`。
4. 配置循环、音量和 3D 播放属性。
5. 在玩法脚本中触发播放。

## 相关 API

- [AudioSource](../api/AudioSource.md)
- [AudioListener](../api/AudioListener.md)
- [AudioClip](../api/AudioClip.md)
