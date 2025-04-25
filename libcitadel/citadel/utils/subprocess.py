from typing import Any
from subprocess import run, PIPE
from json import loads

def run_json(command: list[str]) -> Any:
    command_result = run(command,  stdout=PIPE, check=True)
    return loads(command_result.stdout.decode("utf-8"))