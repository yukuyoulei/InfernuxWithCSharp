---
category: 教程
tags: ["physics"]
---

# Infernux 物理入门

Infernux 的物理层底层基于 Jolt Physics。常见工作流是给对象挂上碰撞体，需要受模拟控制时再添加 [Rigidbody](../api/Rigidbody.md)，查询则通过 [Physics](../api/Physics.md) 完成。

## 核心构件

- [Rigidbody](../api/Rigidbody.md)：控制受模拟影响的运动、受力和约束。
- [BoxCollider](../api/BoxCollider.md)、[SphereCollider](../api/SphereCollider.md)、[CapsuleCollider](../api/CapsuleCollider.md)、[MeshCollider](../api/MeshCollider.md)：定义碰撞形状。
- [CollisionDetectionMode](../api/CollisionDetectionMode.md)：碰撞检测策略。
- [Physics](../api/Physics.md)：物理查询与辅助接口。

## 相关 API

- [Rigidbody](../api/Rigidbody.md)
- [RigidbodyConstraints](../api/RigidbodyConstraints.md)
- [Collider](../api/Collider.md)
- [Physics](../api/Physics.md)
