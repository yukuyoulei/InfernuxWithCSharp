"""Type stubs for Infernux.ui.ui_image — rectangular image UI element."""

from __future__ import annotations

from Infernux.ui.inx_ui_screen_component import InxUIScreenComponent


class UIImage(InxUIScreenComponent):
    """Screen-space image element rendered from a texture asset.

    Inherits ``x``, ``y``, ``width``, ``height``, ``opacity``,
    ``corner_radius``, ``rotation``, ``mirror_x``, ``mirror_y``
    from ``InxUIScreenComponent``.

    Attributes:
        texture_path: Path to texture asset (drag from Project panel).
        color: Tint color as ``[R, G, B, A]`` (0–1 each).

    Example::

        img = game_object.add_component(UIImage)
        img.texture_path = "Assets/Textures/logo.png"
        img.color = [1.0, 1.0, 1.0, 0.8]
    """

    texture_path: str
    color: list
