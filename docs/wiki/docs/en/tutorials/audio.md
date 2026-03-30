---
category: Tutorials
tags: ["audio"]
---

# Audio in Infernux

Audio playback is component-based. Use [AudioSource](../api/AudioSource.md) to emit sound, [AudioListener](../api/AudioListener.md) to define the listening point, and [AudioClip](../api/AudioClip.md) assets as the source data.

## Typical workflow

1. Import or reference an audio asset.
2. Add an `AudioSource` to the object that should emit sound.
3. Ensure the active camera or player rig has an `AudioListener`.
4. Configure looping, volume, and 3D playback behavior.
5. Trigger playback from gameplay code.

## Related API

- [AudioSource](../api/AudioSource.md)
- [AudioListener](../api/AudioListener.md)
- [AudioClip](../api/AudioClip.md)
