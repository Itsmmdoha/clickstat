SELECT ip, user_agent, latitude, longitude, timestamp from data where identifier=%(identifier)s ORDER BY timestamp DESC;
