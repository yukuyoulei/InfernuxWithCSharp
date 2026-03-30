---
category: 教程
tags: ["rendering"]
---

# 渲染、RenderGraph 与 RenderStack

Infernux 将渲染编排能力暴露给 Python 层。重点不只是配置材质，而是能够描述 Pass、资源和效果，让渲染流程保持可读和可扩展。

## 关键类型

- [RenderGraph](../api/RenderGraph.md)
- [RenderPassBuilder](../api/RenderPassBuilder.md)
- [RenderPipeline](../api/RenderPipeline.md)
- [RenderStack](../api/RenderStack.md)
- 后处理效果，例如 [BloomEffect](../api/BloomEffect.md) 和 [ToneMappingEffect](../api/ToneMappingEffect.md)

## 常见工作流

1. 定义需要的渲染 Pass。
2. 描述资源读写和依赖关系。
3. 插入后处理或自定义效果。
4. 在 Python 侧迭代，由原生后端负责执行细节。
