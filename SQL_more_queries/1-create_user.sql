-- creates a user user_0d_1 with password user_0d_1_pwd
-- user_0d_1 should have all privileges on your MYSQL server
-- the user_0d_1 set of password to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
REVOKE AUDIT_ABORT_EXEMPT, FIREWALL_EXEMPT, AUTHENTICATION_POLICY_ADMIN, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost';
