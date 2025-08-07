# Open WebUI

## Project Overview

Open WebUI is a self-hosted, extensible, and user-friendly AI platform designed for offline operation. It integrates with various LLM runners like Ollama and OpenAI-compatible APIs and includes a built-in inference engine for Retrieval-Augmented Generation (RAG). The project is architected with a SvelteKit/Vite frontend and a Python/FastAPI backend, containerized using Docker for easy deployment.

**Key Technologies:**

*   **Frontend:** SvelteKit, Vite, TypeScript, Tailwind CSS
*   **Backend:** Python, FastAPI, SQLAlchemy
*   **Deployment:** Docker, Docker Compose
*   **AI/ML:** Ollama, OpenAI, ONNX, various embedding and reranking models

## Building and Running

### Development

To run the application in a development environment, use the following command:

```bash
npm run dev
```

This command starts the Vite development server for the frontend and likely relies on a concurrently running backend.

### Production Build

To build the application for production, use the following command:

```bash
npm run build
```

This command creates an optimized build of the frontend in the `build` directory.

### Docker

The project provides several `docker-compose` files for different deployment scenarios. The primary way to run the application is with Docker.

**Running with Docker:**

```bash
docker-compose up -d
```

This command will start the application based on the configuration in `docker-compose.yaml`.

## Development Conventions

### Linting and Formatting

The project uses ESLint for frontend linting and Prettier for code formatting. To lint and format the code, use the following commands:

*   **Lint:** `npm run lint`
*   **Format:** `npm run format`

### Backend Development

The backend is a Python/FastAPI application. To run the backend for development, you would typically navigate to the `backend` directory and use a command like:

```bash
uvicorn open_webui.main:app --reload
```

However, it's recommended to use the provided Docker setup for a more consistent environment.

### Testing

The project includes frontend tests that can be run with:

```bash
npm run test:frontend
```

Backend tests are likely run using `pytest`, but a specific command is not immediately apparent from the provided files.
