# schemaverse_dojo

Rapid deployment tool for [Schemaverse](https://github.com/Abstrct/Schemaverse).

Docker Hub: [https://hub.docker.com/r/frozenfoxx/schemaverse_dojo](https://hub.docker.com/r/frozenfoxx/schemaverse_dojo).

# Requirements

* python 3+
* docker

# Setup

* Install [Docker](https://www.docker.com/).
* `pip3 install schemaverse_dojo`
* Edit the `/etc/schemaverse_dojo/conf/dojo.conf` with your player information.

# Usage

* For normal use, `schemaverse_dojo` will suffice.
* If you wish to override any options in your config file use `-h` to see all overrides.

# Testing

* Create a sample config file, use the environment variables, or arguments to supply player information.
* `cd [cloned repo root]`
* `python3 -m schemaverse_dojo.schemaverse_dojo`

# Docker

This tool can also be run as a Docker container. This assumes the player configuration files are on the host:

```
docker run \
  -it \
  --rm \
  -e CONFIG='/data/dojo.conf' \
  -e PLAYERSCONF='/data/players.conf \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/conf/dir/:/data \
  frozenfoxx/schemaverse_dojo:latest
```

# Legal

This project is licensed under the Apache License v2.0.
