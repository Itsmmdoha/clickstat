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

## Run Locally

>steps:
>1. Setup PostgreSQL
>2. Get API token from ipinfo.io
>3. Set Environment Variables
>4. Install Requirements
>5. Run main.py

### Step1:

Install PostgreSQL and Collect the collect/set your database credentials 

### Step2:

This Flask app uses the ipinfo.io API. Get your API token from [here.](https://ipinfo.io/).

### Step3:

The flask app collects the API and database credentials from your Environment Variables. To set the Variables, add the following lines to your .bashrc or .zshrc file
```bash
# Databse Creds
export PGPASSWORD='your_database_password'
export PGHOST='your_host'
export PGUSER='your_username'
export PGPORT='your_port_number'
export PGDATABASE='your_database_name'
# API token
export API_TOKEN='your ipinfo.io api token'

```
Make sure to replace accordingly with the actual credentials. After adding these lines, source the file by
```bash
source .bashrc
```
or by
```bash
source .zshrc
```
if you're using zsh.

### Step4:

Now it's time to install the Requirements. Go to the clickstat directory and type,
```bash
pip install -r requirements.txt
```
### Step5:

Everything is set-up! Now just run the main.py file with python3.
