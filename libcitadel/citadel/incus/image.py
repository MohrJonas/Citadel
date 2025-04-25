from subprocess import run

def import_image(incus_file_path: str, rootfs_file_path: str, alias: str) -> None:
    run(["incus", "image", "import", incus_file_path, rootfs_file_path, "--alias", alias, "--reuse"], check=True)