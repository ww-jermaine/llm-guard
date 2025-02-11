# API

This example demonstrates how to use LLM Guard as an API.

## Usage

## Installation

1. Copy the code from [examples/api](https://github.com/laiyer-ai/llm-guard/tree/main/examples/api)

2. Install dependencies (preferably in a virtual environment)

```sh
pip install -r requirements.txt
```

Or you can use Makefile

```sh
make install
```

3. Run the API locally:

```sh
make run
```

Or you can run it using Docker:

```sh
make run-docker
```

## Configuration

### Environment variables

- `DEBUG` (bool): Enable debug mode
- `CACHE_MAX_SIZE` (int): Maximum number of items in the cache. Default is unlimited.
- `CACHE_TTL` (int): Time in seconds after which a cached item expires. Default is 1 hour.
- `SCAN_FAIL_FAST` (bool): Stop scanning after the first failed check. Default is `False`.

!!! note

    We recommend to enable `SCAN_FAIL_FAST` to avoid unnecessary scans.

### Scanners

You can configure scanners in `scanners.yml` referring to their names and parameters.

Scanners will be executed in the order of configuration.

## Deploy Docker

We have an officially supported image on [Docker Hub](https://hub.docker.com/repository/docker/laiyer/llm-guard-api/general).

### Download Docker image

```sh
docker pull laiyer/llm-guard-api
```

#### Run container with default port

```sh
docker run -d -p 8001:8000 -e DEBUG='false' laiyer/llm-guard-api:latest
```

## Schema

<swagger-ui src="https://raw.githubusercontent.com/laiyer-ai/llm-guard/main/examples/api/openapi.json" />
