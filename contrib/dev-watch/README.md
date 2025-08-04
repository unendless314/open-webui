# Manual Docker Updates for Development

This guide explains how to refresh a local Open WebUI environment when not using file-watch tools.

## Refresh the Running Container

The application source is baked into the Docker image. A `git pull` updates the host files but **does not** update a running container. After pulling new code, rebuild the image and recreate the container:

```bash
git pull
docker compose build open-webui
docker compose up -d --no-deps --force-recreate open-webui
# or
docker compose up -d --build open-webui
```

## Rebuild When Dependencies Change

If `package.json`, `pyproject.toml`, or other dependencies change, the above rebuild step is required before recreating the container.

## Optional: Live Code with Bind Mounts

For immediate code reflection without rebuilding, create a `docker-compose.override.yml` with a bind mount:

```yaml
# docker-compose.override.yml
services:
  open-webui:
    volumes:
      - .:/app
```

`docker compose up -d open-webui` will then use the local source directly.

## Guardrails

- **Avoid** running `docker compose down -v`; it deletes volumes and data.
- **Do not** remove `/app/backend/data`; this directory stores persistent application data.
