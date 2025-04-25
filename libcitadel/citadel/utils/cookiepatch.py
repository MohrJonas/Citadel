from os import environ
from subprocess import run, PIPE

def patch_cookie() -> None:
    display = environ.get("DISPLAY")
    print(f"Display is {display}")

    result = run(["xauth", "extract", "-", display], stdout=PIPE, check=True)

    cookie_bytes = bytearray(result.stdout)
    cookie_bytes[0] = 0xff
    cookie_bytes[1] = 0xff

    xauth = environ.get("XAUTHORITY")
    print(f"Auth is {xauth}")
    run(["xauth", "merge", xauth, "-"], input=cookie_bytes, check=True)