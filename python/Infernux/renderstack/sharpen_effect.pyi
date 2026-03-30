"""Type stubs for Infernux.renderstack.sharpen_effect."""

from __future__ import annotations

from typing import ClassVar, List, TYPE_CHECKING

from Infernux.renderstack.fullscreen_effect import FullScreenEffect

if TYPE_CHECKING:
    from Infernux.rendergraph.graph import RenderGraph
    from Infernux.renderstack.resource_bus import ResourceBus


class SharpenEffect(FullScreenEffect):
    """Contrast Adaptive Sharpening (CAS) post-processing effect.

    AMD FidelityFX CAS-inspired — enhances local contrast without
    visible halos.  Placed after tone mapping to sharpen the final LDR image.

    Attributes:
        intensity: Sharpening strength (0 = off, 1 = maximum).
    """

    name: ClassVar[str]
    injection_point: ClassVar[str]
    default_order: ClassVar[int]
    menu_path: ClassVar[str]

    intensity: float

    def get_shader_list(self) -> List[str]: ...
    def setup_passes(self, graph: RenderGraph, bus: ResourceBus) -> None: ...
