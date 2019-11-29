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

Deploy the compose file as a stack

```
docker stack deploy -c docker-compose.yml mystack
```


# Mistakes made during this project

1. I referred to hostnames in code & config, this was a mistake because with docker stack you can connect via the service name which is load balanced, so basically we don't need to worry about hostname for most cases.
