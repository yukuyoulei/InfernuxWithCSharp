#pragma once

#include "EditorTheme.h"
#include <function/renderer/gui/InxGUIContext.h>
#include <function/renderer/gui/InxGUIRenderable.h>

#include <imgui.h>

#include <functional>
#include <map>
#include <string>
#include <vector>

namespace infernux
{

/// Info about a registered window type (mirrors Python WindowManager data).
struct WindowTypeInfo
{
    std::string typeId;
    std::string displayName;
    bool singleton = true;
};

/// C++ native menu bar — Project / Window menus + keyboard shortcuts.
/// Not dockable (inherits InxGUIRenderable directly).
///
/// Floating sub-panels (BuildSettings, Preferences, PhysicsLayerMatrix) and
/// the save-confirmation popup are still rendered from Python; this panel
/// delegates to Python callbacks for operations that touch Python-only managers.
class MenuBarPanel : public InxGUIRenderable
{
  public:
    MenuBarPanel();
    ~MenuBarPanel() override = default;

    // ── Callbacks set from Python ────────────────────────────────────

    // Scene file operations
    std::function<void()> onSave;
    std::function<void()> onNewScene;
    std::function<void()> onRequestClose;

    // Undo
    std::function<void()> onUndo;
    std::function<void()> onRedo;
    std::function<bool()> canUndo;
    std::function<bool()> canRedo;

    // Window management
    std::function<std::vector<WindowTypeInfo>()> getRegisteredTypes;
    std::function<std::map<std::string, bool>()> getOpenWindows;
    std::function<void(const std::string &)> openWindow;
    std::function<void(const std::string &)> closeWindow;
    std::function<void()> resetLayout;

    // Close request check (C++ engine)
    std::function<bool()> isCloseRequested;

    // Toggle floating sub-panels — rendered from Python
    std::function<void()> toggleBuildSettings;
    std::function<void()> togglePreferences;
    std::function<void()> togglePhysicsLayerMatrix;
    std::function<bool()> isBuildSettingsOpen;
    std::function<bool()> isPreferencesOpen;
    std::function<bool()> isPhysicsLayerMatrixOpen;

    // i18n
    std::function<std::string(const std::string &)> translate;

    // ── InxGUIRenderable ─────────────────────────────────────────────
    void OnRender(InxGUIContext *ctx) override;

  private:
    void HandleShortcuts(InxGUIContext *ctx);
    void RenderProjectMenu(InxGUIContext *ctx);
    void RenderWindowMenu(InxGUIContext *ctx);

    std::string T(const std::string &key) const;

    // ImGuiKey constants
    static constexpr int KEY_S = 564;
    static constexpr int KEY_N = 559;
    static constexpr int KEY_Z = 571;
    static constexpr int KEY_Y = 570;
    static constexpr int KEY_LEFT_CTRL = 527;
    static constexpr int KEY_RIGHT_CTRL = 531;
};

} // namespace infernux
