# bencinmonitor / api

## Development

```bash
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

docker run -ti --pid=host --name api_test --rm --privileged --net host \
  -e MONGO_URI=mongodb://10.8.8.8:27017/bm \
  -e DEBUG=True -v `pwd`:/usr/src/app \
  --entrypoint python bencinmonitor/api:latest -m unittest **_test.py -v

docker run -ti --rm -e MONGO_URI=mongodb://10.8.8.8:27017/bm -e DEBUG=True -v `pwd`:/usr/src/app \
  -p 0.0.0.0:7766:7766 bencinmonitor/api:latest
```

## API Endpoints

```rest

GET /stations
GET /stations?limit=10
GET /stations?prices=bencin-95,bencin-100,diesel,lpg

```
