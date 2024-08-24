# Clickstat

Clickstat is a URL shortener with IP and GPS logging. It logs information like IP address User-Agent and GPS-Coordinates if GPS Tracking is enabled.
Access it at [clickstat.xyz](https://clickstat.xyz)

## Features

1. IP Logging
2. User-Agent Logging
3. GPS Coordinates Loggin
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
The root directory contains an `app` folder with all the flask app source files. 
For ease, we recommend running clickstat with docker. 
clickstat uses postgreSQL for database and ipinfo.io API for ip lookup. 
To set databse and API credential, create a `.env` file in the root directory and put the following content:

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

### Understanding Initialization Scripts in PostgreSQL
In the `db` service defined in the Docker Compose file, the `db_init` folder is mapped to the `/docker-entrypoint-initdb.d/` directory inside the PostgreSQL container. The PostgreSQL image automatically executes any scripts placed in this directory in alphanumerical order when the container starts. This mechanism is useful for tasks like setting up databases, creating tables, and restoring data from backups.

### Restoring with Initialization Scripts
To restore the database using this feature, follow these steps:

1. **Prepare the Backup File**: Rename the desired backup file from the `backups` directory to `01_backup.sql`. This ensures that the file is executed first, as scripts in the `db_init` directory are run alphabetically.

2. **Place the File in the `db_init` Directory**: Move the `01_backup.sql` file to the `db_init` directory. Since this folder is mapped to `/docker-entrypoint-initdb.d/` in the PostgreSQL container for the `db` service, the script will be automatically executed on startup.

3. **Run the Docker Compose Setup**: Start the Docker Compose setup:
    ```sh
    docker-compose up -d
    ```
   The PostgreSQL container in the `db` service will detect the `01_backup.sql` file in the `/docker-entrypoint-initdb.d/` directory and execute it automatically, restoring the database.

### Important Notes
- Ensure the backup file is in `plain-text` format.
- Only one backup file should be in the `db_init` directory at a time for proper restoration.
