from subprocess import Popen

from citadel.utils.misc import read_file

from os.path import join, exists
from os import makedirs, kill, remove, waitpid, WNOHANG
from signal import SIGINT
from sys import stdout

def get_pid_root_folder_path() -> str:
    return "/var/run/citadel"

def get_pid_file_path_for_name(name: str) -> str:
    return join(get_pid_root_folder_path(), name)

def run_process_async(process_name: str, *args) -> None:
    pid_file = get_pid_file_path_for_name(process_name)
    makedirs(get_pid_root_folder_path(), exist_ok=True)
    process = Popen(*args, stdout=stdout, stderr=stdout)
    with open(pid_file, "w") as file:
        file.write(str(process.pid))

def stop_process(process_name: str) -> None:
    pid_file = get_pid_file_path_for_name(process_name)
    pid = int(read_file(pid_file))
    kill(pid, SIGINT)
    waitpid(pid, WNOHANG)
    remove(pid_file)

def does_process_exist(process_name: str) -> bool:
    return exists(get_pid_file_path_for_name(process_name))