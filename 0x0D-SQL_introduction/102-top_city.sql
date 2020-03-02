-- Temperatures
-- script that displays top 3 of cities temperature during July.
SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month = 7 or month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
