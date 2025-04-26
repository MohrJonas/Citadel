from subprocess import run

def reload_firewall() -> None:
    run(["sudo", "firewall-cmd", "--reload"], check=True)

def add_interface_to_trusted(interface_name: str) -> None:
    run(["sudo", "firewall-cmd", "--zone=trusted", f"--change-interface={interface_name}", "--permanent"], check=True)