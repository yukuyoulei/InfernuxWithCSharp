"""Tests for C++ native StatusBarPanel, ToolbarPanel, and MenuBarPanel.

These panels were migrated from Python originals as Phase 2 + Phase 3
of the native editor migration plan.
"""
import pytest
from Infernux.lib import (
    StatusBarPanel,
    ToolbarPanel,
    MenuBarPanel,
    ConsolePanel,
    PlayState,
    WindowTypeInfo,
)


# ═══════════════════════════════════════════════════════════════════════
#  StatusBarPanel
# ═══════════════════════════════════════════════════════════════════════

class TestStatusBarPanel:

    def test_creation(self):
        sb = StatusBarPanel()
        assert sb is not None

    def test_set_latest_message(self):
        sb = StatusBarPanel()
        sb.set_latest_message("Hello world", "info")
        # No crash — message is rendered next frame

    def test_set_latest_message_multiline(self):
        sb = StatusBarPanel()
        sb.set_latest_message("Line1\nLine2\nLine3", "warning")

    def test_clear_counts(self):
        sb = StatusBarPanel()
        sb.increment_warn_count()
        sb.increment_error_count()
        sb.clear_counts()
        # Can't directly read counts, but no crash

    def test_increment_counts(self):
        sb = StatusBarPanel()
        sb.increment_warn_count()
        sb.increment_warn_count()
        sb.increment_error_count()

    def test_set_engine_status(self):
        sb = StatusBarPanel()
        sb.set_engine_status("Loading...", 0.5)
        sb.set_engine_status("", -1.0)  # clear

    def test_set_console_panel(self):
        sb = StatusBarPanel()
        console = ConsolePanel()
        sb.set_console_panel(console)


# ═══════════════════════════════════════════════════════════════════════
#  ToolbarPanel
# ═══════════════════════════════════════════════════════════════════════

class TestToolbarPanel:

    def test_creation(self):
        tb = ToolbarPanel()
        assert tb is not None

    def test_is_editor_panel(self):
        tb = ToolbarPanel()
        assert tb.is_open()
        assert tb.get_window_id() == "toolbar"

    def test_set_open(self):
        tb = ToolbarPanel()
        tb.set_open(False)
        assert not tb.is_open()

    def test_play_callbacks(self):
        tb = ToolbarPanel()
        called = {"play": False, "pause": False, "step": False}

        tb.on_play = lambda: called.__setitem__("play", True)
        tb.on_pause = lambda: called.__setitem__("pause", True)
        tb.on_step = lambda: called.__setitem__("step", True)

        # Invoking from C++ side requires render context, but we can
        # at least verify callbacks are set without crash
        assert tb.on_play is not None
        assert tb.on_pause is not None
        assert tb.on_step is not None

    def test_get_play_state_callback(self):
        tb = ToolbarPanel()
        tb.get_play_state = lambda: PlayState.Edit
        assert tb.get_play_state() == PlayState.Edit

        tb.get_play_state = lambda: PlayState.Playing
        assert tb.get_play_state() == PlayState.Playing

        tb.get_play_state = lambda: PlayState.Paused
        assert tb.get_play_state() == PlayState.Paused

    def test_get_play_time_str(self):
        tb = ToolbarPanel()
        tb.get_play_time_str = lambda: "01:23.456"
        assert tb.get_play_time_str() == "01:23.456"

    def test_camera_settings_roundtrip(self):
        tb = ToolbarPanel()
        settings = {
            "fov": 75.0,
            "rotation_speed": 0.1,
            "pan_speed": 2.0,
            "zoom_speed": 1.5,
            "move_speed": 10.0,
            "move_speed_boost": 5.0,
        }
        tb.set_camera_settings(settings)
        result = tb.get_camera_settings()
        assert abs(result["fov"] - 75.0) < 0.01
        assert abs(result["rotation_speed"] - 0.1) < 0.01
        assert abs(result["pan_speed"] - 2.0) < 0.01
        assert abs(result["zoom_speed"] - 1.5) < 0.01
        assert abs(result["move_speed"] - 10.0) < 0.01
        assert abs(result["move_speed_boost"] - 5.0) < 0.01

    def test_camera_settings_defaults(self):
        tb = ToolbarPanel()
        result = tb.get_camera_settings()
        assert abs(result["fov"] - 60.0) < 0.01
        assert abs(result["move_speed"] - 5.0) < 0.01

    def test_translate_callback(self):
        tb = ToolbarPanel()
        tb.translate = lambda key: f"[{key}]"
        # Callback is invoked during render; just verify wiring
        assert tb.translate is not None

    def test_grid_callbacks(self):
        tb = ToolbarPanel()
        grid_state = {"on": True}
        tb.is_show_grid = lambda: grid_state["on"]
        tb.set_show_grid = lambda v: grid_state.__setitem__("on", v)
        assert tb.is_show_grid()
        tb.set_show_grid(False)
        assert not tb.is_show_grid()

    def test_sync_camera_from_engine(self):
        tb = ToolbarPanel()
        tb.sync_camera_from_engine = lambda: {
            "fov": 90.0,
            "rotation_speed": 0.1,
            "pan_speed": 2.0,
            "zoom_speed": 1.0,
            "move_speed": 5.0,
            "move_speed_boost": 3.0,
        }
        # Will be invoked during render when camera popup opens

    def test_apply_camera_to_engine(self):
        applied = {}
        tb = ToolbarPanel()
        tb.apply_camera_to_engine = lambda d: applied.update(d)
        # Setting camera should invoke the apply callback
        tb.set_camera_settings({"fov": 45.0})
        assert abs(applied.get("fov", 0) - 45.0) < 0.01


# ═══════════════════════════════════════════════════════════════════════
#  MenuBarPanel
# ═══════════════════════════════════════════════════════════════════════

class TestMenuBarPanel:

    def test_creation(self):
        mb = MenuBarPanel()
        assert mb is not None

    def test_scene_file_callbacks(self):
        mb = MenuBarPanel()
        calls = []
        mb.on_save = lambda: calls.append("save")
        mb.on_new_scene = lambda: calls.append("new")
        mb.on_request_close = lambda: calls.append("close")

        mb.on_save()
        mb.on_new_scene()
        mb.on_request_close()
        assert calls == ["save", "new", "close"]

    def test_undo_callbacks(self):
        mb = MenuBarPanel()
        mb.can_undo = lambda: True
        mb.can_redo = lambda: False
        assert mb.can_undo()
        assert not mb.can_redo()

        calls = []
        mb.on_undo = lambda: calls.append("undo")
        mb.on_redo = lambda: calls.append("redo")
        mb.on_undo()
        mb.on_redo()
        assert calls == ["undo", "redo"]

    def test_window_management_callbacks(self):
        mb = MenuBarPanel()

        wti = WindowTypeInfo()
        wti.type_id = "console"
        wti.display_name = "Console"
        wti.singleton = True

        mb.get_registered_types = lambda: [wti]
        mb.get_open_windows = lambda: {"console": True}

        types = mb.get_registered_types()
        assert len(types) == 1
        assert types[0].type_id == "console"
        assert types[0].display_name == "Console"
        assert types[0].singleton is True

        windows = mb.get_open_windows()
        assert windows["console"] is True

    def test_open_close_window(self):
        mb = MenuBarPanel()
        calls = []
        mb.open_window = lambda tid: calls.append(("open", tid))
        mb.close_window = lambda tid: calls.append(("close", tid))
        mb.open_window("inspector")
        mb.close_window("console")
        assert calls == [("open", "inspector"), ("close", "console")]

    def test_reset_layout(self):
        mb = MenuBarPanel()
        called = [False]
        mb.reset_layout = lambda: called.__setitem__(0, True)
        mb.reset_layout()
        assert called[0]

    def test_close_requested_callback(self):
        mb = MenuBarPanel()
        mb.is_close_requested = lambda: False
        assert not mb.is_close_requested()

    def test_floating_panel_toggles(self):
        mb = MenuBarPanel()
        state = {"bs": False, "pref": False, "phys": False}

        mb.is_build_settings_open = lambda: state["bs"]
        mb.is_preferences_open = lambda: state["pref"]
        mb.is_physics_layer_matrix_open = lambda: state["phys"]

        mb.toggle_build_settings = lambda: state.__setitem__("bs", not state["bs"])
        mb.toggle_preferences = lambda: state.__setitem__("pref", not state["pref"])
        mb.toggle_physics_layer_matrix = lambda: state.__setitem__("phys", not state["phys"])

        assert not mb.is_build_settings_open()
        mb.toggle_build_settings()
        assert mb.is_build_settings_open()

    def test_translate_callback(self):
        mb = MenuBarPanel()
        mb.translate = lambda key: f"<<{key}>>"
        assert mb.translate("menu.project") == "<<menu.project>>"


# ═══════════════════════════════════════════════════════════════════════
#  PlayState enum
# ═══════════════════════════════════════════════════════════════════════

class TestPlayState:

    def test_values(self):
        assert PlayState.Edit is not None
        assert PlayState.Playing is not None
        assert PlayState.Paused is not None

    def test_distinct(self):
        assert PlayState.Edit != PlayState.Playing
        assert PlayState.Playing != PlayState.Paused
        assert PlayState.Edit != PlayState.Paused


# ═══════════════════════════════════════════════════════════════════════
#  WindowTypeInfo
# ═══════════════════════════════════════════════════════════════════════

class TestWindowTypeInfo:

    def test_creation(self):
        wti = WindowTypeInfo()
        assert wti.type_id == ""
        assert wti.display_name == ""
        assert wti.singleton is True

    def test_readwrite(self):
        wti = WindowTypeInfo()
        wti.type_id = "hierarchy"
        wti.display_name = "Hierarchy"
        wti.singleton = False
        assert wti.type_id == "hierarchy"
        assert wti.display_name == "Hierarchy"
        assert wti.singleton is False
