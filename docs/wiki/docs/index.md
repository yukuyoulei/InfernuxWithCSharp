# Infernux Wiki

Welcome to the Infernux documentation wiki.

## Quick Links

- [Project README](https://github.com/ChenlizheMe/Infernux#readme)
- [Chinese README](https://github.com/ChenlizheMe/Infernux/blob/main/README-zh.md)
- [Website](https://chenlizheme.github.io/Infernux/)
- [API Reference](en/api/index.md)


## Tutorials

New to Infernux? Start here:

| Tutorial | Description |
|----------|-------------|
| [Physics](en/tutorials/physics.md) | Colliders, Rigidbody, triggers, raycasting, character controller |
| [Audio](en/tutorials/audio.md) | AudioSource, 3D spatial sound, music, footsteps |
| [UI](en/tutorials/ui.md) | Canvas, Text, Image, Button, health bars, screen fade |
| [Coroutines & Time](en/tutorials/coroutines.md) | WaitForSeconds, time control, async patterns |
| [Rendering](en/tutorials/rendering.md) | Render pipeline, post-processing, custom effects |
| [Building](en/tutorials/building.md) | Standalone game export with Nuitka, Hub launcher |

中文教程：[物理](zh/tutorials/physics.md) · [音频](zh/tutorials/audio.md) · [UI](zh/tutorials/ui.md) · [协程](zh/tutorials/coroutines.md) · [渲染](zh/tutorials/rendering.md) · [构建](zh/tutorials/building.md)

## Getting Started

Infernux is an open-source game engine with a C++17 / Vulkan runtime and a Python production layer. Use Python for gameplay, tools, and iteration-heavy workflows while the engine handles rendering, physics, audio, and runtime ownership.

### Hello World

```python
from Infernux import *

class HelloWorld(InxComponent):
    speed: float = serialized_field(default=5.0)
    
    def start(self):
        Debug.log("Hello, Infernux!")
    
    def update(self):
        self.transform.rotate(vector3(0, self.speed * Time.delta_time, 0))
```

## Modules

| Module | Description |
|--------|-------------|
| [Infernux](en/api/index.md) | Core types — GameObject, Transform, Scene, Component |
| [Infernux.components](en/api/InxComponent.md) | Component system — InxComponent, serialized_field, decorators |
| [Infernux.core](en/api/Material.md) | Assets — Material, Texture, Shader, AudioClip |
| [Infernux.coroutine](en/api/Coroutine.md) | Coroutines — WaitForSeconds, WaitUntil, WaitWhile |
| [Infernux.input](en/api/Input.md) | Input system — keyboard, mouse, touch |
| [Infernux.math](en/api/vector3.md) | Math — vector2, vector3, vector4, quaternion |
| [Infernux.mathf](en/api/Mathf.md) | Math utilities — clamp, lerp, smooth_step |
| [Infernux.physics](en/api/Physics.md) | Physics — Rigidbody, colliders, raycasting |
| [Infernux.rendergraph](en/api/RenderGraph.md) | Render graph — textures, passes, formats |
| [Infernux.renderstack](en/api/RenderStack.md) | Render stack — pipelines, post-processing effects |
| [Infernux.scene](en/api/SceneManager.md) | Scene management |
| [Infernux.timing](en/api/Time.md) | Time — delta_time, time_scale, frame timing |
| [Infernux.ui](en/api/UICanvas.md) | UI — Canvas, Text, Image, Button |
| [Infernux.debug](en/api/Debug.md) | Logging and diagnostics |
| [Infernux.gizmos](en/api/Gizmos.md) | Visual debugging aids |
