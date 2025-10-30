FROM python:3.12-slim

# Install the packages that exhibit the slow import behaviour.
# Keeping everything in one layer so the reproduction stays minimal.
RUN pip install --no-cache-dir \
    "mcp[cli]==1.13.0" \
    "jsonschema==4.25.1"

WORKDIR /app
COPY scripts ./scripts

# Default command runs the jsonschema case; docker-compose overrides it per service.
CMD ["python", "scripts/run_jsonschema.py"]
