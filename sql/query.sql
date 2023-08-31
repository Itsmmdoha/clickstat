SELECT click_data.id, click_data.user_agent, click_data.ip_address, click_data.timestamp,
       links.shortcode, links.actual_link
FROM click_data
LEFT JOIN links ON click_data.link_id = links.id
WHERE links.shortcode = 'ABC123'
LIMIT 10;  -- Limit the result to 10 rows

