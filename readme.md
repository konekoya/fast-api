# FastAPI

## About

An API server that was built with [FastAPI](https://fastapi.tiangolo.com/). This was originally a Python course that I took from freecodecamp and later adapted myself in order to create a real world service. There's also a [web UI](https://github.com/konekoya/fastapi-dashboard) for this. The app is currently [deployed](https://konekoya.herokuapp.com/) on [Heroku](https://id.heroku.com/login)

## Prerequisites

- Python 3.11
- pip3
- PostgreSQL 14.6
- Heroku CLI 8

## Development

1. Ensure you're in the venv environment, if not, run the following from the root dir:

```sh
source venv/bin/activate
```

2. Install packages

```sh
pip3 install -r requirements.txt
```

3. Start the server with:

```sh
uvicorn app.main:app --reload
```

By default, the app will run on `http://localhost:8000`, a hello world route has been setup for testing when you visit the root route of `/`:

```json
{
  "message": "hello, world"
}
```

All available APIs can be found at `/docs` route. You can also test the APIs directly since it's a [swagger](https://swagger.io/) docs.

## Production

The app is currently deployed on [Heroku](https://id.heroku.com/login). Check out the [Procfile](/Procfile) for the configuration. The Database is an Postgres instance running on [render](https://render.com/)
