---
category: Tutorials
tags: ["physics"]
---

# Physics in Infernux

Infernux uses Jolt Physics underneath the Python API. The usual workflow is to attach collider components, add a [Rigidbody](../api/Rigidbody.md) when motion should be simulated, and use [Physics](../api/Physics.md) for queries such as raycasts.

## Core building blocks

- [Rigidbody](../api/Rigidbody.md): controls simulated motion, forces, and constraints.
- [BoxCollider](../api/BoxCollider.md), [SphereCollider](../api/SphereCollider.md), [CapsuleCollider](../api/CapsuleCollider.md), [MeshCollider](../api/MeshCollider.md): define collision shapes.
- [CollisionDetectionMode](../api/CollisionDetectionMode.md): choose the collision strategy.
- [Physics](../api/Physics.md): world queries and helper utilities.

## Typical setup

1. Create a `GameObject` for the simulated object.
2. Add a collider that matches the shape you need.
3. Add a `Rigidbody` if the object should respond to simulation.
4. Configure mass, constraints, and collision layers.
5. Use physics queries or callbacks to drive gameplay.

## Related API

- [Rigidbody](../api/Rigidbody.md)
- [RigidbodyConstraints](../api/RigidbodyConstraints.md)
- [Collider](../api/Collider.md)
- [Physics](../api/Physics.md)
