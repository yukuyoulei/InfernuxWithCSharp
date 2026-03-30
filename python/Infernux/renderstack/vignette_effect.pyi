"""Type stubs for Infernux.renderstack.vignette_effect — screen edge darkening."""

from __future__ import annotations

from typing import ClassVar, List, TYPE_CHECKING

from Infernux.renderstack.fullscreen_effect import FullScreenEffect

if TYPE_CHECKING:
    from Infernux.rendergraph.graph import RenderGraph
    from Infernux.renderstack.resource_bus import ResourceBus


class VignetteEffect(FullScreenEffect):
    """URP-aligned Vignette post-processing effect.

    Darkens screen edges for cinematic framing.

    Attributes:
        intensity: Vignette strength (0 = off, 1 = full black edges).
        smoothness: Falloff softness.
        roundness: Shape control (1 = circular, lower = squared).
        rounded: Force perfectly circular regardless of aspect ratio.
    """

    name: ClassVar[str]
    injection_point: ClassVar[str]
    default_order: ClassVar[int]
    menu_path: ClassVar[str]

    intensity: float
    smoothness: float
    roundness: float
    rounded: bool

    def get_shader_list(self) -> List[str]: ...
    def setup_passes(self, graph: RenderGraph, bus: ResourceBus) -> None: ...
