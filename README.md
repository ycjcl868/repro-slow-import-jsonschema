# Slow Import Reproduction

This folder contains a minimal Docker Compose project that reproduces the slow
first-import behaviour we observe for `mcp.types` and the `jsonschema`
package. Both services share the same `Dockerfile` and pin the versions that
are problematic in our production image.

## Prerequisites

- Docker 24+
- Docker Compose V2

## Usage

```bash
# Build the shared base image
docker compose build

# Reproduce the jsonschema import delay (default command)
docker compose run --rm jsonschema

# Reproduce the mcp.types import delay
docker compose run --rm mcp
```

The compose services enforce a low CPU quota (`0.5` cores) and a tight memory
limit (`1g`) to match the constrained hosts where the slowdown is most visible.

### Inspecting detailed import timings

Enable CPython's import profiler to gather the per-module breakdown:

```bash
PYTHONPROFILEIMPORTTIME=1 docker compose run --rm jsonschema
PYTHONPROFILEIMPORTTIME=1 docker compose run --rm mcp
```

The scripts print the wall-clock duration of the target import, while the
profiler dumps the per-module timings to stdout for inclusion in upstream
issues.
