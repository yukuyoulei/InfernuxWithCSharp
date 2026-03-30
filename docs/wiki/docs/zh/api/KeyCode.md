# KeyCode

<div class="class-info">
类位于 <b>Infernux.input</b>
</div>

## 描述

按键代码枚举，用于标识键盘和鼠标按键。

<!-- USER CONTENT START --> description

KeyCode 定义了每个键盘按键和鼠标按钮的整数常量。将这些值传递给 [Input](Input.md) 的 `Input.get_key()`、`Input.get_key_down()` 和 `Input.get_key_up()` 方法来查询特定按键状态。

常用分组包括字母键（`A`–`Z`）、数字键（`ALPHA0`–`ALPHA9`）、功能键（`F1`–`F12`）、方向键、修饰键（Shift、Control、Alt）和小键盘按键。

<!-- USER CONTENT END -->

## 属性

| 名称 | 类型 | 描述 |
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

## 示例

<!-- USER CONTENT START --> example
```python
from Infernux import InxComponent
from Infernux.input import Input, KeyCode
from Infernux.math import vector3

class KeyCodeDemo(InxComponent):
    def update(self):
        # WASD 移动
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

        # 动作按键
        if Input.get_key_down(KeyCode.SPACE):
            Debug.log("跳跃")
        if Input.get_key_down(KeyCode.ESCAPE):
            Debug.log("暂停")

        # 数字键选择物品栏
        for i in range(10):
            code = getattr(KeyCode, f"ALPHA{i}")
            if Input.get_key_down(code):
                Debug.log(f"选择了槽位 {i}")
```
<!-- USER CONTENT END -->

## 另请参阅

<!-- USER CONTENT START --> see_also

- [Input](Input.md) — 使用 KeyCode 值读取按键状态

<!-- USER CONTENT END -->
