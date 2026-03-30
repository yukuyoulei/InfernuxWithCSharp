---
category: Tutorials
tags: ["rendering"]
---

# Rendering with RenderGraph and RenderStack

Infernux exposes render authoring through Python-facing pipeline APIs. The idea is not just to configure materials, but to describe passes, resources, and effects in a way that remains readable.

## Key types

- [RenderGraph](../api/RenderGraph.md)
- [RenderPassBuilder](../api/RenderPassBuilder.md)
- [RenderPipeline](../api/RenderPipeline.md)
- [RenderStack](../api/RenderStack.md)
- Post-processing effects such as [BloomEffect](../api/BloomEffect.md) and [ToneMappingEffect](../api/ToneMappingEffect.md)

## Typical pipeline work

1. Define the render passes you need.
2. Describe resource usage and dependencies.
3. Inject post-processing or custom effects.
4. Iterate from Python while the native backend manages execution details.
