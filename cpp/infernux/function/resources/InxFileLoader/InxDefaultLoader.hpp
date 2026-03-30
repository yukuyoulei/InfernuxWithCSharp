#include <function/resources/AssetRegistry/IAssetLoader.h>
#include <function/resources/InxResource/InxResourceMeta.h>

namespace infernux
{
class InxDefaultTextLoader : public IAssetLoader
{
  public:
    InxDefaultTextLoader();

    bool LoadMeta(const char *content, const std::string &filePath, InxResourceMeta &metaData) override;
    void CreateMeta(const char *content, size_t contentSize, const std::string &filePath,
                    InxResourceMeta &metaData) override;

    std::shared_ptr<void> Load(const std::string & /*filePath*/, const std::string & /*guid*/,
                               AssetDatabase * /*adb*/) override
    {
        return nullptr;
    }
    bool Reload(std::shared_ptr<void> /*existing*/, const std::string & /*filePath*/, const std::string & /*guid*/,
                AssetDatabase * /*adb*/) override
    {
        return false;
    }
    std::set<std::string> ScanDependencies(const std::string & /*filePath*/, AssetDatabase * /*adb*/) override
    {
        return {};
    }
};

class InxDefaultBinaryLoader : public IAssetLoader
{
  public:
    InxDefaultBinaryLoader();

    bool LoadMeta(const char *content, const std::string &filePath, InxResourceMeta &metaData) override;
    void CreateMeta(const char *content, size_t contentSize, const std::string &filePath,
                    InxResourceMeta &metaData) override;

    std::shared_ptr<void> Load(const std::string & /*filePath*/, const std::string & /*guid*/,
                               AssetDatabase * /*adb*/) override
    {
        return nullptr;
    }
    bool Reload(std::shared_ptr<void> /*existing*/, const std::string & /*filePath*/, const std::string & /*guid*/,
                AssetDatabase * /*adb*/) override
    {
        return false;
    }
    std::set<std::string> ScanDependencies(const std::string & /*filePath*/, AssetDatabase * /*adb*/) override
    {
        return {};
    }

  private:
    /// @brief Get binary file type based on file extension
    /// @param extension The file extension
    /// @return String describing the binary file type
    std::string GetBinaryTypeFromExtension(const std::string &extension) const;
};
} // namespace infernux
