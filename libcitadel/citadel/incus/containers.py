from typing import Any, Optional
from subprocess import run, PIPE
from itertools import chain
from os import linesep
from typing import cast
from time import sleep

from citadel.utils.subprocess import run_json

class Container:
    def __init__(self, instance_json: Any) -> None:
        self.raw = instance_json
        self.name = instance_json["name"]
        self.state = instance_json["state"]["status"]
        expanded_devices = instance_json["expanded_devices"]
        network_device = next(filter(lambda device: device["type"] == "nic", expanded_devices.values()), None)
        self.network_name = network_device["network"] if network_device else None
        self.profiles = cast(list[str], instance_json["profiles"])

def get_containers() -> list[Container]:
    containers_json = run_json(["incus", "list", "--format", "json"])
    return list(map(lambda container_json: Container(container_json), containers_json))

def create_instance(container_name: str, image_name: str, profile_names: Optional[list[str]] = None) -> Container:
    profile_parameters = chain(*map(lambda profile_name: ["--profile", profile_name], profile_names)) if profile_names is not None else []
    run(["incus", "create", image_name, container_name, "--no-profiles", *profile_parameters], check=True)
    return list(filter(lambda container: container.name == container_name, get_containers()))[0]

def attach_network(container_name: str, network_name: str) -> Container:
    run(["incus", "network", "attach", network_name, container_name], check=True)
    return list(filter(lambda container: container.name == container_name, get_containers()))[0]

def start_container(container_name: str) -> None:
    run(["incus", "start", container_name], check=True)
    # Wait a short delay to make sure the instance is booted
    sleep(1)

def stop_container(container_name: str) -> None:
    run(["incus", "stop", container_name], check=True)

def open_shell_in_container(container_name: str) -> None:
    run(["xfce4-terminal", "-x", "incus", "shell", container_name], check=True)

def run_in_container(container_name: str, command: list[str], user: int = 0) -> None:
    run(["incus", "exec", "--user", str(user), container_name, "--", *command], check=True)

def run_in_container_capturing(container_name: str, command: list[str], user: int = 0) -> str:
    output = run(["incus", "exec", "--user", str(user), container_name, "--", *command], check=True, stdout=PIPE)
    return output.stdout.decode("utf-8").strip()

def run_in_container_capturing_exitcode(container_name: str, command: list[str], user: int = 0) -> int:
    output = run(["incus", "exec", "--user", str(user), container_name, "--", *command])
    return output.returncode

def list_files_in_directory(container_name: str, folder_path: str) -> list[str]:
    return run_in_container_capturing(container_name, ["find", folder_path, "-maxdepth", "1", "-type", "b,c,p,f,l,s"]).split(linesep)

def get_file_content(container_name: str, file_path: str) -> str:
    return run_in_container_capturing(container_name, ["cat", file_path])

def get_file_content_binary(container_name: str, file_path: str) -> bytes:
    output = run(["incus", "file", "pull", f"{container_name}{file_path}", "-"], check=True, stdout=PIPE)
    return output.stdout

def is_path_directory(container_name: str, file_path: str) -> bool:
    return run_in_container_capturing_exitcode(container_name, ["test", "-d", file_path]) == 0

def is_path_file(container_name: str, file_path: str) -> bool:
    return run_in_container_capturing_exitcode(container_name, ["test", "-f", file_path]) == 0

def does_path_exist(container_name: str, file_path: str) -> bool:
    return run_in_container_capturing_exitcode(container_name, ["test", "-e", file_path]) == 0