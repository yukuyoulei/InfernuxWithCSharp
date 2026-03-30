"""Per-frame scheduler renderable (no window, no UI)."""

from typing import TYPE_CHECKING
from Infernux.lib import InxGUIRenderable, InxGUIContext

if TYPE_CHECKING:
    from Infernux.engine import Engine


class FrameSchedulerPanel(InxGUIRenderable):
    """Runs engine-wide per-frame tasks exactly once per frame."""

    def __init__(self, engine: 'Engine' = None):
        super().__init__()
        self._engine = engine

    def set_engine(self, engine: 'Engine'):
        self._engine = engine

    def on_render(self, ctx: InxGUIContext):
        # DeferredTaskRunner is now ticked by InxRenderer's pre-GUI callback
        # (before BuildFrame) so that scene-mutating steps complete before
        # any ImGui panel renders.  See Engine.run().

        if self._engine:
            try:
                self._engine.tick_play_mode()
            except Exception as exc:
                from Infernux.debug import Debug
                Debug.log_error(f"Frame tick error: {exc}")
