#pragma once

#include <core/log/InxLog.h>

namespace infernux
{

// ----------------------------------
// Template Function Implementations
// ----------------------------------

template <typename T> 
T InxResourceMeta::GetDataAs(const std::string& key) const
{
    auto it = m_metadata.find(key);
    if (it != m_metadata.end()) {
        const auto& metaType = it->second;
        if (metaType.first == InxTypeRegistry::GetInstance().GetTypeName(typeid(T))) {
            return std::any_cast<T>(metaType.second);
        }
        INXLOG_ERROR("Metadata type mismatch for key: ", key, 
                     ", expected: ", InxTypeRegistry::GetInstance().GetTypeName(typeid(T)),
                     ", got: ", metaType.first);
    } else {
        INXLOG_ERROR("Metadata not found for key: ", key);
    }
    return T{}; // Return default-constructed value
}

} // namespace infernux
