import os
import time
from typing import Generator


def html_handler(file: str) -> str:
    try:
        with open(os.path.join("images", f"{file}.html"), "r") as f:
            return f.read()
    except FileNotFoundError:
        print("HTML file not found")
        return ""
    except PermissionError:
        print("Permission denied")
        return ""
    except (OSError, IOError):
        print("OSError")
        return ""


def image_handler(file: str, extension: str = "png") -> bytes:
    try:
        with open(os.path.join("images", f"{file}.{extension}"), "rb") as f:
            return f.read()
    except FileNotFoundError:
        print("Image not found")
        return ""
    except PermissionError:
        print("Permission denied")
        return ""
    except (OSError, IOError):
        print("OSError")
        return ""


def large_txtfile_handler(file: str) -> Generator[str, None, None]:
    try:
        with open(os.path.join("text", f"{file}.txt"), "r") as f:
            data = f.read()
        for word in data.split(" "):
            yield word + " "
            time.sleep(0.16)
    except FileNotFoundError:
        print("TXT file not found")
        yield ""
    except PermissionError:
        print("Permission denied")
        yield ""
    except (OSError, IOError):
        print("OSError")
        yield ""


def txtfile_handler(file: str) -> str:
    try:
        with open(os.path.join("text", f"{file}.txt"), "r") as f:
            return f.read()
    except FileNotFoundError:
        print("TXT file not found")
        return ""
    except PermissionError:
        print("Permission denied")
        return ""
    except (OSError, IOError):
        print("OSError")
        return ""

def load_css(name: str) -> str:
    # loading css put in a html format
    try:
        with open(os.path.join("css", f"{name}.html"), "r") as f:
            return f.read()
    except FileNotFoundError:
        print("CSS file not found")
        return ""
    except PermissionError:
        print("Permission denied")
        return ""
    except (OSError, IOError):
        print("OSError")
        return ""