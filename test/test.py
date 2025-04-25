#!/usr/bin/env python3
# Sample test script

from sys import path
path.append("/mnt/libcitadel")

from citadel.incus.containers import create_instance, get_containers, run_in_container, stop_container, start_container, attach_network
from citadel.incus.networking import create_network

from random import choices
from string import ascii_uppercase
from os import getuid
from time import sleep

containers = get_containers()
print(f"Containers are: {containers}")

container_name = ''.join(choices(ascii_uppercase, k=8))

print(f"Creating new container with name {container_name}")
create_instance(container_name, "debian", ["protected", "citadel", "backup", "rootdisk", "security", "x11", "pulseaudio", "gpu"])
print("Done creating container")

network_name = ''.join(choices(ascii_uppercase, k=8))
print(f"Creating new network with name {network_name}")
create_network(network_name, "bridge")
print("Done creating bridge")

print("Attaching container to network")
attach_network(container_name, network_name, )
print("Done")

print("Starting container")
start_container(container_name)
print("Started containers")

print("Running mousepad")
run_in_container(container_name, ["/sbin/entrypoint", "1000", "mousepad"])
