# add_component_menu

<div class="class-info">
function in <b>Infernux.components</b>
</div>

```python
add_component_menu(path: str) → Callable
```

## Description

Specify where this component appears in the Add Component menu.

Args:
    path: Menu path like ``"Physics/Character Controller"``.

<!-- USER CONTENT START --> description

Specifies the menu path where this component appears in the editor's **Add Component** menu. Use slashes to create nested categories (e.g., `"Gameplay/AI/Patrol"`).

Without this decorator, custom components appear at the top level of the menu.

<!-- USER CONTENT END -->

## Parameters

| Name | Type | Description |
|------|------|------|
| path | `str` |  |

## Example

<!-- USER CONTENT START --> example
```python
from Infernux import InxComponent
from Infernux.components import add_component_menu

@add_component_menu("Gameplay/Character/PlayerController")
class PlayerController(InxComponent):
    """Appears under Gameplay > Character in the Add Component menu."""
    def update(self):
        pass
```
<!-- USER CONTENT END -->
