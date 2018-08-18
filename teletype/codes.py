keys = {
    "lf": "\x0d",  # line feed / enter
    "cr": "\x0a",  # carriage return
    "space": "\x20",
    "ctrl-a": "\x01",
    "ctrl-b": "\x02",
    "ctrl-c": "\x03",
    "ctrl-d": "\x04",
    "ctrl-e": "\x05",
    "ctrl-f": "\x06",
    "ctrl-z": "\x1a",
    "down": "\x1b\x5b\x42",
    "left": "\x1b\x5b\x44",
    "right": "\x1b\x5b\x43",
    "up": "\x1b\x5b\x41",
    "f1": "\x1b\x4f\x50",
    "f2": "\x1b\x4f\x51",
    "f3": "\x1b\x4f\x52",
    "f4": "\x1b\x4f\x53",
    "f5": "\x1b\x4f\x31\x35\x7e",
    "f6": "\x1b\x4f\x31\x37\x7e",
    "f7": "\x1b\x4f\x31\x38\x7e",
    "f8": "\x1b\x4f\x31\x39\x7e",
    "f9": "\x1b\x4f\x32\x30\x7e",
    "f10": "\x1b\x4f\x32\x31\x7e",
    "f11": "\x1b\x4f\x32\x33\x7e",
    "f12": "\x1b\x4f\x32\x34\x7e",
    "backspace": "\x7f",
    "end": "\x1b\x5b\x46",
    "escape": "\x1b",
    "home": "\x1b\x5b\x48",
    "insert": "\x1b\x5b\x32\x7e",
    "page-down": "\x1b\x5b\x36\x7e",
    "page-up": "\x1b\x5b\x35\x7e",
    "super": "\x1b\x5b\x33\x7e",
}

keys_flipped = {v: k for k, v in keys.items()}

colours = {
    "blue": "\033\x5b34m",
    "cyan": "\033\x5b36m",
    "green": "\033\x5b32m",
    "grey": "\033\x5b30m",
    "magenta": "\033\x5b35m",
    "red": "\033\x5b31m",
    "white": "\033\x5b37m",
    "yellow": "\033\x5b33m",
}

highlights = {
    "on-blue": "\033\x5b44m",
    "on-cyan": "\033\x5b46m",
    "on-green": "\033\x5b42m",
    "on-grey": "\033\x5b40m",
    "on-magenta": "\033\x5b45m",
    "on-red": "\033\x5b41m",
    "on-white": "\033\x5b47m",
    "on-yellow": "\033\x5b43m",
}

modes = {
    "blink": "\033\x5b5m",
    "bold": "\033\x5b1m",  # aka increased intensity
    "concealed": "\033\x5b8m",
    "dark": "\033\x5b2m",
    "italic": "\033\x5b3m",  # not widely supported
    "reversed": "\033\x5b7m",
    "strikeout": "\033\x5b9m",
    "underline": "\033\x5b4m",
}

escape_sequences = {
    "\x1b",
    "\x1b\x1b",
    "\x1b\x1b\x5b",
    "\x1b\x1b\x5b\x32",
    "\x1b\x1b\x5b\x33",
    "\x1b\x4f",
    "\x1b\x5b",
    "\x1b\x5b\x31",
    "\x1b\x5b\x31\x35",
    "\x1b\x5b\x31\x36",
    "\x1b\x5b\x31\x37",
    "\x1b\x5b\x31\x38",
    "\x1b\x5b\x31\x39",
    "\x1b\x5b\x32",
    "\x1b\x5b\x32\x30",
    "\x1b\x5b\x32\x31",
    "\x1b\x5b\x32\x32",
    "\x1b\x5b\x32\x33",
    "\x1b\x5b\x32\x34",
    "\x1b\x5b\x33",
    "\x1b\x5b\x35",
    "\x1b\x5b\x36",
}

scan_codes = {
    13: "\x0d",
    27: "\x1b",
    15104: "\x1b\x4f\x50",
    15360: "\x1b\x4f\x51",
    15616: "\x1b\x4f\x52",
    15872: "\x1b\x4f\x53",
    16128: "\x1b\x4f\x31\x35\x7e",
    16384: "\x1b\x4f\x31\x37\x7e",
    16640: "\x1b\x4f\x31\x38\x7e",
    16896: "\x1b\x4f\x31\x39\x7e",
    17152: "\x1b\x4f\x32\x30\x7e",
    17408: "\x1b\x4f\x32\x31\x7e",
    18400: "\x1b\x5b\x48",
    18656: "\x1b\x5b\x41",
    18912: "\x1b\x5b\x35\x7e",
    19424: "\x1b\x5b\x44",
    19936: "\x1b\x5b\x43",
    20448: "\x1b\x5b\x46",
    20704: "\x1b\x5b\x42",
    20960: "\x1b\x5b\x36\x7e",
    21216: "\x1b\x5b\x32\x7e",
    21472: "\x1b\x5b\x33\x7e",
    22272: "\x1b\x4f\x32\x33\x7e",
    34528: "\x1b\x4f\x32\x34\x7e",
}

reset = "\033\x5b0m"
