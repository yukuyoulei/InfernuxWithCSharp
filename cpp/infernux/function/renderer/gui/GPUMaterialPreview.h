#pragma once

#include <function/renderer/vk/VkHandle.h>
#include <memory>
#include <vector>

namespace infernux
{

class InxVkCoreModular;
class InxMaterial;

/// @brief GPU-based material preview renderer.
/// Uses the real material pipeline (vertex + fragment shaders) to render a
/// lit sphere into a small offscreen framebuffer and reads back RGBA8 pixels.
class GPUMaterialPreview
{
  public:
    explicit GPUMaterialPreview(InxVkCoreModular *vkCore);
    ~GPUMaterialPreview();

    GPUMaterialPreview(const GPUMaterialPreview &) = delete;
    GPUMaterialPreview &operator=(const GPUMaterialPreview &) = delete;

    /// @brief Render a material onto a sphere and return RGBA8 pixels.
    /// @param material  Material with a valid Forward pipeline.
    /// @param size      Output image width and height (square).
    /// @param outPixels Receives size*size*4 bytes of RGBA8 pixel data.
    /// @return true on success.
    bool RenderToPixels(InxMaterial &material, int size, std::vector<unsigned char> &outPixels);

  private:
    bool EnsureResources(int size);
    void CreateRenderPass();
    void CreateFramebuffer(int size);
    void CreateSphereBuffers();
    void DestroyFramebuffer();

    InxVkCoreModular *m_vkCore = nullptr;
    int m_currentSize = 0;

    // Render pass (compatible with MaterialPipelineManager's internal pass)
    VkRenderPass m_renderPass = VK_NULL_HANDLE;

    // MSAA color attachment
    vk::VkImageHandle m_msaaColor;
    // Resolved (1x) color attachment for readback
    vk::VkImageHandle m_resolveColor;
    // MSAA depth attachment
    vk::VkImageHandle m_depth;

    VkFramebuffer m_framebuffer = VK_NULL_HANDLE;

    // Staging buffer for GPU → CPU readback
    vk::VkBufferHandle m_staging;

    // Default per-view shadow descriptor used when no active scene descriptor
    // is available but the shader statically uses set 1.
    VkDescriptorSet m_fallbackShadowDescSet = VK_NULL_HANDLE;

    // Sphere geometry
    std::unique_ptr<vk::VkBufferHandle> m_sphereVBO;
    std::unique_ptr<vk::VkBufferHandle> m_sphereIBO;
    uint32_t m_sphereIndexCount = 0;

    // Cached format info
    VkFormat m_colorFormat = VK_FORMAT_UNDEFINED;
    VkFormat m_depthFormat = VK_FORMAT_UNDEFINED;
    VkSampleCountFlagBits m_sampleCount = VK_SAMPLE_COUNT_1_BIT;
};

} // namespace infernux
