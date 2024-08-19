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
Now you can open [http://localhost:5000](http://localhost:5000). And you are all good to go!

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
API_TOKEN=<API-token-from-ipinfo.io>
```

Get your API token from [here.](https://ipinfo.io/).

Run the following command,

```bash
docker-compose up -d
```
This will spin up two containers; a container running the gunicorn WSGI server on port 8000(mapped to localhost) and a container with postgreSQL database.
Now, configure nginx as a proxy server and install a SSL cetificate using certbot and you're all done!
For data safety, set up cronjobs for backup and restore of databse.


# Database Backup & Restore

## Initialization Scripts
Initialization scripts located in the `db_init` directory are executed in alphabetical order when the PostgreSQL container starts. This ensures that scripts are run in the specified sequence, enabling proper database setup.

## Backup

### Using `pg_dump`
To create a backup of a PostgreSQL database with `pg_dump`, use the following command. This will generate a `plain-text` SQL file without ownership information:

```sh
pg_dump -U <user> -h <database-host> -d <database-name> --no-owner -f 01_backup.sql
```

- `-U`: PostgreSQL username
- `-h`: Hostname of the PostgreSQL server
- `-d`: Name of the database to back up
- `--no-owner`: Excludes ownership information from the backup
- `-f`: Specifies the output file

### Using `snap_db.sh`
You can also use the provided `snap_db.sh` script to automate the backup process. This script generates a `plain-text` SQL file without ownership information and stores it in the `backups` directory, which is mapped to the `backups` volume in the Docker container.

#### Making the Script Executable
Before running the script, ensure it is executable by using the following command:

```sh
chmod +x snap_db.sh
```

#### Running the Backup Script
After making it executable, you can take a backup with the following command:

```sh
./snap_db.sh
```
This will create a backup file with the current date in the filename, stored in the `backups` directory.

#### Backup Script Explanation
- The backup file is generated using `pg_dump` and saved in the format `db_backup<date>.sql`.
- The `snap_db.sh` script is designed to store backups in the `backups` directory located at the root of your repository.
- The `--no-owner` flag ensures that ownership information is excluded from the backup.

## Restore

### Using `pg_restore`
To restore the database, you can manually place the `01_backup.sql` file in the `db_init` directory, which will be executed when the PostgreSQL container starts. Alternatively, you can use the `pg_restore` command:

```sh
pg_restore -U <user> -h <database-host> -d <database-name> -1 01_backup.sql
```

### Steps to Restore using `snap_db.sh`
1. Rename the desired backup file from the `backups` directory to `01_backup.sql`.
2. Place the renamed file in the `db_init` directory.
3. Run the Docker Compose setup:
    ```sh
    docker-compose up -d
    ```
   The PostgreSQL container will detect the `01_backup.sql` file and execute it, restoring the database.

### Important Notes
- Ensure the backup file is in `plain-text` format.
- Only one backup file should be in the `db_init` directory at a time for proper restoration.
