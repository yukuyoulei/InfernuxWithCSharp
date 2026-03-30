/**
 * @file PhysicsECSStore.cpp
 * @brief Contiguous memory pools for Collider and Rigidbody data.
 */

#include "PhysicsECSStore.h"

namespace infernux
{

PhysicsECSStore &PhysicsECSStore::Instance()
{
    static PhysicsECSStore instance;
    return instance;
}

// ============================================================================
// Collider pool
// ============================================================================

PhysicsECSStore::ColliderHandle PhysicsECSStore::AllocateCollider(Collider *owner)
{
    ColliderHandle handle = m_colliderPool.Allocate();
    ColliderECSData &data = m_colliderPool.Get(handle);
    data = ColliderECSData{};
    data.owner = owner;
    return handle;
}

void PhysicsECSStore::ReleaseCollider(ColliderHandle handle)
{
    if (!m_colliderPool.IsAlive(handle))
        return;
    m_colliderPool.Get(handle).owner = nullptr;
    m_colliderPool.Free(handle);
}

bool PhysicsECSStore::IsValid(ColliderHandle handle) const
{
    return m_colliderPool.IsAlive(handle);
}

ColliderECSData &PhysicsECSStore::GetCollider(ColliderHandle handle)
{
    return m_colliderPool.Get(handle);
}

const ColliderECSData &PhysicsECSStore::GetCollider(ColliderHandle handle) const
{
    return m_colliderPool.Get(handle);
}

// ============================================================================
// Rigidbody pool
// ============================================================================

PhysicsECSStore::RigidbodyHandle PhysicsECSStore::AllocateRigidbody(Rigidbody *owner)
{
    RigidbodyHandle handle = m_rigidbodyPool.Allocate();
    RigidbodyECSData &data = m_rigidbodyPool.Get(handle);
    data = RigidbodyECSData{};
    data.owner = owner;
    return handle;
}

void PhysicsECSStore::ReleaseRigidbody(RigidbodyHandle handle)
{
    if (!m_rigidbodyPool.IsAlive(handle))
        return;
    Rigidbody *dying = m_rigidbodyPool.Get(handle).owner;
    // Safety net: clear cachedRigidbody on every alive collider that still
    // references this Rigidbody.  Rigidbody::OnDisable() normally handles
    // this, but during editor undo/redo the lifecycle may not fire if the
    // component was never enabled (inactive hierarchy) or the destroy order
    // bypasses the normal CallOnDestroy path.  Without this, collider hot
    // paths (SyncTransformToPhysics, RebuildShape, AddToBroadphase) would
    // dereference a dangling pointer → crash.
    if (dying) {
        for (auto ch : m_colliderPool.GetAliveHandles()) {
            auto &cd = m_colliderPool.Get(ch);
            if (cd.cachedRigidbody == dying)
                cd.cachedRigidbody = nullptr;
        }
    }
    m_rigidbodyPool.Get(handle).owner = nullptr;
    m_rigidbodyPool.Free(handle);
}

bool PhysicsECSStore::IsValid(RigidbodyHandle handle) const
{
    return m_rigidbodyPool.IsAlive(handle);
}

RigidbodyECSData &PhysicsECSStore::GetRigidbody(RigidbodyHandle handle)
{
    return m_rigidbodyPool.Get(handle);
}

const RigidbodyECSData &PhysicsECSStore::GetRigidbody(RigidbodyHandle handle) const
{
    return m_rigidbodyPool.Get(handle);
}

} // namespace infernux
