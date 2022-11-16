# cantasvacashai
Bot para twitter e mastodon que publica o número de vacas que hai por habitante en cada concello galego

## Instalación (docker):

### Construír a imaxe:

```bash
    docker build -t cantasvacashai-imaxe .
```

### Contedor con opcións de exemplo
```bash
    docker run -d --name cantasvacashai-contedor -e TWITTER=true -e T_CONSUMER_KEY='XXXXX' -e T_CONSUMER_SECRET='XXXXX' -e T_ACCESS_KEY='XXXXX' -e T_ACCESS_SECRET='XXXXX'  cantasvacashai-imaxe
```

### Variábeis que acepta
```
TWITTER : true/false # Se queremos habilitar a publicación en twitter. Por defecto false
MASTODON: true/false #Se queremos habilitar a publicación en mastodon. Por defecto false
T_CONSUMER_KEY : Consumer Key de Twitter # Obrigatorio se temos twitter habilitado
T_CONSUMER_SECRET : Consumer Secret de Twitter # Obrigatorio se temos twitter habilitado
T_ACCESS_KEY : Access Key de Twitter # Obrigatorio se temos twitter habilitado
T_ACCESS_SECRET : Access secret de Twitter # Obrigatorio se temos twitter habilitado
M_ACCESS_TOKEN : Access token de Mastodon # Obrigatorio se temos mastodon habilitado
M_API_BASE_URL : Url da instancia de Mastodon. # Por defecto https://botsin.space
DATAFILE : Ruta ao ficheiro que contén os datos. # Por defecto data/vacas_habi.csv
USEDFILE : Ruta ao ficheiro onde se gardan os usados. # Por defecto data/usado.csv
hora : Hora á que queremos que se fagan as publicacións. # Por defecto 22:00
```
