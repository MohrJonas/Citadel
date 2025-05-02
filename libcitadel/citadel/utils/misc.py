from typing import Sized, Optional

from os.path import splitext, relpath, join
from os import listdir, walk

def replace_file_ending(path: str, new_extension: str) -> str:
    return f"{splitext(path)[0]}{new_extension}"

def prepend_to_path(path: str, to_prepend: str) -> str:
    return join(to_prepend, relpath(path, "/"))

def list_dir_absolute(folder_path: str) -> list[str]:
    return list(map(lambda path: join(folder_path, path), listdir(folder_path)))

def walk_absolute(folder_path: str) -> list[str]:
    paths = []
    for root, _, fnames in walk(folder_path):
        paths.extend([join(root, fname) for fname in fnames])
    return paths

def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
    
def read_file_binary(file_path: str) -> bytes:
    with open(file_path, "rb") as file:
        return file.read()
    
def first_or_none[T](iterable: Sized) -> Optional[T]:
    if len(iterable) == 0:
        return None
    return iterable[0]