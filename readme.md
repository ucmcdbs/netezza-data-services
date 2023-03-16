# Netezza Data Services API

Wrap analytical queries using Python and expose as services.

## Setup
```
pip install -r requirements.txt
```

## Run
```
gunicorn -b localhost:8800 main:api
```

Daemonize
```
gunicorn -b localhost:8800 --daemon main:api
```

## Run (Windows)
Install Waitress
```
pip install waitress
```

Run
```
waitress-serve --listen=localhost:8800 main:api
```

## Test
```
curl -u "username:password" localhost:8800/stores/1/sales
curl -u "username:password" localhost:8800/stores/1/sales?from=2023-01-01&to=2023-01-31
```
