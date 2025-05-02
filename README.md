# Citadel OS

## About

Citadel OS is a operating system using incus containers for compartmentalization.  
It is inspired by QubesOS, but makes various changes. These include:

- Citadel OS is **way less secure**:
    - The host still retains network connectivity
    - USB devices are not isolated from the host
    - Certain sockets and files are passed through from the host: the Pulseaudio socket, /dev/dri/renderD128, and if chosen the host's x11 socket
    - There has been **absolutely zero** security auditing
- Citadel OS uses incus containers, rather than full-blown virtual machines
- GPU accelleration is easily obtainable

## Installation

- As a base OS Fedora Everything is used

### In the installer:

- Select the Fedora deskop present and untick everything on the right
- Create a new regular user, making sure the user has uid and gid 1000 (Can be selected under advanced)
- Install the operating system

### After booting into the operating system for the first time:

- Install incus `sudo dnf install incus`
- Install nx* `sudo dnf install nxagent nxdialog`
- Install sshfs `sudo dnf install sshfs`
- Add your user to the incus-admin group `sudo usermod -aG incus-admin $USER`
- Get new group without logout: `newgrp incus-admin`
- Start and enable incus `sudo systemctl enable --now incus.service`
- Add a subgid and subuid range for the root user `sudo usermod -v 1000000-1000999999 -w 1000000-1000999999 root` 
- Restart incus `sudo systemctl restart incus.service`
- Create a new storage called incus that holds the containers `incus storage create citadel <depends on what type, recommended is either btrfs or zfs, see https://linuxcontainers.org/incus/docs/main/explanation/storage/>`
- Install distrobuilder, see https://linuxcontainers.org/distrobuilder/docs/latest/howto/install:
    - `sudo dnf install golang gcc debootstrap rsync gnupg2 squashfs-tools git make hivex genisoimage`
    - `mkdir -p $HOME/go/src/github.com/lxc/`
    - `cd $HOME/go/src/github.com/lxc/`
    - `git clone https://github.com/lxc/distrobuilder`
    - `cd ./distrobuilder`
    - `make`
    - `sudo cp $HOME/go/bin/distrobuilder /sbin/distrobuilder`
    - `sudo chown root:root /sbin/distrobuilder`
    - `sudo chmod 755 /sbin/distrobuilder`
- Clone this repo: `git clone https://github.com/MohrJonas/citadel`
- Run the install script: `./citadel/install`