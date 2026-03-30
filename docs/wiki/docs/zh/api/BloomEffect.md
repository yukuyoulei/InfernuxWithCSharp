# BloomEffect

<div class="class-info">
类位于 <b>Infernux.renderstack</b>
</div>

**继承自:** [FullScreenEffect](FullScreenEffect.md)

## 描述

泛光效果。让亮处溢出光晕——梦幻感拉满。

<!-- USER CONTENT START --> description

<!-- USER CONTENT END -->

## 属性

| 名称 | 类型 | 描述 |
|------|------|------|
| name | `str` |  *(只读)* |
| injection_point | `str` |  *(只读)* |
| default_order | `int` |  *(只读)* |
| menu_path | `str` |  *(只读)* |
| threshold | `float` | 亮度阈值。 |
| intensity | `float` | 泛光强度。 |
| scatter | `float` | 散射范围。 |
| clamp | `float` |  |
| tint_r | `float` |  |
| tint_g | `float` |  |
| tint_b | `float` |  |
| max_iterations | `int` |  |

<!-- USER CONTENT START --> properties

<!-- USER CONTENT END -->

## 公共方法

| 方法 | 描述 |
|------|------|
| `get_shader_list() → List[str]` |  |
| `setup_passes(graph: RenderGraph, bus: ResourceBus) → None` |  |

<!-- USER CONTENT START --> public_methods

<!-- USER CONTENT END -->

## 示例

<!-- USER CONTENT START --> example
```python
# TODO: Add example for BloomEffect
```
<!-- USER CONTENT END -->

## 另请参阅

<!-- USER CONTENT START --> see_also

<!-- USER CONTENT END -->
