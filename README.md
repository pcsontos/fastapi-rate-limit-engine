# fastapi-rate-limit-engine

Distributed API rate limiting engine built with FastAPI, Redis and atomic Lua scripts. Five pluggable algorithms: token bucket, leaking bucket, fixed window, sliding window log, sliding window counter.

## Development

Requires [uv](https://docs.astral.sh/uv/). Python 3.12 or later is installed by uv if it is missing.

```sh
uv sync                  # install dependencies
uv run ruff check .      # lint
uv run ruff format .     # format
uv run pyright           # type check (strict)
uv run pytest            # test
```
