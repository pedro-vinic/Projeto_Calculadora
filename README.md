# 📊 Calculator Data Logger

Projeto desenvolvido em Python que evolui uma calculadora simples para um sistema com persistência em MySQL e geração de relatórios analíticos.

Este projeto demonstra habilidades em:

- Arquitetura modular em Python
- Tratamento estruturado de exceções
- Persistência de dados em MySQL
- Consultas analíticas com SQL
- Geração de relatórios em CSV
- Pipeline simples de dados

---

## 🧠 Arquitetura do Projeto

```
main.py        → Interface da aplicação (loop principal)
calculadora.py → Validação de entrada e fluxo da operação
operadores.py  → Operações matemáticas
erros.py       → Exceções customizadas
db.py          → Conexão e persistência no MySQL
report.py      → Geração de relatórios analíticos
sql/           → Script de criação do banco
exports/       → Relatórios CSV gerados
```

---

## 🗄️ Modelagem do Banco de Dados

Tabela: `operations`

| Campo         | Tipo        | Descrição |
|---------------|------------|------------|
| id            | BIGINT     | Identificador único |
| created_at    | TIMESTAMP  | Data e hora da operação |
| a             | DOUBLE     | Primeiro número |
| b             | DOUBLE     | Segundo número |
| operator      | VARCHAR    | Operador matemático |
| result        | DOUBLE     | Resultado (NULL em caso de erro) |
| status        | VARCHAR    | success / error |
| error_message | VARCHAR    | Mensagem de erro (se houver) |

---

## 📈 Métricas Disponíveis

O sistema permite analisar:

- Total de operações realizadas
- Distribuição entre sucessos e erros
- Operadores mais utilizados
- Taxa de erro (%)
- Principais mensagens de erro

---

## 🚀 Como Executar o Projeto

### 1️⃣ Criar o banco MySQL

Abra o MySQL Workbench e execute o script:

```
sql/schema.sql
```

Ou execute manualmente:

```sql
CREATE DATABASE calculadora_db;
USE calculadora_db;
```

---

### 2️⃣ Executar a aplicação

```bash
python main.py
```

A senha do MySQL será solicitada no terminal.

---

### 3️⃣ Gerar relatório analítico

```bash
python report.py
```

Os arquivos CSV serão gerados na pasta:

```
exports/
```

Arquivos gerados:

- status_counts.csv
- operator_counts.csv
- kpis.csv

---

## 📊 Fluxo de Dados

```
Usuário → Python → MySQL → SQL Analytics → CSV
```

---

## 🛠 Tecnologias Utilizadas

- Python 3
- MySQL
- mysql-connector-python
- SQL
- CSV
- getpass

---

## 🔒 Segurança

A senha do MySQL é solicitada via `getpass`, não ficando armazenada diretamente no código.

---

## 📌 Possíveis Evoluções

- Testes automatizados com pytest
- Integração contínua com GitHub Actions
- Containerização com Docker
- Dashboard analítico com Streamlit
- Uso de ORM (SQLAlchemy)

---

## 🎯 Objetivo do Projeto

Demonstrar domínio em:

- Manipulação e persistência de dados
- Modelagem relacional
- Consultas agregadas em SQL
- Pipeline simples de dados
- Organização modular de código

---

Projeto desenvolvido como parte de portfólio voltado para a área de Dados e Backend Python.

