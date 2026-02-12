CREATE DATABASE IF NOT EXISTS calculadora_db;
USE calculadora_db;

CREATE TABLE IF NOT EXISTS operations (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    a DOUBLE NOT NULL,
    b DOUBLE NOT NULL,
    operator VARCHAR(5) NOT NULL,

    result DOUBLE NULL,
    status VARCHAR(10) NOT NULL,
    error_message VARCHAR(255) NULL
);

CREATE INDEX idx_operations_created_at ON operations (created_at);
CREATE INDEX idx_operations_operator ON operations (operator);
CREATE INDEX idx_operations_status ON operations (status);