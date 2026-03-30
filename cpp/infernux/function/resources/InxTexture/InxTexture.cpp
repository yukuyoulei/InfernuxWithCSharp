#include "InxTexture.h"

#include <function/resources/InxResource/InxResourceMeta.h>

#include <core/log/InxLog.h>

namespace infernux
{

// =============================================================================
// LoadImportSettings — read ALL settings from .meta file
// =============================================================================

bool InxTexture::LoadImportSettings(const std::string &filePath)
{
    std::string metaPath = InxResourceMeta::GetMetaFilePath(filePath);
    InxResourceMeta meta;
    if (!meta.LoadFromFile(metaPath))
        return false;

    if (meta.HasKey("texture_type")) {
        m_textureType = meta.GetDataAs<std::string>("texture_type");
    }
    if (meta.HasKey("srgb")) {
        m_srgb = meta.GetDataAs<bool>("srgb");
    }
    if (meta.HasKey("generate_mipmaps")) {
        m_generateMipmaps = meta.GetDataAs<bool>("generate_mipmaps");
    }
    if (meta.HasKey("max_size")) {
        m_maxSize = meta.GetDataAs<int>("max_size");
    }

    INXLOG_INFO("InxTexture::LoadImportSettings: path='", filePath, "' srgb=", m_srgb ? "true" : "false", " type='",
                m_textureType, "' mipmaps=", m_generateMipmaps ? "true" : "false", " maxSize=", m_maxSize);

    return true;
}

} // namespace infernux
