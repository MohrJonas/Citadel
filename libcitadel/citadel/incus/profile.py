from subprocess import run, PIPE

def create_profile(profile_name: str, contents: str) -> None:
    run(["incus", "profile", "create", profile_name], text=True, input=contents, check=True)