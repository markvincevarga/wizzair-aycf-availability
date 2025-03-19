FROM debian:stable-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl ghostscript ca-certificates && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

CMD ["bash", "-c", "cd /app && /root/.local/bin/uv run main.py"]
