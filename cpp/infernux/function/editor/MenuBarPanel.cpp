#include "MenuBarPanel.h"

namespace infernux
{

// ════════════════════════════════════════════════════════════════════
// Construction
// ════════════════════════════════════════════════════════════════════

MenuBarPanel::MenuBarPanel() = default;

// ════════════════════════════════════════════════════════════════════
// Translation helper
// ════════════════════════════════════════════════════════════════════

std::string MenuBarPanel::T(const std::string &key) const
{
    if (translate)
        return translate(key);
    auto dot = key.rfind('.');
    return (dot != std::string::npos) ? key.substr(dot + 1) : key;
}

// ════════════════════════════════════════════════════════════════════
// Render
// ════════════════════════════════════════════════════════════════════

void MenuBarPanel::OnRender(InxGUIContext *ctx)
{
    // Handle global shortcuts before menu logic
    HandleShortcuts(ctx);

    // Check for window close request (SDL_EVENT_QUIT intercepted by C++)
    if (isCloseRequested && onRequestClose)
    {
        if (isCloseRequested())
            onRequestClose();
    }

    // Style overrides
    ImGui::PushStyleVar(ImGuiStyleVar_FramePadding, EditorTheme::TOOLBAR_FRAME_PAD);
    ImGui::PushStyleVar(ImGuiStyleVar_ItemSpacing, EditorTheme::TOOLBAR_ITEM_SPC);
    ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, EditorTheme::TOOLBAR_WIN_PAD);
    ImGui::PushStyleColor(ImGuiCol_MenuBarBg, EditorTheme::MENU_BAR_BG);
    ImGui::PushStyleColor(ImGuiCol_PopupBg, EditorTheme::POPUP_BG);
    ImGui::PushStyleColor(ImGuiCol_HeaderHovered, EditorTheme::HEADER_HOVERED);
    ImGui::PushStyleColor(ImGuiCol_HeaderActive, EditorTheme::HEADER_ACTIVE);

    if (ImGui::BeginMainMenuBar())
    {
        RenderProjectMenu(ctx);
        RenderWindowMenu(ctx);
        ImGui::EndMainMenuBar();
    }

    ImGui::PopStyleColor(4);
    ImGui::PopStyleVar(3);

    // Note: floating sub-panels (BuildSettings, Preferences, PhysicsLayerMatrix)
    // and save-confirmation popup are rendered from Python side.
}

// ════════════════════════════════════════════════════════════════════
// Keyboard shortcuts
// ════════════════════════════════════════════════════════════════════

void MenuBarPanel::HandleShortcuts(InxGUIContext *ctx)
{
    bool ctrl = ctx->IsKeyDown(KEY_LEFT_CTRL) || ctx->IsKeyDown(KEY_RIGHT_CTRL);
    if (!ctrl)
        return;

    if (ctx->IsKeyPressed(KEY_S) && onSave)
        onSave();

    if (ctx->IsKeyPressed(KEY_N) && onNewScene)
        onNewScene();

    if (ctx->IsKeyPressed(KEY_Z))
    {
        if (canUndo && canUndo() && onUndo)
            onUndo();
    }

    if (ctx->IsKeyPressed(KEY_Y))
    {
        if (canRedo && canRedo() && onRedo)
            onRedo();
    }
}

// ════════════════════════════════════════════════════════════════════
// Project menu
// ════════════════════════════════════════════════════════════════════

void MenuBarPanel::RenderProjectMenu(InxGUIContext *ctx)
{
    if (!ImGui::BeginMenu(T("menu.project").c_str()))
        return;

    // Build Settings toggle
    bool bsOpen = isBuildSettingsOpen ? isBuildSettingsOpen() : false;
    if (ImGui::MenuItem(T("menu.build_settings").c_str(), "", bsOpen, true))
    {
        if (toggleBuildSettings)
            toggleBuildSettings();
    }

    // Physics Layer Matrix toggle
    bool plOpen = isPhysicsLayerMatrixOpen ? isPhysicsLayerMatrixOpen() : false;
    if (ImGui::MenuItem(T("menu.physics_layer_matrix").c_str(), "", plOpen, true))
    {
        if (togglePhysicsLayerMatrix)
            togglePhysicsLayerMatrix();
    }

    ImGui::Separator();

    // Preferences toggle
    bool prefOpen = isPreferencesOpen ? isPreferencesOpen() : false;
    if (ImGui::MenuItem(T("menu.preferences").c_str(), "", prefOpen, true))
    {
        if (togglePreferences)
            togglePreferences();
    }

    ImGui::EndMenu();
}

// ════════════════════════════════════════════════════════════════════
// Window menu
// ════════════════════════════════════════════════════════════════════

void MenuBarPanel::RenderWindowMenu(InxGUIContext *ctx)
{
    if (!ImGui::BeginMenu(T("menu.window").c_str()))
        return;

    if (getRegisteredTypes && getOpenWindows)
    {
        auto types = getRegisteredTypes();
        auto openWins = getOpenWindows();

        if (!types.empty())
        {
            for (const auto &info : types)
            {
                bool isOpen = false;
                auto it = openWins.find(info.typeId);
                if (it != openWins.end())
                    isOpen = it->second;

                bool canCreate = !(info.singleton && isOpen);

                if (ImGui::MenuItem(info.displayName.c_str(), "", isOpen, canCreate))
                {
                    if (isOpen)
                    {
                        if (closeWindow)
                            closeWindow(info.typeId);
                    }
                    else
                    {
                        if (openWindow)
                            openWindow(info.typeId);
                    }
                }
            }
        }
        else
        {
            ImGui::MenuItem(T("menu.no_windows").c_str(), "", false, false);
        }
    }
    else
    {
        ImGui::MenuItem(T("menu.no_wm").c_str(), "", false, false);
    }

    ImGui::Separator();

    if (ImGui::MenuItem(T("menu.reset_layout").c_str(), "", false, true))
    {
        if (resetLayout)
            resetLayout();
    }

    ImGui::EndMenu();
}

} // namespace infernux
