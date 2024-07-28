# Clickstat
![preview](https://github.com/Itsmmdoha/clickstat/assets/70005698/c25de049-b2bc-48f5-9a3f-20b1c6b99f8a)
Clickstat is 
a URL shortener with IP and GPS logging. It logs information like IP address User-Agent and GPS-Coordinates if GPS Tracking is enabled.
Access it at [clickstat.xyz](https://clickstat.xyz)

## Features

1. IP Logging
2. User-Agent Logging
3. GPS Loggin
4. IP lookup

## Contribute

clone the repository

```bash
git clone https://github.com/itsmmdoha/clickstat
```

cd into the root directory

```bash
cd clickstat
```
The root directory contains an `app` folder will all the flask source files. 
For ease, we recommend running the dev environment with docker. 
clickstat uses postgreSQL for database and ipinfo.io API for ip lookup. 
To set databse and API credential, create a `.env` file in the root directory and put the following content:

```env
# Database Credentials
PGPASSWORD=testPassword
PGUSER=HoundSec
PGPORT=5432
PGDATABASE=clickstat
# API Token
API_TOKEN=random_value_123456 #optional
```

if you want the ip lookup feature to work, put a real API key in the API_TOKEN variable.
Get your API token from [here.](https://ipinfo.io/).

To start the dev environment, make sure you have docker and docker compose installed and run the following command

```bash
docker-compose -f dev-compose.yaml up --build
```
This will spin up two containers; a container running the flask app and a container with postgreSQL database.
And you are all good to go!

# Deployment

clone the repository

```bash
git clone https://github.com/itsmmdoha/clickstat
```

cd into the root directory

```bash
cd clickstat
```
The root directory contains an `app` folder will all the flask source files. 
For ease, we recommend running the dev environment with docker. 
clickstat uses postgreSQL for database and ipinfo.io API for ip lookup. 
To set databse and API credential, create a `.env` file in the roo directory and put the following content:

```env
# Database Credentials
PGPASSWORD=<set-a-database-password>
PGUSER=HoundSec 
PGPORT=5432
PGDATABASE=clickstat
# API Token
API_TOKEN=<API-token-from-ipinfo.ip>
```

Get your API token from [here.](https://ipinfo.io/).

Run the following command,

```bash
docker-compose up 
```
This will spin up two containers; a container running the gunicorn WSGI server on port 8000(mapped to localhost) and a container with postgreSQL database.
Now, configure nginx as a proxy server and install a SSL cetificate using certbot and you're all done!
For data safety, set up cronjobs for backup and restore of databse.
