# Component

<div class="class-info">
class in <b>Infernux</b>
</div>

## Description

Base class for all components attached to GameObjects.

<!-- USER CONTENT START --> description

Component is the base class for all built-in C++ components in Infernux, including [Transform](Transform.md), [Camera](Camera.md), [Light](Light.md), and [MeshRenderer](MeshRenderer.md). Components are attached to a [GameObject](GameObject.md) and provide specific functionality.

You do not instantiate Component directly. Instead, use `GameObject.add_component()` to attach a built-in component by its type name. Every Component holds a reference back to its owning `game_object` and its `transform`, giving convenient access to the object hierarchy.

For custom gameplay logic written in Python, derive from [InxComponent](InxComponent.md) rather than Component. InxComponent extends Component with lifecycle callbacks such as `start()`, `update()`, and event methods.

<!-- USER CONTENT END -->

## Properties

| Name | Type | Description |
|------|------|------|
| type_name | `str` |  *(read-only)* |
| component_id | `int` |  *(read-only)* |
| enabled | `bool` |  |
| execution_order | `int` |  |
| game_object | `GameObject` |  *(read-only)* |
| required_component_types | `List[str]` |  *(read-only)* |

<!-- USER CONTENT START --> properties

<!-- USER CONTENT END -->

## Public Methods

| Method | Description |
|------|------|
| `is_component_type(type_name: str) → bool` |  |
| `serialize() → str` |  |
| `deserialize(json_str: str) → None` |  |

<!-- USER CONTENT START --> public_methods

<!-- USER CONTENT END -->

## Example

<!-- USER CONTENT START --> example
```python
from Infernux import InxComponent

class ComponentQuery(InxComponent):
    def start(self):
        # Every component can access its owning GameObject
        owner = self.game_object
        print(f"Attached to: {owner.name}")

        # Access the Transform through the component shortcut
        pos = self.transform.position
        print(f"Position: {pos}")

        # Get a sibling C++ component
        renderer = owner.get_cpp_component("MeshRenderer")
        if renderer:
            print("MeshRenderer found")

        # List all components on this object
        for comp in owner.get_components():
            print(f"Component: {type(comp).__name__}")
```
<!-- USER CONTENT END -->

## See Also

<!-- USER CONTENT START --> see_also

- [GameObject](GameObject.md)
- [Transform](Transform.md)
- [InxComponent](InxComponent.md)

<!-- USER CONTENT END -->
