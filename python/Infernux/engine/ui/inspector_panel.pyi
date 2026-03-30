"""InspectorPanel — property inspector for GameObjects and assets."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from Infernux.lib import InxGUIContext
from Infernux.engine.ui.editor_panel import EditorPanel


class InspectorMode(Enum):
    OBJECT = ...
    ASSET = ...
    PREVIEW = ...


class InspectorPanel(EditorPanel):
    """Displays and edits properties of the selected object or asset."""

    WINDOW_TYPE_ID: str
    WINDOW_DISPLAY_NAME: str
    MIN_PROPERTIES_HEIGHT: float
    MIN_RAW_DATA_HEIGHT: float
    SPLITTER_HEIGHT: float

    def __init__(self, title: str = "Inspector", engine: object = None) -> None: ...

    def set_engine(self, engine: object) -> None: ...

    def set_selected_object(self, obj: object) -> None:
        """Set the currently inspected GameObject (or ``None`` to clear).

        Args:
            obj: A ``GameObject`` or ``None``.
        """
        ...

    def set_selected_file(self, file_path: str) -> None:
        """Switch to asset inspector mode for *file_path*."""
        ...

    def set_detail_file(self, file_path: str) -> None:
        """Open a secondary file detail view."""
        ...

    def on_render_content(self, ctx: InxGUIContext) -> None: ...
