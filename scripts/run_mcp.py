"""
Minimal reproduction script that highlights the slow first import of `mcp.types`.

It prints both the total wall time of the import and, when the environment
variable `PYTHONPROFILEIMPORTTIME=1` is present, relies on CPython to emit the
per-module breakdown (so that upstream maintainers can see which modules are
expensive).
"""

from __future__ import annotations

import os
import time


def main() -> None:
    profile_enabled = os.environ.get("PYTHONPROFILEIMPORTTIME") == "1"

    start = time.perf_counter()
    import mcp.types  # noqa: F401  # The side effects of the import are what we care about.

    elapsed = time.perf_counter() - start
    marker = "[profile enabled]" if profile_enabled else ""
    print(f"import mcp.types took {elapsed:.2f}s {marker}")


if __name__ == "__main__":
    main()
