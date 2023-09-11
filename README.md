# Clickstat
Clickstat is a URL shortener with IP and GPS logging. It logs information like IP address User-Agent and GPS-Coordinates if GPS Tracking is enabled.
Access it at [clickstat.xyz](https://clickstat.xyz)

## Features

1. IP Logging
2. User-Agent Logging
3. GPS Loggin

## Run Locally

>steps:
>1. Setup PostgreSQL
>2. Set Environment Variables
>3. Install Requirements
>4. Run main.py

### Step1:

Install PostgreSQL and Collect the collect/set your database credentials 

### Step2:

The flask app collects the database credentials from your Environment Variables. To set the Variables, add the following lines to your .bashrc or .zshrc file
```bash
export PGPASSWORD='your_database_password'
export PGHOST='your_host'
export PGUSER='your_username'
export PGPORT='your_port_number'
export PGDATABASE='your_database_name'

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

### Step3:

Now it's time to install the Requirements. Go to the clickstat directory and type,
```bash
pip install -r requirements.txt
```
### Step4:

Everything is set-up! Now just run the main.py file with python3.
