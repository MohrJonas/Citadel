from typing import Any
from subprocess import run

from citadel.utils.subprocess import run_json

class Network:
    def __init__(self, network_json: dict[str, Any]) -> None:
        self.raw = network_json
        self.name = self.raw["name"]
        self.type = self.raw["type"]
        self.used_by = self.raw["used_by"]

def get_networks() -> list[Network]:
    networks_json = run_json(["incus", "network", "list", "--format", "json"])
    return list(map(lambda network_json: Network(network_json), networks_json))

def create_network(network_name: str, network_type: str) -> Network:
    run(["incus", "network", "create", network_name, "--type", network_type], check=True)
    return next(filter(lambda network: network.name == network_name, get_networks()))

def remove_network(network_name) -> None:
    run(["incus", "network", "delete", network_name], check=True)