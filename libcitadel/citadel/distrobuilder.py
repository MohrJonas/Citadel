from itertools import chain
from typing import Optional

from pathlib import Path
from subprocess import run

def build_incus_image(yaml_file_path: str, output_folder_path: str, options: Optional[list[str]] = None) -> None:
    option_parameters = chain(*map(lambda option: ["--options", option], options)) if options is not None else []
    parent_dir = Path(yaml_file_path).parent
    run(["distrobuilder", "build-incus", yaml_file_path, output_folder_path, *option_parameters], cwd=parent_dir, check=True)