# bencinmonitor / api

## Development

```bash
docker build -t bencinmonitor/api .

ls **/*.py | entr docker run --rm -ti -e DEBUG=True -v `pwd`:/usr/src/app \
  --entrypoint python bencinmonitor/api:latest -m unittest **_test.py -v

docker run --rm -ti --name bm_api -p 7766:7766  -e DEBUG=True \
  -v `pwd`:/usr/src/app bencinmonitor/api:latest
```

## API Endpoints

```rest



```
