# Objective mimic UI App

One login panel which takes user name and password. Call the backend service [a docker container within private network]. Check if the result is present shows login successful or else shows user not present.

* APPLICATION_SERVICE_URL = "http://application_layer:8000"

## App overview

* UI (Public network)
* Backend (Private docker internal network)

## Getting up and running

```bash
docker network create web
touch acme.json
chmod 600 acme.json
docker run -d \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $PWD/traefik.toml:/traefik.toml \
  -v $PWD/traefik_dynamic.toml:/traefik_dynamic.toml \
  -v $PWD/acme.json:/acme.json \
  -p 80:80 \
  -p 443:443 \
  --network web \
  --name traefik \
  traefik:v2.2

docker-compose build
docker-compose up
docker-compose down
```

![image info](/ssl_test.png)

__Reference:__

* https://github.com/vercel/next.js/issues/16791
* https://stackoverflow.com/questions/62098417/nextjs-docker-compose-how-to-resolve-container-hostname-client-side
* https://www.digitalocean.com/community/tutorials/how-to-use-traefik-v2-as-a-reverse-proxy-for-docker-containers-on-ubuntu-20-04
