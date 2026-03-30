---
category: Tutorials
tags: ["coroutines", "timing"]
---

# Coroutines and Time

Coroutines let you express delayed or multi-frame behavior without turning everything into state-machine boilerplate. Timing utilities live alongside the coroutine system so frame-based logic stays readable.

## Common tools

- [Coroutine](../api/Coroutine.md)
- [WaitForSeconds](../api/WaitForSeconds.md)
- [WaitForSecondsRealtime](../api/WaitForSecondsRealtime.md)
- [WaitUntil](../api/WaitUntil.md)
- [WaitWhile](../api/WaitWhile.md)
- [Time](../api/Time.md)

## Typical uses

- Delayed VFX or SFX playback.
- Cooldowns, invulnerability windows, and staged interactions.
- Multi-frame polling of gameplay conditions.
