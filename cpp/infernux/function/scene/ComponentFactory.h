#pragma once

#include <functional>
#include <memory>
#include <string>

namespace infernux
{
class Component;

class ComponentFactory
{
  public:
    using Creator = std::function<std::unique_ptr<Component>()>;

    /// @brief Register a component creator by type name
    /// @return true if registered, false if already exists
    static bool Register(const std::string &typeName, Creator creator);

    /// @brief Create a component by type name
    /// @return unique_ptr to component or nullptr if not registered
    static std::unique_ptr<Component> Create(const std::string &typeName);

    /// @brief Check if a component type is registered
    static bool IsRegistered(const std::string &typeName);

    /// @brief Get all registered component type names
    static std::vector<std::string> GetRegisteredTypeNames();
};

} // namespace infernux

// Convenience macro for registering components
#define INFERNUX_REGISTER_COMPONENT(TYPE_STR, CLASS_TYPE)                                                              \
    namespace                                                                                                          \
    {                                                                                                                  \
    const bool s_infernux_component_registered_##CLASS_TYPE =                                                          \
        infernux::ComponentFactory::Register(TYPE_STR, []() { return std::make_unique<CLASS_TYPE>(); });               \
    }
