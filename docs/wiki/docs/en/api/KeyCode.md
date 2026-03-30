# KeyCode

<div class="class-info">
class in <b>Infernux.input</b>
</div>

## Description

Key code constants for keyboard input.

<!-- USER CONTENT START --> description

KeyCode defines integer constants for every keyboard key and mouse button. Pass these values to [Input](Input.md) methods such as `Input.get_key()`, `Input.get_key_down()`, and `Input.get_key_up()` to query specific key states.

Common groups include letter keys (`A`–`Z`), digit keys (`ALPHA0`–`ALPHA9`), function keys (`F1`–`F12`), arrow keys, modifier keys (Shift, Control, Alt), and numpad keys.

<!-- USER CONTENT END -->

## Properties

| Name | Type | Description |
|------|------|------|
| NONE | `int` |  |
| BACKSPACE | `int` |  |
| TAB | `int` |  |
| RETURN | `int` |  |
| ESCAPE | `int` |  |
| SPACE | `int` |  |
| DELETE | `int` |  |
| ALPHA0 | `int` |  |
| ALPHA1 | `int` |  |
| ALPHA2 | `int` |  |
| ALPHA3 | `int` |  |
| ALPHA4 | `int` |  |
| ALPHA5 | `int` |  |
| ALPHA6 | `int` |  |
| ALPHA7 | `int` |  |
| ALPHA8 | `int` |  |
| ALPHA9 | `int` |  |
| A | `int` |  |
| B | `int` |  |
| C | `int` |  |
| D | `int` |  |
| E | `int` |  |
| F | `int` |  |
| G | `int` |  |
| H | `int` |  |
| I | `int` |  |
| J | `int` |  |
| K | `int` |  |
| L | `int` |  |
| M | `int` |  |
| N | `int` |  |
| O | `int` |  |
| P | `int` |  |
| Q | `int` |  |
| R | `int` |  |
| S | `int` |  |
| T | `int` |  |
| U | `int` |  |
| V | `int` |  |
| W | `int` |  |
| X | `int` |  |
| Y | `int` |  |
| Z | `int` |  |
| F1 | `int` |  |
| F2 | `int` |  |
| F3 | `int` |  |
| F4 | `int` |  |
| F5 | `int` |  |
| F6 | `int` |  |
| F7 | `int` |  |
| F8 | `int` |  |
| F9 | `int` |  |
| F10 | `int` |  |
| F11 | `int` |  |
| F12 | `int` |  |
| UP_ARROW | `int` |  |
| DOWN_ARROW | `int` |  |
| LEFT_ARROW | `int` |  |
| RIGHT_ARROW | `int` |  |
| LEFT_SHIFT | `int` |  |
| RIGHT_SHIFT | `int` |  |
| LEFT_CONTROL | `int` |  |
| RIGHT_CONTROL | `int` |  |
| LEFT_ALT | `int` |  |
| RIGHT_ALT | `int` |  |
| LEFT_COMMAND | `int` |  |
| RIGHT_COMMAND | `int` |  |
| KEYPAD0 | `int` |  |
| KEYPAD1 | `int` |  |
| KEYPAD2 | `int` |  |
| KEYPAD3 | `int` |  |
| KEYPAD4 | `int` |  |
| KEYPAD5 | `int` |  |
| KEYPAD6 | `int` |  |
| KEYPAD7 | `int` |  |
| KEYPAD8 | `int` |  |
| KEYPAD9 | `int` |  |
| KEYPAD_PERIOD | `int` |  |
| KEYPAD_DIVIDE | `int` |  |
| KEYPAD_MULTIPLY | `int` |  |
| KEYPAD_MINUS | `int` |  |
| KEYPAD_PLUS | `int` |  |
| KEYPAD_ENTER | `int` |  |
| MINUS | `int` |  |
| EQUALS | `int` |  |
| LEFT_BRACKET | `int` |  |
| RIGHT_BRACKET | `int` |  |
| BACKSLASH | `int` |  |
| SEMICOLON | `int` |  |
| QUOTE | `int` |  |
| BACKQUOTE | `int` |  |
| COMMA | `int` |  |
| PERIOD | `int` |  |
| SLASH | `int` |  |
| CAPS_LOCK | `int` |  |
| INSERT | `int` |  |
| HOME | `int` |  |
| END | `int` |  |
| PAGE_UP | `int` |  |
| PAGE_DOWN | `int` |  |
| PRINT_SCREEN | `int` |  |
| SCROLL_LOCK | `int` |  |
| PAUSE | `int` |  |
| NUM_LOCK | `int` |  |

<!-- USER CONTENT START --> properties

<!-- USER CONTENT END -->

## Example

<!-- USER CONTENT START --> example
```python
from Infernux import InxComponent
from Infernux.input import Input, KeyCode
from Infernux.math import vector3

class KeyCodeDemo(InxComponent):
    def update(self):
        # WASD movement
        move = vector3.zero
        if Input.get_key(KeyCode.W):
            move += vector3.forward
        if Input.get_key(KeyCode.S):
            move -= vector3.forward
        if Input.get_key(KeyCode.A):
            move -= vector3.right
        if Input.get_key(KeyCode.D):
            move += vector3.right
        self.transform.translate(move * 5.0 * self.time.delta_time)

        # Action keys
        if Input.get_key_down(KeyCode.SPACE):
            Debug.log("Jump")
        if Input.get_key_down(KeyCode.ESCAPE):
            Debug.log("Pause")

        # Number keys for item selection
        for i in range(10):
            code = getattr(KeyCode, f"ALPHA{i}")
            if Input.get_key_down(code):
                Debug.log(f"Selected slot {i}")
```
<!-- USER CONTENT END -->

## See Also

<!-- USER CONTENT START --> see_also

- [Input](Input.md) — reads key states using KeyCode values

<!-- USER CONTENT END -->
