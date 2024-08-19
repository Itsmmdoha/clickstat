#!/bin/bash
docker compose exec db pg_dump -d clickstat --no-owner -f /backups/db_backup$(date +%d-%m-%Y).sql
echo db_backup$(date +%d-%m-%Y).sql :::: Successful
