CREATE VIEW IF NOT EXISTS log_commands AS
SELECT u.username, c.command
FROM users AS u
JOIN logs AS l ON l.id_user = u.id
JOIN commands AS c ON c.id = l.id_command;