#pragma once

#include <core/log/InxLog.h>
#include <core/types/InxApplication.h>

#include <vulkan/vulkan.h>

#include <SDL3/SDL.h>
#include <SDL3/SDL_vulkan.h>

namespace infernux
{
class InxView
{
  public:
    friend class InxRenderer;

    InxView();

    InxView(const InxView &) = delete;
    InxView(InxView &&) = delete;
    InxView &operator=(const InxView &) = delete;
    InxView &operator=(InxView &&) = delete;

    const char *const *GetVkExtensions(uint32_t *count);

    void Init(int width, int height);
    void ProcessEvent();
    void Quit();

    int GetUserEvent();
    void Show();
    void Hide();
    void SetWindowIcon(const std::string &iconPath);
    void SetWindowFullscreen(bool fullscreen);
    void SetWindowTitle(const std::string &title);
    void SetWindowMaximized(bool maximized);
    void SetWindowResizable(bool resizable);

    /// Close-request interception: SDL_EVENT_QUIT sets this flag instead of
    /// immediately terminating.  Python checks the flag each frame and may
    /// show a "save before exit?" dialog before calling ConfirmClose().
    bool IsCloseRequested() const
    {
        return m_closeRequested;
    }
    void ConfirmClose()
    {
        m_keepRunning = false;
    }
    void CancelClose()
    {
        m_closeRequested = false;
    }

    bool IsMinimized() const
    {
        return m_isMinimized;
    }

    void CreateSurface(VkInstance *vkInstance, VkSurfaceKHR *vkSurface);
    void SetAppMetadata(InxAppMetadata appMetaData);

  private:
    int m_windowWidth = 0;
    int m_windowHeight = 0;

    SDL_Window *m_window = nullptr;

    bool m_keepRunning;
    bool m_closeRequested = false;
    bool m_isMinimized = false;
    InxAppMetadata m_appMetadata;

    void SDLInit();
};
} // namespace infernux
