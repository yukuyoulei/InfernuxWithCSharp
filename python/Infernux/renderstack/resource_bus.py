"""
ResourceBus — Transient resource handle dictionary for graph construction.

Created by ``RenderStack.build_graph()``, passed into
``Pipeline.define_topology()`` and each ``Pass.inject()``.
Carries TextureHandle references between pipeline stages and user passes.

Lifecycle::

    RenderStack creates bus
        → Pipeline initialises base resources (color, depth)
        → injection point callbacks pass bus to each Pass
        → RenderStack reads final output from bus

Resource name conventions::

    "color"       — scene color
    "depth"       — scene depth
    custom names  — introduced by Pass ``creates`` declarations
"""

from __future__ import annotations

from typing import Dict, Optional, Set, TYPE_CHECKING

if TYPE_CHECKING:
    from Infernux.rendergraph.graph import TextureHandle


class ResourceBus:
    """Dictionary that carries resource handles during graph construction.

    Passes interact with the bus through their ``requires``, ``modifies``,
    and ``creates`` declarations. Undeclared resources pass through to later
    passes automatically.

    .. note::
        ``modifies`` implies ``requires``. A pass that declares
        ``modifies={"color"}`` both reads and writes ``color``.
    """

    def __init__(
        self, initial: Optional[Dict[str, "TextureHandle"]] = None
    ) -> None:
        self._resources: Dict[str, "TextureHandle"] = dict(initial or {})

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get(self, name: str) -> Optional["TextureHandle"]:
        """Return a resource handle, or ``None`` if it is missing."""
        return self._resources.get(name)

    def set(self, name: str, handle: "TextureHandle") -> None:
        """Set or update a resource handle."""
        self._resources[name] = handle

    def has(self, name: str) -> bool:
        """Return whether a resource exists."""
        return name in self._resources

    @property
    def available_resources(self) -> Set[str]:
        """Return the set of currently available resource names."""
        return set(self._resources.keys())

    def snapshot(self) -> Dict[str, "TextureHandle"]:
        """Return a shallow snapshot of the current resources for debugging."""
        return dict(self._resources)

    # ------------------------------------------------------------------
    # Dunder
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        keys = ", ".join(sorted(self._resources.keys()))
        return f"<ResourceBus [{keys}]>"
