USE calculadora_db;

-- Total de operações
SELECT COUNT(*) AS total_operations
FROM operations;

-- Sucesso vs erro
SELECT status, COUNT(*) AS total
FROM operations
GROUP BY status;

-- Operadores mais usados
SELECT operator, COUNT(*) AS total
FROM operations
GROUP BY operator
ORDER BY total DESC;

-- Taxa de erro (%)
SELECT
  ROUND(
    100 * SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) / COUNT(*),
    2
  ) AS error_rate_percent
FROM operations;

-- Top 5 mensagens de erro
SELECT error_message, COUNT(*) AS total
FROM operations
WHERE status = 'error'
GROUP BY error_message
ORDER BY total DESC
LIMIT 5;
