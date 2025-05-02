from citadel.utils.subprocess import run_json

from subprocess import run
from typing import cast, Any

def create_profile(profile_name: str, contents: str) -> None:
    run(["incus", "profile", "create", profile_name], text=True, input=contents, check=True)

def get_profile_names() -> list[str]:
    return list(map(lambda profile: profile["name"], run_json(["incus", "profile", "list", "--format", "json"])))