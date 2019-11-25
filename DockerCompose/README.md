# Docker Compose Notes

To build the custom images...

```
docker-compose build
```

To start the setup

```
docker-compose up -d
```

To destroy the setup including volumes

```
docker-compose down -v
```

Access a running container...

```
docker exec -ti dockercompose_web_1 sh
```

Execute a call against the bundled postcode api

```
curl http://localhost:80?postcode=sl71uq
```

Check logs for a container

```
docker container logs dockercompose_web_1
```
