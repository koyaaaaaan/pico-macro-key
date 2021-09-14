# FileCopyrightText: 2021 Koyaaaaaan
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.keyboard_layout_jp.KeyboardLayoutJP`
=======================================================

* Author(s): Koyaaaaaan
"""

from .keycode import Keycode


class KeyboardLayoutJP:
    # 入力文字 / USBコード(JP) / SHIFTありなし
    KEYMAP = [
        ["1", 0x1e ,False],
        ["!", 0x1e ,True],
        ["2", 0x1f ,False],
        ["\"", 0x1f ,True],
        ["3", 0x20 ,False],
        ["#", 0x20 ,True],
        ["4", 0x21 ,False],
        ["$", 0x21 ,True],
        ["5", 0x22 ,False],
        ["%", 0x22 ,True],
        ["6", 0x23 ,False],
        ["&", 0x23 ,True],
        ["7", 0x24 ,False],
        ["'", 0x24 ,True],
        ["8", 0x25 ,False],
        ["(", 0x25 ,True],
        ["9", 0x26 ,False],
        [")", 0x26 ,True],
        ["0", 0x27 ,False],
        ["-", 0x2d ,False],
        ["=", 0x2d ,True],
        ["^", 0x2e ,False],
        ["~", 0x2e ,True],
        ["¥", 0x89 ,False],
        ["|", 0x89 ,True],
        ["\t", 0x002b ,False],
        ["	", 0x002b ,False],
        ["q", 0x14 ,False],
        ["Q", 0x14 ,True],
        ["w", 0x1a ,False],
        ["W", 0x1a ,True],
        ["e", 0x08 ,False],
        ["E", 0x08 ,True],
        ["r", 0x15 ,False],
        ["R", 0x15 ,True],
        ["t", 0x17 ,False],
        ["T", 0x17 ,True],
        ["y", 0x1c ,False],
        ["Y", 0x1c ,True],
        ["u", 0x18 ,False],
        ["U", 0x18 ,True],
        ["i", 0x0c ,False],
        ["I", 0x0c ,True],
        ["o", 0x12 ,False],
        ["O", 0x12 ,True],
        ["p", 0x13 ,False],
        ["P", 0x13 ,True],
        ["@", 0x2f ,False],
        ["`", 0x2f ,True],
        ["[", 0x30 ,False],
        ["{", 0x30 ,True],
        ["a", 0x04 ,False],
        ["A", 0x04 ,True],
        ["s", 0x16 ,False],
        ["S", 0x16 ,True],
        ["d", 0x07 ,False],
        ["D", 0x07 ,True],
        ["f", 0x09 ,False],
        ["F", 0x09 ,True],
        ["g", 0x0a ,False],
        ["G", 0x0a ,True],
        ["h", 0x0b ,False],
        ["H", 0x0b ,True],
        ["j", 0x0d ,False],
        ["J", 0x0d ,True],
        ["k", 0x0e ,False],
        ["K", 0x0e ,True],
        ["l", 0x0f ,False],
        ["L", 0x0f ,True],
        [";", 0x33 ,False],
        ["+", 0x33 ,True],
        [":", 0x34 ,False],
        ["*", 0x34 ,True],
        ["]", 0x32 ,False],
        ["}", 0x32 ,True],
        ["z", 0x1d ,False],
        ["Z", 0x1d ,True],
        ["x", 0x1b ,False],
        ["X", 0x1b ,True],
        ["c", 0x06 ,False],
        ["C", 0x06 ,True],
        ["v", 0x19 ,False],
        ["V", 0x19 ,True],
        ["b", 0x05 ,False],
        ["B", 0x05 ,True],
        ["n", 0x11 ,False],
        ["N", 0x11 ,True],
        ["m", 0x10 ,False],
        ["M", 0x10 ,True],
        [",", 0x36 ,False],
        ["<", 0x36 ,True],
        [".", 0x37 ,False],
        [">", 0x37 ,True],
        ["/", 0x38 ,False],
        ["?", 0x38 ,True],
        ["\\", 0x87 ,False],
        ["_", 0x87 ,True],
        [" ", 0x2c ,False],
        ["\n", 0x28 ,False],
        ["""
""", 0x28 ,False]
    ]

    def __init__(self, keyboard):
        self.keyboard = keyboard

    def write(self, string):
        for char in string:
            keymap = self._char_to_keycode(char)
            if keymap[2]:
                self.keyboard.press(Keycode.SHIFT)
            self.keyboard.press(keymap[1])
            self.keyboard.release_all()

    def _char_to_keycode(self, char):
        for c in self.KEYMAP:
            if c[0] == char:
                return c
        return None
