# UICanvas

<div class="class-info">
class in <b>Infernux.ui</b>
</div>

**Inherits from:** [InxUIComponent](InxUIComponent.md)

## Description

Screen-space UI canvas — root container for all UI elements.

Defines a *design* reference resolution (default 1920x1080).  At runtime
the Game View scales from design resolution to actual viewport size so
that all positions, sizes and font sizes adapt proportionally.

Attributes:
    render_mode: ``ScreenOverlay`` or ``CameraOverlay``.
    sort_order: Rendering order (lower draws first).
    target_camera_id: Camera GameObject ID (CameraOverlay mode only).
    reference_width: Design reference width in pixels (default 1920).
    reference_height: Design reference height in pixels (default 1080).

<!-- USER CONTENT START --> description

<!-- USER CONTENT END -->

## Properties

| Name | Type | Description |
|------|------|------|
| render_mode | `RenderMode` |  |
| sort_order | `int` |  |
| target_camera_id | `int` |  |
| reference_width | `int` |  |
| reference_height | `int` |  |

<!-- USER CONTENT START --> properties

<!-- USER CONTENT END -->

## Public Methods

| Method | Description |
|------|------|
| `invalidate_element_cache() → None` | Mark the cached element list as stale. |
| `iter_ui_elements() → Iterator[InxUIScreenComponent]` | Yield all screen-space UI components on child GameObjects (depth-first). |
| `raycast(canvas_x: float, canvas_y: float) → Optional[InxUIScreenComponent]` | Return the front-most element hit at ``(canvas_x, canvas_y)``, or ``None``. |
| `raycast_all(canvas_x: float, canvas_y: float) → List[InxUIScreenComponent]` | Return all elements hit at the given point, front-to-back order. |

<!-- USER CONTENT START --> public_methods

<!-- USER CONTENT END -->

## Example

<!-- USER CONTENT START --> example
```python
# TODO: Add example for UICanvas
```
<!-- USER CONTENT END -->

## See Also

<!-- USER CONTENT START --> see_also

<!-- USER CONTENT END -->
