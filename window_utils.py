import os


if os.name == "nt":
    from window_utils_windows import *
elif os.name == "posix":
    from window_utils_linux import *
else:
    raise Exception("Unsupported OS.")
