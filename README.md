# bencinmonitor / api

## Development

```bash
# sudo ifconfig lo0 alias 10.8.8.8 netmask 255.255.255.255 up

docker build -t bencinmonitor/api .

ls **/*.py | entr docker run --rm -ti -e DEBUG=True -v `pwd`:/usr/src/app \
  --entrypoint python bencinmonitor/api:latest -m unittest **_test.py -v

docker run --rm -ti --name bm_api -p 7766:7766  -e DEBUG=True \
  -v `pwd`:/usr/src/app bencinmonitor/api:latest
```

## Live development

```bash
./bin/production_tunnels.sh

ngrok http 7766 -region eu --hostname dev.bencinmonitor.si

docker run -ti --rm \
  -e MONGO_URL=mongodb://10.8.8.8:27017/bm \
  -e REDIS_URL=redis://@10.8.8.8:6379/1 \
  -e DEBUG=True \
  -v `pwd`:/usr/src/app \
  --entrypoint python bencinmonitor/api:latest -m unittest **_test.py -v

docker run -ti --rm \
  -e MONGO_URL=mongodb://10.8.8.8:27017/bm \
  -e REDIS_URL=redis://@10.8.8.8:6379/1 \
  -e DEBUG=True \
  -v `pwd`:/usr/src/app \
  -p 0.0.0.0:7766:7766 bencinmonitor/api:latest
```

## API Endpoints

## Stations

Examples:

```rest
GET /stations
GET /stations?limit=10
GET /stations?prices=bencin-95,bencin-100,diesel,lpg


GET /stations?near=Kranj

GET /stations?near=Ljubljana&prices=bencin-95

GET /stations?at=14.5058,46.0569
GET /stations?near=Ljubljana&limit=30&max=10000
```

Parameters

- `at` - Coordinates that are used as starting point for search.
- `near` - Location / address that is "geocoded" and then used as starting point.
- `limit` - Limit of records that API provides. By default number is set to `10`. Max is `50`.
- `maxDistance` - Maximum distance from starting point. By default `10000` meters. Max is `50000` meters.

## Other things

- Dates are in `ISO 8601` format.
- Distances are in `meters`.

## Author

- [Oto Brglez](https://github.com/otobrglez)