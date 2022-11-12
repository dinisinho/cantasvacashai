# cantasvacashai
Bot twitter @cantasvacashai escrito en python

Publica o número de vacas, habitantes e vacas por habitante dun concello galego.

## Instalación (docker):

```bash
    docker build -t cantasvacashai-imaxe .
```

```bash
    run -d --name cantasvacashai-contedor -e CONSUMER_KEY='XXXXX' -e CONSUMER_SECRET='XXXXX' -e ACCESS_KEY='XXXXX' -e ACCESS_SECRET='XXXXX' -e hora='14:56' cantasvacashai-imaxe
```