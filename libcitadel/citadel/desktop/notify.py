from typing import Optional
from subprocess import run

def show_desktop_notification(summary: str, body: Optional[str] = None, urgency: str = "low"):
    command = ["notify-send", "-u", urgency, summary]
    if body is not None:
        command.append(body)
    run(command)
