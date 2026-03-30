"""ProjectPanel — asset browser with thumbnails and context menus."""

from __future__ import annotations

from typing import Callable, Optional

from Infernux.lib import InxGUIContext
from Infernux.engine.ui.editor_panel import EditorPanel


class ProjectPanel(EditorPanel):
    """File browser for the project's Assets directory."""

    WINDOW_TYPE_ID: str
    WINDOW_DISPLAY_NAME: str

    SCRIPT_TEMPLATE: str
    VERTEX_SHADER_TEMPLATE: str
    FRAGMENT_SHADER_TEMPLATE: str
    MATERIAL_TEMPLATE: str

    HIDDEN_EXTENSIONS: set
    HIDDEN_PREFIXES: set
    IMAGE_EXTENSIONS: set
    ICON_MAP: dict
    THUMBNAIL_MAX_PX: int
    MODEL_EXTENSIONS: set

    def __init__(
        self,
        root_path: str = "",
        title: str = "Project",
        engine: object = None,
    ) -> None: ...

    def save_state(self) -> dict: ...
    def load_state(self, data: dict) -> None: ...

    def set_root_path(self, path: str) -> None: ...
    def set_on_file_selected(self, callback: Callable) -> None: ...
    def set_on_file_double_click(self, callback: Callable) -> None: ...
    def set_engine(self, engine: object) -> None: ...
    def clear_selection(self) -> None: ...
    def on_render_content(self, ctx: InxGUIContext) -> None: ...
