"""
Minimal reproduction script that highlights the slow first import of `jsonschema`.

It mirrors the `mcp.types` reproduction so the two issue reports can share the
same docker-compose setup.
"""

from __future__ import annotations

import os
import time


def main() -> None:
    profile_enabled = os.environ.get("PYTHONPROFILEIMPORTTIME") == "1"

    start = time.perf_counter()
    import jsonschema  # noqa: F401

    elapsed = time.perf_counter() - start
    marker = "[profile enabled]" if profile_enabled else ""
    print(f"import jsonschema took {elapsed:.2f}s {marker}")


if __name__ == "__main__":
    main()
