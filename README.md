# Clickstat

Clickstat is a no BS URL shortener with IP and GPS logging. It logs information like IP address User-Agent and GPS-Coordinates if GPS Tracking is enabled.
Access it at [clickstat.xyz](https://clickstat.xyz)

## Features

1. **URL Shortening**: Efficiently convert long URLs into short, shareable links.
  
2. **IP & User-Agent Logging**: Capture IP addresses and user-agent data for each link click.

3. **Optional GPS Tracking**: Enable precise GPS tracking with user consent for enhanced location data.

4. **Real-Time Click Stats**: Access detailed click statistics, including IP, GPS (if enabled), and user-agent, via a unique identifier.

5. **Secure & Private**: Data is securely stored, with no third-party access or sharing.


## APIs Used

**Clickstat** uses the following APIs to enhance its functionality. Both are optional, but certain features depend on them being configured:

1. **Google Safe Browsing API**: Used to check if URLs are malicious or flagged for phishing, malware, or other threats before shortening them. To enable URL verification, you need to include a valid API key and set the `VERIFY_URL` environment variable to `true`. If `VERIFY_URL` is set to `false`, the check will be skipped, which is useful if you don't have access to the API or don't require URL verification.
   
   Get your API key [here.](https://developers.google.com/safe-browsing/v4/get-started)

2. **ipinfo.io API**: This API is used for IP address lookups to gather geographic or other information about users who access shortened links. If you don't provide an API key, the IP lookup feature in the web app will be disabled, but all other features will continue to work normally.

   Get your API key [here.](https://ipinfo.io/)

---

## Contribute

Clone the repository:

```bash
git clone https://github.com/itsmmdoha/clickstat
```

Navigate into the root directory:

```bash
cd clickstat
```

The root directory contains an `app` folder with all the Flask source files. For ease, we recommend running the dev environment with Docker. Clickstat uses PostgreSQL for its database and also integrates with the ipinfo.io API and Google Safe Browsing API for enhanced features.

To set up the database and API credentials, create a `.env` file in the root directory and include the following content:

```env
# Database Credentials
PGPASSWORD=testPassword
PGUSER=HoundSec
PGPORT=5432
PGDATABASE=clickstat
VERIFY_URL=true # set to false to disable URL verification
# API Tokens
IP_INFO_TOKEN=<API token from ipinfo.io> #optional
SAFE_BROWSING_TOKEN=<API token from Google Safe Browsing API> #optional
```

- If the `VERIFY_URL` variable is set to `false`, the Google Safe Browsing check will be skipped. This is useful if you don't have access to the API or don't need URL verification.
- If you don't set the `IP_INFO_TOKEN`, the IP lookup feature will not work, but all other features will continue to function as expected.

To start the development environment, make sure Docker and Docker Compose are installed, then run the following command:

```bash
docker-compose -f dev-compose.yaml up --build
```

This will spin up two containers: one running the Flask app and another running the PostgreSQL database. You can now access the app at [http://localhost:5000](http://localhost:5000).

---

## Deployment

Clone the repository:

```bash
git clone https://github.com/itsmmdoha/clickstat
```

Navigate into the root directory:

```bash
cd clickstat
```

The root directory contains an `app` folder with all the Flask app source files. For ease, we recommend running clickstat with Docker. Clickstat uses PostgreSQL for its database, the ipinfo.io API for IP lookup, and the Google Safe Browsing API for URL security checks.

To set up the database and API credentials, create a `.env` file in the root directory with the following content:

```env
# Database Credentials
PGPASSWORD=<set-a-database-password>
PGUSER=HoundSec
PGPORT=5432
PGDATABASE=clickstat
VERIFY_URL=true # set to false to disable URL verification
# API Tokens
IP_INFO_TOKEN=<API token from ipinfo.io> #optional
SAFE_BROWSING_TOKEN=<API token from Google Safe Browsing API> #optional
```

- If you don't want URL verification or don't have access to the Google Safe Browsing API, you can set `VERIFY_URL` to `false`. The URL shortening will proceed without checking for malicious URLs.
- If the `IP_INFO_TOKEN` is not set, IP lookups will be disabled, but the rest of the app will work normally.

Run the following command:

```bash
docker-compose up -d
```

This will spin up two containers: one running the Gunicorn WSGI server on port 8000 (mapped to localhost) and another running the PostgreSQL database.

For production, configure **nginx** as a proxy server and install an SSL certificate using **certbot**. Set up **cron jobs** for backup and restore of the database for data safety.

---

This version includes the `VERIFY_URL` option and explains how both APIs are optional depending on the functionality you want to enable.

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
