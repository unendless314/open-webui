# Manual Docker Updates for Development

This guide explains how to refresh a local Open WebUI environment when not using file-watch tools.

## Refresh the Running Container

1. Pull the latest code:
   ```bash
   git pull
   ```
2. Restart the app container:
   ```bash
   docker compose restart open-webui
   ```

## Rebuild When Dependencies Change

If `package.json`, `pyproject.toml`, or other dependencies change, rebuild the image before restarting:

```bash
docker compose build open-webui
docker compose restart open-webui
```

## Guardrails

- **Avoid** running `docker compose down -v`; it deletes volumes and data.
- **Do not** remove `/app/backend/data`; this directory stores persistent application data.
